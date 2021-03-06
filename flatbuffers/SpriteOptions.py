# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers

class SpriteOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsSpriteOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SpriteOptions()
        x.Init(buf, n + offset)
        return x

    # SpriteOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SpriteOptions
    def NodeOptions(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .WidgetOptions import WidgetOptions
            obj = WidgetOptions()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # SpriteOptions
    def FileNameData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .ResourceData import ResourceData
            obj = ResourceData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # SpriteOptions
    def BlendFunc(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = o + self._tab.Pos
            from .BlendFunc import BlendFunc
            obj = BlendFunc()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def SpriteOptionsStart(builder): builder.StartObject(3)
def SpriteOptionsAddNodeOptions(builder, nodeOptions): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(nodeOptions), 0)
def SpriteOptionsAddFileNameData(builder, fileNameData): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(fileNameData), 0)
def SpriteOptionsAddBlendFunc(builder, blendFunc): builder.PrependStructSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(blendFunc), 0)
def SpriteOptionsEnd(builder): return builder.EndObject()
