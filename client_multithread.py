import socket
from threading import Thread

SERVER_ADDRESS=("localhost",9000)
BUFFER_SIZE=4096

class Receiver(Thread):
    def __init__(self,s):
        super().__init__()
        self.s=s
        self.isRunning=True

    def run(self):
        while self.isRunning:
            data,address=self.s.recvfrom(BUFFER_SIZE)
            print(f"<-{data.decode()}")
            
    def stop(self):
        self.isRunning=False
    

def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    message=input("->")
    s.sendto(message.encode(),SERVER_ADDRESS)

    #qui faremo partire il thread di ricezione 
    t=Receiver(s)
    t.start()
    while message.upper()!="EXIT":
        message=input("->")
        s.sendto(message.encode(),SERVER_ADDRESS)
    t.stop()
    t.join()
if __name__=="__main__":
    main()

    #cose da fare :
    #creare ed eseguire il thread
    #far terminare il thread di ricezione 
    #fare .join del thread 
    #il tutto deve essere testato con un server udp 