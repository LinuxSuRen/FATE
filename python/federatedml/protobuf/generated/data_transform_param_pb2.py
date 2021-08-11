# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data-transform-param.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='data-transform-param.proto',
  package='com.webank.ai.fate.core.mlmodel.buffer',
  syntax='proto3',
  serialized_options=_b('B\020DataIOParamProto'),
  serialized_pb=_b('\n\x1a\x64\x61ta-transform-param.proto\x12&com.webank.ai.fate.core.mlmodel.buffer\"\x83\x03\n\x19\x44\x61taTransformImputerParam\x12y\n\x15missing_replace_value\x18\x01 \x03(\x0b\x32Z.com.webank.ai.fate.core.mlmodel.buffer.DataTransformImputerParam.MissingReplaceValueEntry\x12u\n\x13missing_value_ratio\x18\x02 \x03(\x0b\x32X.com.webank.ai.fate.core.mlmodel.buffer.DataTransformImputerParam.MissingValueRatioEntry\x1a:\n\x18MissingReplaceValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x38\n\x16MissingValueRatioEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"\x83\x03\n\x19\x44\x61taTransformOutlierParam\x12y\n\x15outlier_replace_value\x18\x01 \x03(\x0b\x32Z.com.webank.ai.fate.core.mlmodel.buffer.DataTransformOutlierParam.OutlierReplaceValueEntry\x12u\n\x13outlier_value_ratio\x18\x02 \x03(\x0b\x32X.com.webank.ai.fate.core.mlmodel.buffer.DataTransformOutlierParam.OutlierValueRatioEntry\x1a:\n\x18OutlierReplaceValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x38\n\x16OutlierValueRatioEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"\xfe\x01\n\x12\x44\x61taTransformParam\x12\x0e\n\x06header\x18\x01 \x03(\t\x12\x10\n\x08sid_name\x18\x02 \x01(\t\x12\x12\n\nlabel_name\x18\x03 \x01(\t\x12X\n\rimputer_param\x18\x04 \x01(\x0b\x32\x41.com.webank.ai.fate.core.mlmodel.buffer.DataTransformImputerParam\x12X\n\routlier_param\x18\x05 \x01(\x0b\x32\x41.com.webank.ai.fate.core.mlmodel.buffer.DataTransformOutlierParamB\x12\x42\x10\x44\x61taIOParamProtob\x06proto3')
)




_DATATRANSFORMIMPUTERPARAM_MISSINGREPLACEVALUEENTRY = _descriptor.Descriptor(
  name='MissingReplaceValueEntry',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransformImputerParam.MissingReplaceValueEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransformImputerParam.MissingReplaceValueEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransformImputerParam.MissingReplaceValueEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=342,
  serialized_end=400,
)

_DATATRANSFORMIMPUTERPARAM_MISSINGVALUERATIOENTRY = _descriptor.Descriptor(
  name='MissingValueRatioEntry',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransformImputerParam.MissingValueRatioEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransformImputerParam.MissingValueRatioEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransformImputerParam.MissingValueRatioEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=402,
  serialized_end=458,
)

_DATATRANSFORMIMPUTERPARAM = _descriptor.Descriptor(
  name='DataTransformImputerParam',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransformImputerParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='missing_replace_value', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransformImputerParam.missing_replace_value', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='missing_value_ratio', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransformImputerParam.missing_value_ratio', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DATATRANSFORMIMPUTERPARAM_MISSINGREPLACEVALUEENTRY, _DATATRANSFORMIMPUTERPARAM_MISSINGVALUERATIOENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=458,
)


_DATATRANSFORMOUTLIERPARAM_OUTLIERREPLACEVALUEENTRY = _descriptor.Descriptor(
  name='OutlierReplaceValueEntry',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransformOutlierParam.OutlierReplaceValueEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransformOutlierParam.OutlierReplaceValueEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransformOutlierParam.OutlierReplaceValueEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=732,
  serialized_end=790,
)

_DATATRANSFORMOUTLIERPARAM_OUTLIERVALUERATIOENTRY = _descriptor.Descriptor(
  name='OutlierValueRatioEntry',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransformOutlierParam.OutlierValueRatioEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransformOutlierParam.OutlierValueRatioEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransformOutlierParam.OutlierValueRatioEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=792,
  serialized_end=848,
)

_DATATRANSFORMOUTLIERPARAM = _descriptor.Descriptor(
  name='DataTransformOutlierParam',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransformOutlierParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='outlier_replace_value', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransformOutlierParam.outlier_replace_value', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outlier_value_ratio', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransformOutlierParam.outlier_value_ratio', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DATATRANSFORMOUTLIERPARAM_OUTLIERREPLACEVALUEENTRY, _DATATRANSFORMOUTLIERPARAM_OUTLIERVALUERATIOENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=461,
  serialized_end=848,
)


_DATATRANSFORMPARAM = _descriptor.Descriptor(
  name='DataTransformParam',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransformParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransformParam.header', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sid_name', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransformParam.sid_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label_name', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransformParam.label_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='imputer_param', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransformParam.imputer_param', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outlier_param', full_name='com.webank.ai.fate.core.mlmodel.buffer.DataTransformParam.outlier_param', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=851,
  serialized_end=1105,
)

_DATATRANSFORMIMPUTERPARAM_MISSINGREPLACEVALUEENTRY.containing_type = _DATATRANSFORMIMPUTERPARAM
_DATATRANSFORMIMPUTERPARAM_MISSINGVALUERATIOENTRY.containing_type = _DATATRANSFORMIMPUTERPARAM
_DATATRANSFORMIMPUTERPARAM.fields_by_name['missing_replace_value'].message_type = _DATATRANSFORMIMPUTERPARAM_MISSINGREPLACEVALUEENTRY
_DATATRANSFORMIMPUTERPARAM.fields_by_name['missing_value_ratio'].message_type = _DATATRANSFORMIMPUTERPARAM_MISSINGVALUERATIOENTRY
_DATATRANSFORMOUTLIERPARAM_OUTLIERREPLACEVALUEENTRY.containing_type = _DATATRANSFORMOUTLIERPARAM
_DATATRANSFORMOUTLIERPARAM_OUTLIERVALUERATIOENTRY.containing_type = _DATATRANSFORMOUTLIERPARAM
_DATATRANSFORMOUTLIERPARAM.fields_by_name['outlier_replace_value'].message_type = _DATATRANSFORMOUTLIERPARAM_OUTLIERREPLACEVALUEENTRY
_DATATRANSFORMOUTLIERPARAM.fields_by_name['outlier_value_ratio'].message_type = _DATATRANSFORMOUTLIERPARAM_OUTLIERVALUERATIOENTRY
_DATATRANSFORMPARAM.fields_by_name['imputer_param'].message_type = _DATATRANSFORMIMPUTERPARAM
_DATATRANSFORMPARAM.fields_by_name['outlier_param'].message_type = _DATATRANSFORMOUTLIERPARAM
DESCRIPTOR.message_types_by_name['DataTransformImputerParam'] = _DATATRANSFORMIMPUTERPARAM
DESCRIPTOR.message_types_by_name['DataTransformOutlierParam'] = _DATATRANSFORMOUTLIERPARAM
DESCRIPTOR.message_types_by_name['DataTransformParam'] = _DATATRANSFORMPARAM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataTransformImputerParam = _reflection.GeneratedProtocolMessageType('DataTransformImputerParam', (_message.Message,), dict(

  MissingReplaceValueEntry = _reflection.GeneratedProtocolMessageType('MissingReplaceValueEntry', (_message.Message,), dict(
    DESCRIPTOR = _DATATRANSFORMIMPUTERPARAM_MISSINGREPLACEVALUEENTRY,
    __module__ = 'data_transform_param_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.DataTransformImputerParam.MissingReplaceValueEntry)
    ))
  ,

  MissingValueRatioEntry = _reflection.GeneratedProtocolMessageType('MissingValueRatioEntry', (_message.Message,), dict(
    DESCRIPTOR = _DATATRANSFORMIMPUTERPARAM_MISSINGVALUERATIOENTRY,
    __module__ = 'data_transform_param_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.DataTransformImputerParam.MissingValueRatioEntry)
    ))
  ,
  DESCRIPTOR = _DATATRANSFORMIMPUTERPARAM,
  __module__ = 'data_transform_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.DataTransformImputerParam)
  ))
_sym_db.RegisterMessage(DataTransformImputerParam)
_sym_db.RegisterMessage(DataTransformImputerParam.MissingReplaceValueEntry)
_sym_db.RegisterMessage(DataTransformImputerParam.MissingValueRatioEntry)

DataTransformOutlierParam = _reflection.GeneratedProtocolMessageType('DataTransformOutlierParam', (_message.Message,), dict(

  OutlierReplaceValueEntry = _reflection.GeneratedProtocolMessageType('OutlierReplaceValueEntry', (_message.Message,), dict(
    DESCRIPTOR = _DATATRANSFORMOUTLIERPARAM_OUTLIERREPLACEVALUEENTRY,
    __module__ = 'data_transform_param_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.DataTransformOutlierParam.OutlierReplaceValueEntry)
    ))
  ,

  OutlierValueRatioEntry = _reflection.GeneratedProtocolMessageType('OutlierValueRatioEntry', (_message.Message,), dict(
    DESCRIPTOR = _DATATRANSFORMOUTLIERPARAM_OUTLIERVALUERATIOENTRY,
    __module__ = 'data_transform_param_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.DataTransformOutlierParam.OutlierValueRatioEntry)
    ))
  ,
  DESCRIPTOR = _DATATRANSFORMOUTLIERPARAM,
  __module__ = 'data_transform_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.DataTransformOutlierParam)
  ))
_sym_db.RegisterMessage(DataTransformOutlierParam)
_sym_db.RegisterMessage(DataTransformOutlierParam.OutlierReplaceValueEntry)
_sym_db.RegisterMessage(DataTransformOutlierParam.OutlierValueRatioEntry)

DataTransformParam = _reflection.GeneratedProtocolMessageType('DataTransformParam', (_message.Message,), dict(
  DESCRIPTOR = _DATATRANSFORMPARAM,
  __module__ = 'data_transform_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.DataTransformParam)
  ))
_sym_db.RegisterMessage(DataTransformParam)


DESCRIPTOR._options = None
_DATATRANSFORMIMPUTERPARAM_MISSINGREPLACEVALUEENTRY._options = None
_DATATRANSFORMIMPUTERPARAM_MISSINGVALUERATIOENTRY._options = None
_DATATRANSFORMOUTLIERPARAM_OUTLIERREPLACEVALUEENTRY._options = None
_DATATRANSFORMOUTLIERPARAM_OUTLIERVALUERATIOENTRY._options = None
# @@protoc_insertion_point(module_scope)