# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from steward import maintenance_pb2 as steward_dot_maintenance__pb2
from steward import user_pb2 as steward_dot_user__pb2


class UserServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetUser = channel.unary_unary(
        '/steward.UserService/GetUser',
        request_serializer=steward_dot_user__pb2.GetUserRequest.SerializeToString,
        response_deserializer=steward_dot_user__pb2.User.FromString,
        )
    self.CreateUser = channel.unary_unary(
        '/steward.UserService/CreateUser',
        request_serializer=steward_dot_user__pb2.CreateUserRequest.SerializeToString,
        response_deserializer=steward_dot_user__pb2.User.FromString,
        )
    self.DeleteUser = channel.unary_unary(
        '/steward.UserService/DeleteUser',
        request_serializer=steward_dot_user__pb2.DeleteUserRequest.SerializeToString,
        response_deserializer=steward_dot_user__pb2.User.FromString,
        )
    self.UpdateUser = channel.unary_unary(
        '/steward.UserService/UpdateUser',
        request_serializer=steward_dot_user__pb2.UpdateUserRequest.SerializeToString,
        response_deserializer=steward_dot_user__pb2.User.FromString,
        )
    self.ListUsers = channel.unary_stream(
        '/steward.UserService/ListUsers',
        request_serializer=steward_dot_user__pb2.ListUsersRequest.SerializeToString,
        response_deserializer=steward_dot_user__pb2.User.FromString,
        )


class UserServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListUsers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetUser': grpc.unary_unary_rpc_method_handler(
          servicer.GetUser,
          request_deserializer=steward_dot_user__pb2.GetUserRequest.FromString,
          response_serializer=steward_dot_user__pb2.User.SerializeToString,
      ),
      'CreateUser': grpc.unary_unary_rpc_method_handler(
          servicer.CreateUser,
          request_deserializer=steward_dot_user__pb2.CreateUserRequest.FromString,
          response_serializer=steward_dot_user__pb2.User.SerializeToString,
      ),
      'DeleteUser': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteUser,
          request_deserializer=steward_dot_user__pb2.DeleteUserRequest.FromString,
          response_serializer=steward_dot_user__pb2.User.SerializeToString,
      ),
      'UpdateUser': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateUser,
          request_deserializer=steward_dot_user__pb2.UpdateUserRequest.FromString,
          response_serializer=steward_dot_user__pb2.User.SerializeToString,
      ),
      'ListUsers': grpc.unary_stream_rpc_method_handler(
          servicer.ListUsers,
          request_deserializer=steward_dot_user__pb2.ListUsersRequest.FromString,
          response_serializer=steward_dot_user__pb2.User.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'steward.UserService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class MaintenanceServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetMaintenance = channel.unary_unary(
        '/steward.MaintenanceService/GetMaintenance',
        request_serializer=steward_dot_maintenance__pb2.GetMaintenanceRequest.SerializeToString,
        response_deserializer=steward_dot_maintenance__pb2.Maintenance.FromString,
        )
    self.CreateMaintenance = channel.unary_unary(
        '/steward.MaintenanceService/CreateMaintenance',
        request_serializer=steward_dot_maintenance__pb2.CreateMaintenanceRequest.SerializeToString,
        response_deserializer=steward_dot_maintenance__pb2.Maintenance.FromString,
        )
    self.DeleteMaintenance = channel.unary_unary(
        '/steward.MaintenanceService/DeleteMaintenance',
        request_serializer=steward_dot_maintenance__pb2.DeleteMaintenanceRequest.SerializeToString,
        response_deserializer=steward_dot_maintenance__pb2.Maintenance.FromString,
        )
    self.UpdateMaintenance = channel.unary_unary(
        '/steward.MaintenanceService/UpdateMaintenance',
        request_serializer=steward_dot_maintenance__pb2.UpdateMaintenanceRequest.SerializeToString,
        response_deserializer=steward_dot_maintenance__pb2.Maintenance.FromString,
        )
    self.ListMaintenances = channel.unary_stream(
        '/steward.MaintenanceService/ListMaintenances',
        request_serializer=steward_dot_maintenance__pb2.ListMaintenancesRequest.SerializeToString,
        response_deserializer=steward_dot_maintenance__pb2.Maintenance.FromString,
        )


class MaintenanceServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetMaintenance(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateMaintenance(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteMaintenance(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateMaintenance(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListMaintenances(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MaintenanceServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetMaintenance': grpc.unary_unary_rpc_method_handler(
          servicer.GetMaintenance,
          request_deserializer=steward_dot_maintenance__pb2.GetMaintenanceRequest.FromString,
          response_serializer=steward_dot_maintenance__pb2.Maintenance.SerializeToString,
      ),
      'CreateMaintenance': grpc.unary_unary_rpc_method_handler(
          servicer.CreateMaintenance,
          request_deserializer=steward_dot_maintenance__pb2.CreateMaintenanceRequest.FromString,
          response_serializer=steward_dot_maintenance__pb2.Maintenance.SerializeToString,
      ),
      'DeleteMaintenance': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteMaintenance,
          request_deserializer=steward_dot_maintenance__pb2.DeleteMaintenanceRequest.FromString,
          response_serializer=steward_dot_maintenance__pb2.Maintenance.SerializeToString,
      ),
      'UpdateMaintenance': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateMaintenance,
          request_deserializer=steward_dot_maintenance__pb2.UpdateMaintenanceRequest.FromString,
          response_serializer=steward_dot_maintenance__pb2.Maintenance.SerializeToString,
      ),
      'ListMaintenances': grpc.unary_stream_rpc_method_handler(
          servicer.ListMaintenances,
          request_deserializer=steward_dot_maintenance__pb2.ListMaintenancesRequest.FromString,
          response_serializer=steward_dot_maintenance__pb2.Maintenance.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'steward.MaintenanceService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class MaintenanceDefaultsServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetMaintenanceDefaults = channel.unary_unary(
        '/steward.MaintenanceDefaultsService/GetMaintenanceDefaults',
        request_serializer=steward_dot_maintenance__pb2.GetMaintenanceDefaultsRequest.SerializeToString,
        response_deserializer=steward_dot_maintenance__pb2.Maintenance.FromString,
        )
    self.CreateMaintenanceDefaults = channel.unary_unary(
        '/steward.MaintenanceDefaultsService/CreateMaintenanceDefaults',
        request_serializer=steward_dot_maintenance__pb2.CreateMaintenanceDefaultsRequest.SerializeToString,
        response_deserializer=steward_dot_maintenance__pb2.Maintenance.FromString,
        )
    self.DeleteMaintenanceDefaults = channel.unary_unary(
        '/steward.MaintenanceDefaultsService/DeleteMaintenanceDefaults',
        request_serializer=steward_dot_maintenance__pb2.DeleteMaintenanceDefaultsRequest.SerializeToString,
        response_deserializer=steward_dot_maintenance__pb2.Maintenance.FromString,
        )
    self.UpdateMaintenanceDefaults = channel.unary_unary(
        '/steward.MaintenanceDefaultsService/UpdateMaintenanceDefaults',
        request_serializer=steward_dot_maintenance__pb2.UpdateMaintenanceDefaultsRequest.SerializeToString,
        response_deserializer=steward_dot_maintenance__pb2.Maintenance.FromString,
        )
    self.ListMaintenanceDefaults = channel.unary_stream(
        '/steward.MaintenanceDefaultsService/ListMaintenanceDefaults',
        request_serializer=steward_dot_maintenance__pb2.ListMaintenanceDefaultsRequest.SerializeToString,
        response_deserializer=steward_dot_maintenance__pb2.Maintenance.FromString,
        )


class MaintenanceDefaultsServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetMaintenanceDefaults(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateMaintenanceDefaults(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteMaintenanceDefaults(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateMaintenanceDefaults(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListMaintenanceDefaults(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MaintenanceDefaultsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetMaintenanceDefaults': grpc.unary_unary_rpc_method_handler(
          servicer.GetMaintenanceDefaults,
          request_deserializer=steward_dot_maintenance__pb2.GetMaintenanceDefaultsRequest.FromString,
          response_serializer=steward_dot_maintenance__pb2.Maintenance.SerializeToString,
      ),
      'CreateMaintenanceDefaults': grpc.unary_unary_rpc_method_handler(
          servicer.CreateMaintenanceDefaults,
          request_deserializer=steward_dot_maintenance__pb2.CreateMaintenanceDefaultsRequest.FromString,
          response_serializer=steward_dot_maintenance__pb2.Maintenance.SerializeToString,
      ),
      'DeleteMaintenanceDefaults': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteMaintenanceDefaults,
          request_deserializer=steward_dot_maintenance__pb2.DeleteMaintenanceDefaultsRequest.FromString,
          response_serializer=steward_dot_maintenance__pb2.Maintenance.SerializeToString,
      ),
      'UpdateMaintenanceDefaults': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateMaintenanceDefaults,
          request_deserializer=steward_dot_maintenance__pb2.UpdateMaintenanceDefaultsRequest.FromString,
          response_serializer=steward_dot_maintenance__pb2.Maintenance.SerializeToString,
      ),
      'ListMaintenanceDefaults': grpc.unary_stream_rpc_method_handler(
          servicer.ListMaintenanceDefaults,
          request_deserializer=steward_dot_maintenance__pb2.ListMaintenanceDefaultsRequest.FromString,
          response_serializer=steward_dot_maintenance__pb2.Maintenance.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'steward.MaintenanceDefaultsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
