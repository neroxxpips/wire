# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wirepas_messaging/gateway/data_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wirepas_messaging.gateway import wp_global_pb2 as wirepas__messaging_dot_gateway_dot_wp__global__pb2
from wirepas_messaging.nanopb import nanopb_pb2 as wirepas__messaging_dot_nanopb_dot_nanopb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='wirepas_messaging/gateway/data_message.proto',
  package='com.wirepas.proto.gateway',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n,wirepas_messaging/gateway/data_message.proto\x12\x19\x63om.wirepas.proto.gateway\x1a)wirepas_messaging/gateway/wp_global.proto\x1a%wirepas_messaging/nanopb/nanopb.proto\"\x8a\x02\n\rSendPacketReq\x12\x38\n\x06header\x18\x01 \x02(\x0b\x32(.com.wirepas.proto.gateway.RequestHeader\x12\x1b\n\x13\x64\x65stination_address\x18\x02 \x02(\r\x12\x17\n\x0fsource_endpoint\x18\x03 \x02(\r\x12\x1c\n\x14\x64\x65stination_endpoint\x18\x04 \x02(\r\x12\x0b\n\x03qos\x18\x05 \x02(\r\x12\x17\n\x07payload\x18\x06 \x02(\x0c\x42\x06\x92?\x03\x08\x80\x08\x12\x18\n\x10initial_delay_ms\x18\x07 \x01(\r\x12\x18\n\x10is_unack_csma_ca\x18\x08 \x01(\x08\x12\x11\n\thop_limit\x18\t \x01(\r\"K\n\x0eSendPacketResp\x12\x39\n\x06header\x18\x01 \x02(\x0b\x32).com.wirepas.proto.gateway.ResponseHeader\"\xba\x02\n\x13PacketReceivedEvent\x12\x36\n\x06header\x18\x01 \x02(\x0b\x32&.com.wirepas.proto.gateway.EventHeader\x12\x16\n\x0esource_address\x18\x02 \x02(\r\x12\x1b\n\x13\x64\x65stination_address\x18\x03 \x02(\r\x12\x17\n\x0fsource_endpoint\x18\x04 \x02(\r\x12\x1c\n\x14\x64\x65stination_endpoint\x18\x05 \x02(\r\x12\x16\n\x0etravel_time_ms\x18\x06 \x02(\r\x12\x18\n\x10rx_time_ms_epoch\x18\x07 \x02(\x04\x12\x0b\n\x03qos\x18\x08 \x02(\r\x12\x17\n\x07payload\x18\t \x01(\x0c\x42\x06\x92?\x03\x08\x80\x08\x12\x14\n\x0cpayload_size\x18\n \x01(\r\x12\x11\n\thop_count\x18\x0b \x01(\r')
  ,
  dependencies=[wirepas__messaging_dot_gateway_dot_wp__global__pb2.DESCRIPTOR,wirepas__messaging_dot_nanopb_dot_nanopb__pb2.DESCRIPTOR,])




_SENDPACKETREQ = _descriptor.Descriptor(
  name='SendPacketReq',
  full_name='com.wirepas.proto.gateway.SendPacketReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='com.wirepas.proto.gateway.SendPacketReq.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destination_address', full_name='com.wirepas.proto.gateway.SendPacketReq.destination_address', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_endpoint', full_name='com.wirepas.proto.gateway.SendPacketReq.source_endpoint', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destination_endpoint', full_name='com.wirepas.proto.gateway.SendPacketReq.destination_endpoint', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qos', full_name='com.wirepas.proto.gateway.SendPacketReq.qos', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='com.wirepas.proto.gateway.SendPacketReq.payload', index=5,
      number=6, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\003\010\200\010'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initial_delay_ms', full_name='com.wirepas.proto.gateway.SendPacketReq.initial_delay_ms', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_unack_csma_ca', full_name='com.wirepas.proto.gateway.SendPacketReq.is_unack_csma_ca', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hop_limit', full_name='com.wirepas.proto.gateway.SendPacketReq.hop_limit', index=8,
      number=9, type=13, cpp_type=3, label=1,
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
  serialized_start=158,
  serialized_end=424,
)


_SENDPACKETRESP = _descriptor.Descriptor(
  name='SendPacketResp',
  full_name='com.wirepas.proto.gateway.SendPacketResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='com.wirepas.proto.gateway.SendPacketResp.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=426,
  serialized_end=501,
)


_PACKETRECEIVEDEVENT = _descriptor.Descriptor(
  name='PacketReceivedEvent',
  full_name='com.wirepas.proto.gateway.PacketReceivedEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='com.wirepas.proto.gateway.PacketReceivedEvent.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_address', full_name='com.wirepas.proto.gateway.PacketReceivedEvent.source_address', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destination_address', full_name='com.wirepas.proto.gateway.PacketReceivedEvent.destination_address', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_endpoint', full_name='com.wirepas.proto.gateway.PacketReceivedEvent.source_endpoint', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destination_endpoint', full_name='com.wirepas.proto.gateway.PacketReceivedEvent.destination_endpoint', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='travel_time_ms', full_name='com.wirepas.proto.gateway.PacketReceivedEvent.travel_time_ms', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rx_time_ms_epoch', full_name='com.wirepas.proto.gateway.PacketReceivedEvent.rx_time_ms_epoch', index=6,
      number=7, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qos', full_name='com.wirepas.proto.gateway.PacketReceivedEvent.qos', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='com.wirepas.proto.gateway.PacketReceivedEvent.payload', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\003\010\200\010'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload_size', full_name='com.wirepas.proto.gateway.PacketReceivedEvent.payload_size', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hop_count', full_name='com.wirepas.proto.gateway.PacketReceivedEvent.hop_count', index=10,
      number=11, type=13, cpp_type=3, label=1,
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
  serialized_start=504,
  serialized_end=818,
)

_SENDPACKETREQ.fields_by_name['header'].message_type = wirepas__messaging_dot_gateway_dot_wp__global__pb2._REQUESTHEADER
_SENDPACKETRESP.fields_by_name['header'].message_type = wirepas__messaging_dot_gateway_dot_wp__global__pb2._RESPONSEHEADER
_PACKETRECEIVEDEVENT.fields_by_name['header'].message_type = wirepas__messaging_dot_gateway_dot_wp__global__pb2._EVENTHEADER
DESCRIPTOR.message_types_by_name['SendPacketReq'] = _SENDPACKETREQ
DESCRIPTOR.message_types_by_name['SendPacketResp'] = _SENDPACKETRESP
DESCRIPTOR.message_types_by_name['PacketReceivedEvent'] = _PACKETRECEIVEDEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SendPacketReq = _reflection.GeneratedProtocolMessageType('SendPacketReq', (_message.Message,), {
  'DESCRIPTOR' : _SENDPACKETREQ,
  '__module__' : 'wirepas_messaging.gateway.data_message_pb2'
  # @@protoc_insertion_point(class_scope:com.wirepas.proto.gateway.SendPacketReq)
  })
_sym_db.RegisterMessage(SendPacketReq)

SendPacketResp = _reflection.GeneratedProtocolMessageType('SendPacketResp', (_message.Message,), {
  'DESCRIPTOR' : _SENDPACKETRESP,
  '__module__' : 'wirepas_messaging.gateway.data_message_pb2'
  # @@protoc_insertion_point(class_scope:com.wirepas.proto.gateway.SendPacketResp)
  })
_sym_db.RegisterMessage(SendPacketResp)

PacketReceivedEvent = _reflection.GeneratedProtocolMessageType('PacketReceivedEvent', (_message.Message,), {
  'DESCRIPTOR' : _PACKETRECEIVEDEVENT,
  '__module__' : 'wirepas_messaging.gateway.data_message_pb2'
  # @@protoc_insertion_point(class_scope:com.wirepas.proto.gateway.PacketReceivedEvent)
  })
_sym_db.RegisterMessage(PacketReceivedEvent)


_SENDPACKETREQ.fields_by_name['payload']._options = None
_PACKETRECEIVEDEVENT.fields_by_name['payload']._options = None
# @@protoc_insertion_point(module_scope)
