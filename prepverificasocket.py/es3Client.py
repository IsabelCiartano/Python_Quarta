import socket 

BUFFER_SIZE=4096
DESTINATARIO=("127.0.0.1",5006)

def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    msg=input("->")
    s.sendto(msg.encode(),DESTINATARIO)
    dati,ip_porta_mittente=s.recvfrom(BUFFER_SIZE)
    print(f"-- {dati.decode()} da {ip_porta_mittente}")
    s.close()


if __name__=="__main__":
    main()