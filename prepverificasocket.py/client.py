import socket
BUFFER_SIZE=4096
def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    messaggio=input("->")
    messaggio_f=f"GET {messaggio}"
    DESTINATARIO=("127.0.0.1",5005)
    s.sendto(messaggio_f.encode(),DESTINATARIO)
    dati,ip_porta_mittente=s.recvfrom(BUFFER_SIZE)
    string=dati.decode()
    print(f"risposta del server {string}")
    s.close()

if __name__=="__main__":
    main()