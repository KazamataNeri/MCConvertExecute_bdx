from io import BytesIO
from BDXConverter.GeneralClass import GeneralClass
from utils.getByte import getByte
from struct import pack, unpack


class PlaceBlock(GeneralClass):
    def __init__(self) -> None:
        self.operationName: str = 'PlaceBlock'
        self.operationNumber: int = 7
        self.blockConstantStringID: int = 0
        self.blockData: int = 0

    def Marshal(self, writer: BytesIO) -> None:
        writer.write(pack('>H', self.blockConstantStringID) +
                     pack('>H', self.blockData))

    def UnMarshal(self, buffer: BytesIO) -> None:
        self.blockConstantStringID = unpack('>H', getByte(buffer, 2))[0]
        self.blockData = unpack('>H', getByte(buffer, 2))[0]

    def Loads(self, jsonDict: dict) -> None:
        self.blockConstantStringID = jsonDict['blockConstantStringID'] if 'blockConstantStringID' in jsonDict else 0
        self.blockData = jsonDict['blockData'] if 'blockData' in jsonDict else 0
