import socket
from threading import Thread

MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096
rubrica = {} # chiave = NICKNAME  valore = CONNESSIONE

class GestoreClient(Thread):
    def __init__(self, connessione, indirizzo):
        super().__init__()
        self.connessione = connessione
        self.indirizzo = indirizzo
        self.attivo = True
    
    def run(self):
        global rubrica
        dati = self.connessione.recv(BUFFER_SIZE)
        nickname = dati.decode().upper()
        if nickname not in rubrica:
            rubrica[nickname] = self.connessione
        print(rubrica)
        while self.attivo:
            dati = self.connessione.recv(BUFFER_SIZE)
            print(f"Ho ricevuto: {dati.decode()}")
            nick_destinatario, messaggio = dati.decode().split("|")
            connessione_destinatario = rubrica[nick_destinatario.upper()]
            connessione_destinatario.sendall(messaggio.encode())
            if dati.decode().upper() == "EXIT":
                self.attivo = False

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket ipv4 TCP
    s.bind(MY_ADDRESS)
    print("Server attivo...")

    s.listen() # alloca risorse per le connessioni TCP
    print("Server in attesa di connesioni")
    lista_client = []

    while True:
        connessione, indirizzo = s.accept()
        thread = GestoreClient(connessione, indirizzo)
        thread.start()
        lista_client.append(thread)
        print(f"Un client si è connesso, si tratta di {indirizzo}")

    

    s.close()

    # RENDERE IL CODICE PIù ROBUSTO, 
    # IMPLEMENTARE UN MESSAGGIO "rubrica" CHE, QUANDO RICEVUTO DAL CLIENT, RESTITUISCE L'ELENCO
    # DEI NICKNAME ISCRITTI.


if __name__ == "__main__":
    main()