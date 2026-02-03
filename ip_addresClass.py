
class IPaddres():
    def __init__(self,ip,subnetMask):
        #ip è una stringa 
        #subnet mask è in notazione cdr /XX
        self.ip = ip
        self.subnet = subnetMask

    def network_address(self):
        #restituisce indirizzo di rete tutti i bit a 0 
        pass
    def broadcastAddress(self):
        #restituisce indirizzo di broadcast
        pass
    def hostNumber(self):
        #restituisce in numero di host della rete 
        pass
def main():
    ip=IPaddres("192.168.168.1","/24")


if __name__ =="__main__":
    main()
