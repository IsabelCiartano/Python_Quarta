
# PROCESSO SERVER: colui che eroga servizi, per esempio di comunicazione

import socket # built-in

def main():
    # 1) CREAZIONE DEL SOCKET
    # UN SOCKET E' UN ENDPOINT DI COMUNICAZIONE (ES: LA CORNETTA TELEFONICA)
    #       IPv4        UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # crea un socket

    # 2) SOLO SUL SERVER (DI SOLITO): LEGARE IL SOCKET A INDIRIZZO IP+PORTA
    # PORTA: numero a 16 bit che indirizza un processo nel computer
    # LE PORTE < 1024 SI CHIAMANO WELL_KNOWN (NON USARE)

    IP_PORTA = ("127.0.0.1", 12000)
    s.bind(IP_PORTA) # metodo per legare

    # ORA IL SOCKET PUO' ESSERE USATO PER COMUNICARE
    BUFFER_SIZE = 4096
    print("server in ascolto .....")
    # i dati sono stringhe binarie
    while True:
        dati, ip_porta_mittente = s.recvfrom(BUFFER_SIZE) # riceve dalla scheda di rete e mette dentro un buffer, E' BLOCCANTE!!!
        stringa = dati.decode() # trasforma i dati binari in stringa
        print(f"Ho ricevuto {stringa} da {ip_porta_mittente}")
        if stringa.upper()=="EXIT":
            break

    s.close() # chiude il socket

if __name__ == "__main__":
    main()