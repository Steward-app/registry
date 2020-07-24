# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steward/schedule.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='steward/schedule.proto',
  package='steward',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16steward/schedule.proto\x12\x07steward\x1a\x1egoogle/protobuf/duration.proto\"\xcb\x01\n\x08Schedule\x12\x0b\n\x03_id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12#\n\x04type\x18\x03 \x01(\x0e\x32\x15.steward.ScheduleType\x12+\n\x08interval\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x1f\n\x06snooze\x18\x05 \x01(\x0b\x32\x0f.steward.Snooze\x12*\n\x11\x61vailable_snoozes\x18\x06 \x03(\x0b\x32\x0f.steward.Snooze\"J\n\x06Snooze\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12+\n\x08\x64uration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration**\n\x0cScheduleType\x12\x0c\n\x08\x44URATION\x10\x00\x12\x0c\n\x08\x45XTERNAL\x10\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])

_SCHEDULETYPE = _descriptor.EnumDescriptor(
  name='ScheduleType',
  full_name='steward.ScheduleType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DURATION', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXTERNAL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=349,
  serialized_end=391,
)
_sym_db.RegisterEnumDescriptor(_SCHEDULETYPE)

ScheduleType = enum_type_wrapper.EnumTypeWrapper(_SCHEDULETYPE)
DURATION = 0
EXTERNAL = 1



_SCHEDULE = _descriptor.Descriptor(
  name='Schedule',
  full_name='steward.Schedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='_id', full_name='steward.Schedule._id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='steward.Schedule.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='steward.Schedule.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='interval', full_name='steward.Schedule.interval', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='snooze', full_name='steward.Schedule.snooze', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='available_snoozes', full_name='steward.Schedule.available_snoozes', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=68,
  serialized_end=271,
)


_SNOOZE = _descriptor.Descriptor(
  name='Snooze',
  full_name='steward.Snooze',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='steward.Snooze.description', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='duration', full_name='steward.Snooze.duration', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=273,
  serialized_end=347,
)

_SCHEDULE.fields_by_name['type'].enum_type = _SCHEDULETYPE
_SCHEDULE.fields_by_name['interval'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_SCHEDULE.fields_by_name['snooze'].message_type = _SNOOZE
_SCHEDULE.fields_by_name['available_snoozes'].message_type = _SNOOZE
_SNOOZE.fields_by_name['duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
DESCRIPTOR.message_types_by_name['Schedule'] = _SCHEDULE
DESCRIPTOR.message_types_by_name['Snooze'] = _SNOOZE
DESCRIPTOR.enum_types_by_name['ScheduleType'] = _SCHEDULETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Schedule = _reflection.GeneratedProtocolMessageType('Schedule', (_message.Message,), {
  'DESCRIPTOR' : _SCHEDULE,
  '__module__' : 'steward.schedule_pb2'
  # @@protoc_insertion_point(class_scope:steward.Schedule)
  })
_sym_db.RegisterMessage(Schedule)

Snooze = _reflection.GeneratedProtocolMessageType('Snooze', (_message.Message,), {
  'DESCRIPTOR' : _SNOOZE,
  '__module__' : 'steward.schedule_pb2'
  # @@protoc_insertion_point(class_scope:steward.Snooze)
  })
_sym_db.RegisterMessage(Snooze)


# @@protoc_insertion_point(module_scope)
