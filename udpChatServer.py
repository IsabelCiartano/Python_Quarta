import socket

IP_PORTA=("localhost",12345)
BUFFER_SIZE =4096
SEPARATORE="|"
LOG_LEVEL="DEBUG"

def log(stringa,tipo):
    if (tipo.upper=="DEBUG") and (LOG_LEVEL=="DEBUG"):
        print(f"[Debug]:{stringa}")
    

def main():

    rubrica={}
    #creazione di un socket ipv4 e UDP
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #lego socket a IP + porta 
    s.bind(IP_PORTA)
    while True:
        dati,ip_porta_mittente=s.recvfrom(BUFFER_SIZE)
        #il server deve capire se il messaggio ricevuto è di hello oppure di chat 
        #se è un messaggio di hello allora aggiorna rubrica 
        #se è un messaggio di chat allora lo inoltra 
        log(f"ricevuto {dati.decode()} da {ip_porta_mittente}","DEBUG")
        if dati[:5].decode().upper() == "HELLO":
            hello=dati.decode().split(",")
            nick=hello[1]
            rubrica[nick]=ip_porta_mittente
            print(rubrica)
            continue
        else:
            campi=dati.decode().split(SEPARATORE)
            dest,mess=campi
            if mess.decode().upper=="EXIT":
                break

if __name__ =="__main__":
    main()