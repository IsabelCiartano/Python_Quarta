
import socket # built-in

BUFFER_SIZE = 4096
DESTINATARIO = ("192.168.1.108", 13000)
def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # crea un socket
    messaggio = input("->")

    s.sendto(messaggio.encode(), DESTINATARIO) 

    dati, ip_porta_mittente = s.recvfrom(BUFFER_SIZE) # riceve dalla scheda di rete e mette dentro un buffer, E' BLOCCANTE!!!
    stringa = dati.decode() # trasforma i dati binari in stringa
    print(f"Ho ricevuto {stringa} da {ip_porta_mittente}")
    
    s.close()

if __name__ == "__main__":
    main()