# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wirepas_messaging/gateway/wp_global.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wirepas_messaging.gateway import error_pb2 as wirepas__messaging_dot_gateway_dot_error__pb2
from wirepas_messaging.nanopb import nanopb_pb2 as wirepas__messaging_dot_nanopb_dot_nanopb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='wirepas_messaging/gateway/wp_global.proto',
  package='com.wirepas.proto.gateway',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n)wirepas_messaging/gateway/wp_global.proto\x12\x19\x63om.wirepas.proto.gateway\x1a%wirepas_messaging/gateway/error.proto\x1a%wirepas_messaging/nanopb/nanopb.proto\"8\n\rRequestHeader\x12\x0e\n\x06req_id\x18\x01 \x02(\x04\x12\x17\n\x07sink_id\x18\x02 \x01(\tB\x06\x92?\x03\x08\x80\x01\"\x83\x01\n\x0eResponseHeader\x12\x0e\n\x06req_id\x18\x01 \x02(\x04\x12\x15\n\x05gw_id\x18\x02 \x02(\tB\x06\x92?\x03\x08\x80\x01\x12\x17\n\x07sink_id\x18\x03 \x01(\tB\x06\x92?\x03\x08\x80\x01\x12\x31\n\x03res\x18\x04 \x02(\x0e\x32$.com.wirepas.proto.gateway.ErrorCode\"O\n\x0b\x45ventHeader\x12\x15\n\x05gw_id\x18\x01 \x02(\tB\x06\x92?\x03\x08\x80\x01\x12\x17\n\x07sink_id\x18\x02 \x01(\tB\x06\x92?\x03\x08\x80\x01\x12\x10\n\x08\x65vent_id\x18\x03 \x02(\x04\"K\n\x0f\x46irmwareVersion\x12\r\n\x05major\x18\x01 \x02(\r\x12\r\n\x05minor\x18\x02 \x02(\r\x12\r\n\x05maint\x18\x03 \x02(\r\x12\x0b\n\x03\x64\x65v\x18\x04 \x02(\r*\x1d\n\nOnOffState\x12\x06\n\x02ON\x10\x01\x12\x07\n\x03OFF\x10\x02')
  ,
  dependencies=[wirepas__messaging_dot_gateway_dot_error__pb2.DESCRIPTOR,wirepas__messaging_dot_nanopb_dot_nanopb__pb2.DESCRIPTOR,])

_ONOFFSTATE = _descriptor.EnumDescriptor(
  name='OnOffState',
  full_name='com.wirepas.proto.gateway.OnOffState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ON', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OFF', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=500,
  serialized_end=529,
)
_sym_db.RegisterEnumDescriptor(_ONOFFSTATE)

OnOffState = enum_type_wrapper.EnumTypeWrapper(_ONOFFSTATE)
ON = 1
OFF = 2



_REQUESTHEADER = _descriptor.Descriptor(
  name='RequestHeader',
  full_name='com.wirepas.proto.gateway.RequestHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='req_id', full_name='com.wirepas.proto.gateway.RequestHeader.req_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sink_id', full_name='com.wirepas.proto.gateway.RequestHeader.sink_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\003\010\200\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=206,
)


_RESPONSEHEADER = _descriptor.Descriptor(
  name='ResponseHeader',
  full_name='com.wirepas.proto.gateway.ResponseHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='req_id', full_name='com.wirepas.proto.gateway.ResponseHeader.req_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gw_id', full_name='com.wirepas.proto.gateway.ResponseHeader.gw_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\003\010\200\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sink_id', full_name='com.wirepas.proto.gateway.ResponseHeader.sink_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\003\010\200\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='res', full_name='com.wirepas.proto.gateway.ResponseHeader.res', index=3,
      number=4, type=14, cpp_type=8, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=209,
  serialized_end=340,
)


_EVENTHEADER = _descriptor.Descriptor(
  name='EventHeader',
  full_name='com.wirepas.proto.gateway.EventHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gw_id', full_name='com.wirepas.proto.gateway.EventHeader.gw_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\003\010\200\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sink_id', full_name='com.wirepas.proto.gateway.EventHeader.sink_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\003\010\200\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_id', full_name='com.wirepas.proto.gateway.EventHeader.event_id', index=2,
      number=3, type=4, cpp_type=4, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=342,
  serialized_end=421,
)


_FIRMWAREVERSION = _descriptor.Descriptor(
  name='FirmwareVersion',
  full_name='com.wirepas.proto.gateway.FirmwareVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='major', full_name='com.wirepas.proto.gateway.FirmwareVersion.major', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minor', full_name='com.wirepas.proto.gateway.FirmwareVersion.minor', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maint', full_name='com.wirepas.proto.gateway.FirmwareVersion.maint', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev', full_name='com.wirepas.proto.gateway.FirmwareVersion.dev', index=3,
      number=4, type=13, cpp_type=3, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=423,
  serialized_end=498,
)

_RESPONSEHEADER.fields_by_name['res'].enum_type = wirepas__messaging_dot_gateway_dot_error__pb2._ERRORCODE
DESCRIPTOR.message_types_by_name['RequestHeader'] = _REQUESTHEADER
DESCRIPTOR.message_types_by_name['ResponseHeader'] = _RESPONSEHEADER
DESCRIPTOR.message_types_by_name['EventHeader'] = _EVENTHEADER
DESCRIPTOR.message_types_by_name['FirmwareVersion'] = _FIRMWAREVERSION
DESCRIPTOR.enum_types_by_name['OnOffState'] = _ONOFFSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestHeader = _reflection.GeneratedProtocolMessageType('RequestHeader', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTHEADER,
  '__module__' : 'wirepas_messaging.gateway.wp_global_pb2'
  # @@protoc_insertion_point(class_scope:com.wirepas.proto.gateway.RequestHeader)
  })
_sym_db.RegisterMessage(RequestHeader)

ResponseHeader = _reflection.GeneratedProtocolMessageType('ResponseHeader', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEHEADER,
  '__module__' : 'wirepas_messaging.gateway.wp_global_pb2'
  # @@protoc_insertion_point(class_scope:com.wirepas.proto.gateway.ResponseHeader)
  })
_sym_db.RegisterMessage(ResponseHeader)

EventHeader = _reflection.GeneratedProtocolMessageType('EventHeader', (_message.Message,), {
  'DESCRIPTOR' : _EVENTHEADER,
  '__module__' : 'wirepas_messaging.gateway.wp_global_pb2'
  # @@protoc_insertion_point(class_scope:com.wirepas.proto.gateway.EventHeader)
  })
_sym_db.RegisterMessage(EventHeader)

FirmwareVersion = _reflection.GeneratedProtocolMessageType('FirmwareVersion', (_message.Message,), {
  'DESCRIPTOR' : _FIRMWAREVERSION,
  '__module__' : 'wirepas_messaging.gateway.wp_global_pb2'
  # @@protoc_insertion_point(class_scope:com.wirepas.proto.gateway.FirmwareVersion)
  })
_sym_db.RegisterMessage(FirmwareVersion)


_REQUESTHEADER.fields_by_name['sink_id']._options = None
_RESPONSEHEADER.fields_by_name['gw_id']._options = None
_RESPONSEHEADER.fields_by_name['sink_id']._options = None
_EVENTHEADER.fields_by_name['gw_id']._options = None
_EVENTHEADER.fields_by_name['sink_id']._options = None
# @@protoc_insertion_point(module_scope)
