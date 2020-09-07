from ubxlib.cid import UbxCID
from ubxlib.frame import UbxFrame
from ubxlib.types import U1, X4


class UbxMgaAckData0_(UbxFrame):
    CID = UbxCID(0x13, 0x60)
    NAME = 'UBX-MGA-ACK-DATA0'


class UbxMgaAckData0(UbxMgaAckData0_):
    def __init__(self):
        super().__init__()

        self.f.add(U1('type'))
        self.f.add(U1('version'))
        self.f.add(U1('infoCode'))
        self.f.add(U1('msgId'))
        self.f.add(X4('msgPayloadStart'))