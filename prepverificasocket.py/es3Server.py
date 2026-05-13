import socket

BUFFER_SIZE=4096
IP_PORTA=("127.0.0.1",5006)

def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    s.bind(IP_PORTA)
    print("server in ascolto")
    n=0

    while True:
        dati,ip_porta_mittente=s.recvfrom(BUFFER_SIZE)
        n+=1
        print(f" ricevuto: {dati.decode()} da {ip_porta_mittente} richersta n {n}")
        msg=f"{n} {dati.decode()}"
        s.sendto(msg.encode(),ip_porta_mittente)
        if dati.decode().upper()=="EXIT":
            break
    s.close()

if __name__=="__main__":
    main()