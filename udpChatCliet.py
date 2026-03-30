
import socket # built-in
SERVER_CHAT=("127.0.0.1", 12345)#per tutti i client 
NICKNAME="johndoe"#ogni client ha il suo 
SEPARATORE="|"


def main():
    #implementare un messaggio di hello in cui il client si presenta al server 
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # crea un socket
    HELLO=f"Hello,{NICKNAME}"
    s.sendto(f"{HELLO}".encode(),SERVER_CHAT)
    messaggio = input("DESTINATARIO | MESSAGGIO ->")
    campi=messaggio.split(SEPARATORE)
    if len(campi)==2:
        dest,mess=campi
        s.sendto(f"{dest}{SEPARATORE}{mess}".encode(),SERVER_CHAT)
    else:
        print("errore")
    s.close() # chiude il socket

if __name__ == "__main__":
    main()