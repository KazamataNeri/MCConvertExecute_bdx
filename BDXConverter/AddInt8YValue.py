from io import BytesIO
from BDXConverter.GeneralClass import GeneralClass
from utils.getByte import getByte
from struct import unpack


class AddInt8YValue(GeneralClass):
    def __init__(self) -> None:
        self.operationName: str = 'AddInt8YValue'
        self.operationNumber: int = 29
        self.value: int = 0

    def Marshal(self, writer: BytesIO) -> None:
        writer.write(self.value.to_bytes(
            length=1, byteorder='big', signed=True))

    def UnMarshal(self, buffer: BytesIO) -> None:
        self.value = unpack('>b', getByte(buffer, 1))[0]

    def Loads(self, jsonDict: dict) -> None:
        self.value = jsonDict['value'] if 'value' in jsonDict else 0
