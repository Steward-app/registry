from concurrent import futures
from absl import logging, flags, app
from box import Box
import yaml

import grpc
from grpc_reflection.v1alpha import reflection

from registry import server_flags, sentry
from registry.decorators import must_have, must_have_any

from proto.steward import schedule_pb2 as s
from proto.steward import registry_pb2_grpc, registry_pb2
from google.protobuf.json_format import MessageToDict, ParseDict

FLAGS = flags.FLAGS

flags.DEFINE_string('schedule_config', 'static/schedules.yaml', 'Path to schedule config')

class ScheduleServiceServicer(registry_pb2_grpc.ScheduleServiceServicer):
    def __init__(self, argv=None):
        with open(FLAGS.schedule_config) as config:
            config = yaml.safe_load(config)
            # Box up the dict to make it's use identical to the storage module
            self.storage = Box(config)
        logging.info('ScheduleService initialized.')

    @must_have('_id', s.Schedule)
    def GetSchedule(self, request, context):
        schedule_id = request._id
        if schedule_id and schedule_id in self.storage.schedules:
            schedule = ParseDict(self.storage.schedules[schedule_id].to_dict(), s.Schedule())
            return schedule
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Schedule "{}" not found.'.format(request))
            return s.Schedule()

    def ListSchedules(self, request, context):
        for schedule in self.storage.schedules:
            yield ParseDict(self.storage.schedules[schedule].to_dict(), s.Schedule())

def serve(argv):
    from registry.monitoring import psi
    sentry.init(FLAGS.sentry)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), interceptors=(psi,))
    registry_pb2_grpc.add_ScheduleServiceServicer_to_server(ScheduleServiceServicer(), server)
    SERVICE_NAMES = (
            registry_pb2.DESCRIPTOR.services_by_name['ScheduleService'].full_name,
            reflection.SERVICE_NAME,
            )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port(FLAGS.listen_addr)
    logging.info('Schedule Microserver listening to: {0}'.format(FLAGS.listen_addr))
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    app.run(serve)
