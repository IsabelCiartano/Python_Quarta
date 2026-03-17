import socket

IP_PORTA=("localhost",12345)
BUFFER_SIZE 4096
SEPARATORE="|"

def main():

    rubrica={"luca":("192.168.100.2",54617)
    }
    #creazione di un socket ipv4 e UDP
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #lego socket a IP + porta 
    s.bind(IP_PORTA)
    while True:
        dati,ip_porta_mittente=s.recvfrom(BUFFER_SIZE)
        #il server deve capire se il messaggio ricevuto è di hello oppure di chat 
        #se è un messaggio di hello allora aggiorna rubrica 
        #se è un messaggio di chat allora lo inoltra 
        print(f"ricevuto {dati.decode()} da {ip_porta_mittente}")
        campi=dati.decode().split(SEPARATORE)
        dest,mess=campi
        if dati.decode().upper=="EXIT":
            break

if __name__ =="__main__":
    main()