
import socket
from threading import Thread

MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER = 4096

rubrica = {}

class GestoreClient(Thread):
    def __init__(self, connessione, indirizzo):
        super().__init__()
        self.connessione = connessione
        self.indirizzo = indirizzo
        self.nickname = ""
        self.attivo = True

    def run(self):
        dati = self.connessione.recv(BUFFER)
        self.nickname = dati.decode().upper()

        if self.nickname in rubrica:
            self.connessione.sendall("ERRORE: nickname già in uso.".encode())
            self.connessione.close()
            return

        rubrica[self.nickname] = self.connessione
        print(f"{self.nickname} connesso da {self.indirizzo}")

        while self.attivo:
            dati = self.connessione.recv(BUFFER)
            messaggio2 = dati.decode().strip()

            if messaggio2.upper() == "RUBRICA":
                lista = ", ".join(rubrica)
                self.connessione.sendall(f"Utenti online: {lista}".encode())

            if messaggio2.upper() == "EXIT":
                break

            if "|" not in messaggio2:
                self.connessione.sendall("ERRORE: formato non valido. Usa DESTINATARIO|messaggio".encode())

            nick_dest, corpo = messaggio2.split("|")
            nick_dest = nick_dest.upper()

            if nick_dest not in rubrica:
                self.connessione.sendall(f"ERRORE: '{nick_dest}' non trovato in rubrica.".encode())

            rubrica[nick_dest].sendall(f"[{self.nickname}] {corpo}".encode())

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(MY_ADDRESS)
    s.listen()

    print(f"Server in ascolto su {MY_ADDRESS[0]}:{MY_ADDRESS[1]}")

    lista_client = []

    while True:
        connessione, indirizzo = s.accept()
        thread = GestoreClient(connessione, indirizzo)
        thread.start()
        lista_client.append(thread)
        print(f"Nuova connessione da {indirizzo}")

if __name__ == "__main__":
    main()

# meccanismo per interrompere i thread e fare la join

# compito: rendere più robusto il codice da lato server
#          implementare un messaggio "rubrica" che, quando ricevuto dal client, restituisce l'elenco SOLO dei nickname iscritti
#          usare l'IA per risolvere le print fatte male
