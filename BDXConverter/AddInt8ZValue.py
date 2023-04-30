from io import BytesIO
from BDXConverter.GeneralClass import GeneralClass
from Utils.getByte import getByte
from struct import unpack


class AddInt8ZValue(GeneralClass):
    def __init__(self) -> None:
        self.operationName: str = 'AddInt8ZValue'
        self.operationNumber: int = 30
        self.value: int = 0

    def Marshal(self, writer: BytesIO) -> None:
        writer.write(self.value.to_bytes(
            length=1, byteorder='big', signed=True))

    def UnMarshal(self, buffer: BytesIO) -> None:
        self.value = unpack('>b', getByte(buffer, 1))[0]

    def Loads(self, jsonDict: dict) -> None:
        self.value = jsonDict['value'] if 'value' in jsonDict else 0