# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steward/user.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from steward import organization_pb2 as steward_dot_organization__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='steward/user.proto',
  package='steward',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12steward/user.proto\x12\x07steward\x1a\x1asteward/organization.proto\"\\\n\x04User\x12\x0b\n\x03_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x18\n\x10\x61vailable_effort\x18\x05 \x01(\x02\"\x7f\n\x03\x41\x43L\x12\x0b\n\x03_id\x18\x01 \x01(\t\x12\x1b\n\x04user\x18\x02 \x01(\x0b\x32\r.steward.User\x12+\n\x0corganization\x18\x03 \x01(\x0b\x32\x15.steward.Organization\x12!\n\x05level\x18\x04 \x01(\x0e\x32\x12.steward.UserLevel\",\n\x0eGetUserRequest\x12\x0b\n\x03_id\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\"\x12\n\x10ListUsersRequest\"\\\n\x11\x43reateUserRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x18\n\x10\x61vailable_effort\x18\x04 \x01(\x02*/\n\tUserLevel\x12\r\n\tANONYMOUS\x10\x00\x12\x08\n\x04USER\x10\x01\x12\t\n\x05OWNER\x10\x02\x62\x06proto3')
  ,
  dependencies=[steward_dot_organization__pb2.DESCRIPTOR,])

_USERLEVEL = _descriptor.EnumDescriptor(
  name='UserLevel',
  full_name='steward.UserLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ANONYMOUS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OWNER', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=442,
  serialized_end=489,
)
_sym_db.RegisterEnumDescriptor(_USERLEVEL)

UserLevel = enum_type_wrapper.EnumTypeWrapper(_USERLEVEL)
ANONYMOUS = 0
USER = 1
OWNER = 2



_USER = _descriptor.Descriptor(
  name='User',
  full_name='steward.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='_id', full_name='steward.User._id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='steward.User.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='steward.User.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='steward.User.email', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='available_effort', full_name='steward.User.available_effort', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=151,
)


_ACL = _descriptor.Descriptor(
  name='ACL',
  full_name='steward.ACL',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='_id', full_name='steward.ACL._id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='steward.ACL.user', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='organization', full_name='steward.ACL.organization', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='steward.ACL.level', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=153,
  serialized_end=280,
)


_GETUSERREQUEST = _descriptor.Descriptor(
  name='GetUserRequest',
  full_name='steward.GetUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='_id', full_name='steward.GetUserRequest._id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='steward.GetUserRequest.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=282,
  serialized_end=326,
)


_LISTUSERSREQUEST = _descriptor.Descriptor(
  name='ListUsersRequest',
  full_name='steward.ListUsersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=328,
  serialized_end=346,
)


_CREATEUSERREQUEST = _descriptor.Descriptor(
  name='CreateUserRequest',
  full_name='steward.CreateUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='steward.CreateUserRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='steward.CreateUserRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='steward.CreateUserRequest.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='available_effort', full_name='steward.CreateUserRequest.available_effort', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=348,
  serialized_end=440,
)

_ACL.fields_by_name['user'].message_type = _USER
_ACL.fields_by_name['organization'].message_type = steward_dot_organization__pb2._ORGANIZATION
_ACL.fields_by_name['level'].enum_type = _USERLEVEL
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['ACL'] = _ACL
DESCRIPTOR.message_types_by_name['GetUserRequest'] = _GETUSERREQUEST
DESCRIPTOR.message_types_by_name['ListUsersRequest'] = _LISTUSERSREQUEST
DESCRIPTOR.message_types_by_name['CreateUserRequest'] = _CREATEUSERREQUEST
DESCRIPTOR.enum_types_by_name['UserLevel'] = _USERLEVEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'steward.user_pb2'
  # @@protoc_insertion_point(class_scope:steward.User)
  })
_sym_db.RegisterMessage(User)

ACL = _reflection.GeneratedProtocolMessageType('ACL', (_message.Message,), {
  'DESCRIPTOR' : _ACL,
  '__module__' : 'steward.user_pb2'
  # @@protoc_insertion_point(class_scope:steward.ACL)
  })
_sym_db.RegisterMessage(ACL)

GetUserRequest = _reflection.GeneratedProtocolMessageType('GetUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERREQUEST,
  '__module__' : 'steward.user_pb2'
  # @@protoc_insertion_point(class_scope:steward.GetUserRequest)
  })
_sym_db.RegisterMessage(GetUserRequest)

ListUsersRequest = _reflection.GeneratedProtocolMessageType('ListUsersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTUSERSREQUEST,
  '__module__' : 'steward.user_pb2'
  # @@protoc_insertion_point(class_scope:steward.ListUsersRequest)
  })
_sym_db.RegisterMessage(ListUsersRequest)

CreateUserRequest = _reflection.GeneratedProtocolMessageType('CreateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERREQUEST,
  '__module__' : 'steward.user_pb2'
  # @@protoc_insertion_point(class_scope:steward.CreateUserRequest)
  })
_sym_db.RegisterMessage(CreateUserRequest)


# @@protoc_insertion_point(module_scope)
