import socket

BUFFER_SIZE =4096
DESTINATARIO=("127.0.0.1",5007)

def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    op=input("->")
    s.sendto(op.encode(),DESTINATARIO)
    dati,ip_porta_mittente=s.recvfrom(BUFFER_SIZE)
    print(f"ricevuto da {ip_porta_mittente} -> {dati.decode()}")
    s.close()


if __name__=="__main__":
    main()