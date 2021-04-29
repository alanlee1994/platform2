# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: signal.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='signal.proto',
  package='Signal',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0csignal.proto\x12\x06Signal\"\xcb\x02\n\x06Signal\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0binstruments\x18\x02 \x01(\t\x12\x11\n\tsignal_ts\x18\x03 \x01(\t\x12%\n\x05Stats\x18\x05 \x03(\x0b\x32\x16.Signal.Signal.Summary\x1a\xe3\x01\n\x07Summary\x12\x11\n\ttotal_cnt\x18\x01 \x01(\x02\x12\x0f\n\x07winrate\x18\x02 \x01(\x02\x12\x0f\n\x07\x61vg_win\x18\x03 \x01(\x02\x12\x10\n\x08\x61vg_lose\x18\x04 \x01(\x02\x12\x12\n\nmedian_win\x18\x05 \x01(\x02\x12\x13\n\x0bmedian_lose\x18\x06 \x01(\x02\x12\x0e\n\x06sharpe\x18\x07 \x01(\x02\x12\r\n\x05kelly\x18\x08 \x01(\x02\x12\x14\n\x0csignal_value\x18\t \x01(\x02\x12\x10\n\x08\x63omments\x18\n \x01(\t\x12\x10\n\x08\x65nter_ts\x18\x0b \x01(\t\x12\x0f\n\x07\x65xit_ts\x18\x0c \x01(\t\"5\n\tHeartbeat\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\n\n\x02ts\x18\x03 \x01(\t'
)




_SIGNAL_SUMMARY = _descriptor.Descriptor(
  name='Summary',
  full_name='Signal.Signal.Summary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='total_cnt', full_name='Signal.Signal.Summary.total_cnt', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='winrate', full_name='Signal.Signal.Summary.winrate', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='avg_win', full_name='Signal.Signal.Summary.avg_win', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='avg_lose', full_name='Signal.Signal.Summary.avg_lose', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='median_win', full_name='Signal.Signal.Summary.median_win', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='median_lose', full_name='Signal.Signal.Summary.median_lose', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sharpe', full_name='Signal.Signal.Summary.sharpe', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kelly', full_name='Signal.Signal.Summary.kelly', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signal_value', full_name='Signal.Signal.Summary.signal_value', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='comments', full_name='Signal.Signal.Summary.comments', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enter_ts', full_name='Signal.Signal.Summary.enter_ts', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exit_ts', full_name='Signal.Signal.Summary.exit_ts', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=356,
)

_SIGNAL = _descriptor.Descriptor(
  name='Signal',
  full_name='Signal.Signal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Signal.Signal.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instruments', full_name='Signal.Signal.instruments', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signal_ts', full_name='Signal.Signal.signal_ts', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Stats', full_name='Signal.Signal.Stats', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SIGNAL_SUMMARY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=356,
)


_HEARTBEAT = _descriptor.Descriptor(
  name='Heartbeat',
  full_name='Signal.Heartbeat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Signal.Heartbeat.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='Signal.Heartbeat.status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ts', full_name='Signal.Heartbeat.ts', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=358,
  serialized_end=411,
)

_SIGNAL_SUMMARY.containing_type = _SIGNAL
_SIGNAL.fields_by_name['Stats'].message_type = _SIGNAL_SUMMARY
DESCRIPTOR.message_types_by_name['Signal'] = _SIGNAL
DESCRIPTOR.message_types_by_name['Heartbeat'] = _HEARTBEAT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Signal = _reflection.GeneratedProtocolMessageType('Signal', (_message.Message,), {

  'Summary' : _reflection.GeneratedProtocolMessageType('Summary', (_message.Message,), {
    'DESCRIPTOR' : _SIGNAL_SUMMARY,
    '__module__' : 'signal_pb2'
    # @@protoc_insertion_point(class_scope:Signal.Signal.Summary)
    })
  ,
  'DESCRIPTOR' : _SIGNAL,
  '__module__' : 'signal_pb2'
  # @@protoc_insertion_point(class_scope:Signal.Signal)
  })
_sym_db.RegisterMessage(Signal)
_sym_db.RegisterMessage(Signal.Summary)

Heartbeat = _reflection.GeneratedProtocolMessageType('Heartbeat', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEAT,
  '__module__' : 'signal_pb2'
  # @@protoc_insertion_point(class_scope:Signal.Heartbeat)
  })
_sym_db.RegisterMessage(Heartbeat)


# @@protoc_insertion_point(module_scope)
