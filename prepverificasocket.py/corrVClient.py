import socket 
IP_PORTA=("127.0.0.1",5005)
BUFFER_SIZE=4096

def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    comando=input("->")
    if comando.upper()=="VOTA":
        citta=input("citta: ")
        s.sendto(f"VOTA {citta}".encode(),IP_PORTA)
    else:
        s.sendto(f"{comando}".encode(),IP_PORTA)
    dati,_=s.recvfrom(BUFFER_SIZE)
    print(dati.decode())
    s.close()
if __name__=="__main__":
    main()
