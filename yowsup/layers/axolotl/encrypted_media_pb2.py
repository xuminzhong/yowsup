# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: encrypted_media.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='encrypted_media.proto',
  package='',
  serialized_pb=_b('\n\x15\x65ncrypted_media.proto\"\xb2\x01\n\x05Media\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x10\n\x08mimetype\x18\x02 \x01(\t\x12\x0f\n\x07\x63\x61ption\x18\x03 \x01(\t\x12\x0e\n\x06sha256\x18\x04 \x01(\x0c\x12\x0e\n\x06length\x18\x05 \x01(\x05\x12\x0e\n\x06height\x18\x06 \x01(\x05\x12\r\n\x05width\x18\x07 \x01(\x05\x12\x0e\n\x06refkey\x18\x08 \x01(\x0c\x12\x0b\n\x03key\x18\t \x01(\t\x12\n\n\x02iv\x18\n \x01(\t\x12\x11\n\tthumbnail\x18\x0b \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MEDIA = _descriptor.Descriptor(
  name='Media',
  full_name='Media',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='Media.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mimetype', full_name='Media.mimetype', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='caption', full_name='Media.caption', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sha256', full_name='Media.sha256', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='length', full_name='Media.length', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='Media.height', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width', full_name='Media.width', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='refkey', full_name='Media.refkey', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='Media.key', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iv', full_name='Media.iv', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='thumbnail', full_name='Media.thumbnail', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=204,
)

DESCRIPTOR.message_types_by_name['Media'] = _MEDIA

Media = _reflection.GeneratedProtocolMessageType('Media', (_message.Message,), dict(
  DESCRIPTOR = _MEDIA,
  __module__ = 'encrypted_media_pb2'
  # @@protoc_insertion_point(class_scope:Media)
  ))
_sym_db.RegisterMessage(Media)


# @@protoc_insertion_point(module_scope)
