import socket

BUFFER_SIZE=4096
IP_PORTA=("127.0.0.1",5007)

def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(IP_PORTA)

    print("server in ascolto ......")
    while True:
        dati,ip_porta_mittente=s.recvfrom(BUFFER_SIZE)
        print(f"Ricevuto {dati.decode()} da {ip_porta_mittente}")
        campi=dati.decode().split(" ")
        if len(campi)==3:
            if campi[0].lower()=="add":
                ris=int(campi[1]) + int(campi[2])
                msg=f"RISULTATO : {ris}"
            if campi[0].lower()=="sub":
                ris=int(campi[1]) - int(campi[2])
                msg=f"RISULTATO : {ris}"
            if campi[0].lower()=="mul":
                ris=int(campi[1]) * int(campi[2])
                msg=f"RISULTATO : {ris}"
            if campi[0].lower()=="div":
                if int(campi[2])!= 0:
                    ris=int(campi[1])/int(campi[2])
                    msg=f"RISULTATO : {ris}"
                else:
                    msg="ERR operazione non valida: divisione per zero"
            
            if campi[0].lower() != "add" and campi[0].lower() != "sub" and campi[0].lower() != "mul" and campi[0].lower() != "div":
                msg=f"ERR comando non esistente "
        else:
            msg="ERR campi errati"
        s.sendto(msg.encode(),ip_porta_mittente)
        if dati.decode().upper()=="EXIT":
            break
    s.close()


if __name__=="__main__":
    main()