# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steward/registry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from steward import user_pb2 as steward_dot_user__pb2
from steward import maintenance_pb2 as steward_dot_maintenance__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='steward/registry.proto',
  package='steward',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16steward/registry.proto\x12\x07steward\x1a\x12steward/user.proto\x1a\x19steward/maintenance.proto2\xae\x02\n\x0bUserService\x12\x33\n\x07GetUser\x12\x17.steward.GetUserRequest\x1a\r.steward.User\"\x00\x12\x39\n\nCreateUser\x12\x1a.steward.CreateUserRequest\x1a\r.steward.User\"\x00\x12\x39\n\nDeleteUser\x12\x1a.steward.DeleteUserRequest\x1a\r.steward.User\"\x00\x12\x39\n\nUpdateUser\x12\x1a.steward.UpdateUserRequest\x1a\r.steward.User\"\x00\x12\x39\n\tListUsers\x12\x19.steward.ListUsersRequest\x1a\r.steward.User\"\x00\x30\x01\x32\x9e\x03\n\x12MaintenanceService\x12H\n\x0eGetMaintenance\x12\x1e.steward.GetMaintenanceRequest\x1a\x14.steward.Maintenance\"\x00\x12N\n\x11\x43reateMaintenance\x12!.steward.CreateMaintenanceRequest\x1a\x14.steward.Maintenance\"\x00\x12N\n\x11\x44\x65leteMaintenance\x12!.steward.DeleteMaintenanceRequest\x1a\x14.steward.Maintenance\"\x00\x12N\n\x11UpdateMaintenance\x12!.steward.UpdateMaintenanceRequest\x1a\x14.steward.Maintenance\"\x00\x12N\n\x10ListMaintenances\x12 .steward.ListMaintenancesRequest\x1a\x14.steward.Maintenance\"\x00\x30\x01\x32\xf4\x03\n\x1aMaintenanceDefaultsService\x12X\n\x16GetMaintenanceDefaults\x12&.steward.GetMaintenanceDefaultsRequest\x1a\x14.steward.Maintenance\"\x00\x12^\n\x19\x43reateMaintenanceDefaults\x12).steward.CreateMaintenanceDefaultsRequest\x1a\x14.steward.Maintenance\"\x00\x12^\n\x19\x44\x65leteMaintenanceDefaults\x12).steward.DeleteMaintenanceDefaultsRequest\x1a\x14.steward.Maintenance\"\x00\x12^\n\x19UpdateMaintenanceDefaults\x12).steward.UpdateMaintenanceDefaultsRequest\x1a\x14.steward.Maintenance\"\x00\x12\\\n\x17ListMaintenanceDefaults\x12\'.steward.ListMaintenanceDefaultsRequest\x1a\x14.steward.Maintenance\"\x00\x30\x01\x62\x06proto3')
  ,
  dependencies=[steward_dot_user__pb2.DESCRIPTOR,steward_dot_maintenance__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_USERSERVICE = _descriptor.ServiceDescriptor(
  name='UserService',
  full_name='steward.UserService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=83,
  serialized_end=385,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetUser',
    full_name='steward.UserService.GetUser',
    index=0,
    containing_service=None,
    input_type=steward_dot_user__pb2._GETUSERREQUEST,
    output_type=steward_dot_user__pb2._USER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateUser',
    full_name='steward.UserService.CreateUser',
    index=1,
    containing_service=None,
    input_type=steward_dot_user__pb2._CREATEUSERREQUEST,
    output_type=steward_dot_user__pb2._USER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteUser',
    full_name='steward.UserService.DeleteUser',
    index=2,
    containing_service=None,
    input_type=steward_dot_user__pb2._DELETEUSERREQUEST,
    output_type=steward_dot_user__pb2._USER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateUser',
    full_name='steward.UserService.UpdateUser',
    index=3,
    containing_service=None,
    input_type=steward_dot_user__pb2._UPDATEUSERREQUEST,
    output_type=steward_dot_user__pb2._USER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListUsers',
    full_name='steward.UserService.ListUsers',
    index=4,
    containing_service=None,
    input_type=steward_dot_user__pb2._LISTUSERSREQUEST,
    output_type=steward_dot_user__pb2._USER,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERSERVICE)

DESCRIPTOR.services_by_name['UserService'] = _USERSERVICE


_MAINTENANCESERVICE = _descriptor.ServiceDescriptor(
  name='MaintenanceService',
  full_name='steward.MaintenanceService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=388,
  serialized_end=802,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetMaintenance',
    full_name='steward.MaintenanceService.GetMaintenance',
    index=0,
    containing_service=None,
    input_type=steward_dot_maintenance__pb2._GETMAINTENANCEREQUEST,
    output_type=steward_dot_maintenance__pb2._MAINTENANCE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateMaintenance',
    full_name='steward.MaintenanceService.CreateMaintenance',
    index=1,
    containing_service=None,
    input_type=steward_dot_maintenance__pb2._CREATEMAINTENANCEREQUEST,
    output_type=steward_dot_maintenance__pb2._MAINTENANCE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteMaintenance',
    full_name='steward.MaintenanceService.DeleteMaintenance',
    index=2,
    containing_service=None,
    input_type=steward_dot_maintenance__pb2._DELETEMAINTENANCEREQUEST,
    output_type=steward_dot_maintenance__pb2._MAINTENANCE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateMaintenance',
    full_name='steward.MaintenanceService.UpdateMaintenance',
    index=3,
    containing_service=None,
    input_type=steward_dot_maintenance__pb2._UPDATEMAINTENANCEREQUEST,
    output_type=steward_dot_maintenance__pb2._MAINTENANCE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListMaintenances',
    full_name='steward.MaintenanceService.ListMaintenances',
    index=4,
    containing_service=None,
    input_type=steward_dot_maintenance__pb2._LISTMAINTENANCESREQUEST,
    output_type=steward_dot_maintenance__pb2._MAINTENANCE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MAINTENANCESERVICE)

DESCRIPTOR.services_by_name['MaintenanceService'] = _MAINTENANCESERVICE


_MAINTENANCEDEFAULTSSERVICE = _descriptor.ServiceDescriptor(
  name='MaintenanceDefaultsService',
  full_name='steward.MaintenanceDefaultsService',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  serialized_start=805,
  serialized_end=1305,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetMaintenanceDefaults',
    full_name='steward.MaintenanceDefaultsService.GetMaintenanceDefaults',
    index=0,
    containing_service=None,
    input_type=steward_dot_maintenance__pb2._GETMAINTENANCEDEFAULTSREQUEST,
    output_type=steward_dot_maintenance__pb2._MAINTENANCE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateMaintenanceDefaults',
    full_name='steward.MaintenanceDefaultsService.CreateMaintenanceDefaults',
    index=1,
    containing_service=None,
    input_type=steward_dot_maintenance__pb2._CREATEMAINTENANCEDEFAULTSREQUEST,
    output_type=steward_dot_maintenance__pb2._MAINTENANCE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteMaintenanceDefaults',
    full_name='steward.MaintenanceDefaultsService.DeleteMaintenanceDefaults',
    index=2,
    containing_service=None,
    input_type=steward_dot_maintenance__pb2._DELETEMAINTENANCEDEFAULTSREQUEST,
    output_type=steward_dot_maintenance__pb2._MAINTENANCE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateMaintenanceDefaults',
    full_name='steward.MaintenanceDefaultsService.UpdateMaintenanceDefaults',
    index=3,
    containing_service=None,
    input_type=steward_dot_maintenance__pb2._UPDATEMAINTENANCEDEFAULTSREQUEST,
    output_type=steward_dot_maintenance__pb2._MAINTENANCE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListMaintenanceDefaults',
    full_name='steward.MaintenanceDefaultsService.ListMaintenanceDefaults',
    index=4,
    containing_service=None,
    input_type=steward_dot_maintenance__pb2._LISTMAINTENANCEDEFAULTSREQUEST,
    output_type=steward_dot_maintenance__pb2._MAINTENANCE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MAINTENANCEDEFAULTSSERVICE)

DESCRIPTOR.services_by_name['MaintenanceDefaultsService'] = _MAINTENANCEDEFAULTSSERVICE

# @@protoc_insertion_point(module_scope)
