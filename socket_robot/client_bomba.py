#inviare al server i comandi randomici che bombardino il server 

import socket
import random
BUFFER_SIZE=4096

import random

def random_msg():
    valore = random.randint(-180, 180)
    cmd = ["forward", "backward", "left", "right"]
    st = random.choice(cmd)
    st = st + "," + str(valore)
    return st

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    DESTINATARIO = ("127.0.0.1", 9000) 

    while True:
        messaggio=random_msg()
        s.sendto(messaggio.encode(), DESTINATARIO) 
        dati, ip_porta_mittente = s.recvfrom(BUFFER_SIZE) # riceve dalla scheda di rete e mette dentro un buffer, E' BLOCCANTE!!!
        stringa = dati.decode() # trasforma i dati binari in stringa
        #print(f"Ho ricevuto {stringa} da {ip_porta_mittente}")
        
        
        if messaggio.upper()=="EXIT":
            break
    s.close() 

if __name__ == "__main__":
    main()