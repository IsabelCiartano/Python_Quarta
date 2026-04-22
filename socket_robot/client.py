#inviare al server i comandi 
#BONUS : implementare il client usando la libreria pyinput 

import socket
BUFFER_SIZE=4096
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

    messaggio = input("->")
    DESTINATARIO = ("127.0.0.1", 9000) 

    s.sendto(messaggio.encode(), DESTINATARIO) 
    while True:
        dati, ip_porta_mittente = s.recvfrom(BUFFER_SIZE) # riceve dalla scheda di rete e mette dentro un buffer, E' BLOCCANTE!!!
        stringa = dati.decode() # trasforma i dati binari in stringa
        print(f"Ho ricevuto {stringa} da {ip_porta_mittente}")
        messaggio2=input("->")
        s.sendto(messaggio2.encode(), DESTINATARIO) 
        if messaggio2.upper()=="EXIT":
            break
    s.close() 

if __name__ == "__main__":
    main()