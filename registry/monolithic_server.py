from concurrent import futures
from absl import logging, flags, app

import grpc
from grpc_reflection.v1alpha import reflection
from proto.steward import user_pb2 as u
from proto.steward import maintenance_pb2 as m
from proto.steward import asset_pb2 as a
from proto.steward import schedule_pb2 as s
from proto.steward import registry_pb2_grpc, registry_pb2
from registry import server_flags, server_info, storage, user_server, maintenance_server, asset_server, schedule_server, sentry
from registry.monitoring import psi

FLAGS = flags.FLAGS


#flags.DEFINE_string('listen_addr', '[::]:50051', 'Address to listen.')

def serve(argv):
    server_info.log_server_info()
    sentry.init(FLAGS.sentry)

    sm = storage.StorageManager()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), interceptors=(psi,))
    registry_pb2_grpc.add_UserServiceServicer_to_server(user_server.UserServiceServicer(storage_manager=sm), server)
    registry_pb2_grpc.add_MaintenanceServiceServicer_to_server(maintenance_server.MaintenanceServiceServicer(storage_manager=sm), server)
    registry_pb2_grpc.add_AssetServiceServicer_to_server(asset_server.AssetServiceServicer(storage_manager=sm), server)
    registry_pb2_grpc.add_ScheduleServiceServicer_to_server(schedule_server.ScheduleServiceServicer(storage_manager=sm), server)
    SERVICE_NAMES = (
            registry_pb2.DESCRIPTOR.services_by_name['UserService'].full_name,
            registry_pb2.DESCRIPTOR.services_by_name['MaintenanceService'].full_name,
            registry_pb2.DESCRIPTOR.services_by_name['AssetService'].full_name,
            registry_pb2.DESCRIPTOR.services_by_name['ScheduleService'].full_name,
            reflection.SERVICE_NAME,
            )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port(FLAGS.listen_addr)
    logging.info('Monolithic Server listening to: {0}'.format(FLAGS.listen_addr))
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    app.run(serve)
