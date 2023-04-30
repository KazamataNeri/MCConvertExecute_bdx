from io import BytesIO
from BDXConverter.GeneralClass import GeneralClass
from Utils.getString import getByte, getString
from struct import pack, unpack


class SetCommandBlockData(GeneralClass):
    def __init__(self) -> None:
        self.operationName: str = 'SetCommandBlockData'
        self.operationNumber: int = 26
        self.mode: int = 0
        self.command: str = ''
        self.customName: str = ''
        self.lastOutput: str = ''
        self.tickdelay: int = 0
        self.executeOnFirstTick: bool = True
        self.trackOutput: bool = True
        self.conditional: bool = False
        self.needsRedstone: bool = False

    def Marshal(self, writer: BytesIO) -> None:
        writer.write(pack('>I', self.mode) + self.command.encode(encoding='utf-8') + b'\x00' + self.customName.encode(encoding='utf-8') + b'\x00' + self.lastOutput.encode(encoding='utf-8') + b'\x00' + pack('>i', self.tickdelay) + self.executeOnFirstTick.to_bytes(
            length=1, byteorder='big', signed=False) + self.trackOutput.to_bytes(length=1, byteorder='big', signed=False) + self.conditional.to_bytes(length=1, byteorder='big', signed=False) + self.needsRedstone.to_bytes(length=1, byteorder='big', signed=False))

    def UnMarshal(self, buffer: BytesIO) -> None:
        self.mode = unpack('>I', getByte(buffer, 4))[0]
        self.command = getString(buffer)
        self.customName = getString(buffer)
        self.lastOutput = getString(buffer)
        self.tickdelay = unpack('>i', getByte(buffer, 4))[0]
        self.executeOnFirstTick = bool(getByte(buffer, 1)[0])
        self.trackOutput = bool(getByte(buffer, 1)[0])
        self.conditional = bool(getByte(buffer, 1)[0])
        self.needsRedstone = bool(getByte(buffer, 1)[0])

    def Loads(self, jsonDict: dict) -> None:
        self.mode = jsonDict['mode'] if 'mode' in jsonDict else 0
        self.command = jsonDict['command'] if 'command' in jsonDict else ''
        self.customName = jsonDict['customName'] if 'customName' in jsonDict else ''
        self.lastOutput = jsonDict['lastOutput'] if 'lastOutput' in jsonDict else ''
        self.tickdelay = jsonDict['tickdelay'] if 'tickdelay' in jsonDict else 0
        self.executeOnFirstTick = jsonDict['executeOnFirstTick'] if 'executeOnFirstTick' in jsonDict else True
        self.trackOutput = jsonDict['trackOutput'] if 'trackOutput' in jsonDict else True
        self.conditional = jsonDict['conditional'] if 'conditional' in jsonDict else False
        self.needsRedstone = jsonDict['needsRedstone'] if 'needsRedstone' in jsonDict else False
