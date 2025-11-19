import uuid

def getMac():
    mac=uuid.getnode()
    macAddress=':'.join(('%012X'%mac)[i:i+2]for i in range (0,12,2))
    return macAddress

