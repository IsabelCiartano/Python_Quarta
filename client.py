# PROCESSO CLIENT: colui che sfrutta servizi, per esempio di comunicazione, del server

import socket # built-in

def main():
    # 1) CREAZIONE DEL SOCKET
    # UN SOCKET E' UN ENDPOINT DI COMUNICAZIONE (ES: LA CORNETTA TELEFONICA)
    #       IPv4        UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # crea un socket

    messaggio = input("->")
    DESTINATARIO = ("127.0.0.1", 13000) # è un processo

    s.sendto(messaggio.encode(), DESTINATARIO) 

    s.close() # chiude il socket

if __name__ == "__main__":
    main()