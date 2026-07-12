import socket
from threading import Thread

SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFER_SIZE = 4096

class Ricevitore(Thread):
    def __init__(self, s):
        super().__init__()
        self.s = s
        self.attivo = True

    def run(self):
        while self.attivo:
            dati_ricezione = self.s.recv(BUFFER_SIZE)
            print(f"Ricevuto <-- {dati_ricezione.decode()}")

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket ipv4 TCP
    s.connect(SERVER_ADDRESS)
    print("Mi sono connesso.")
    nickname = input("Inserisci il tuo nickname -> ").upper()
    s.sendall(nickname.encode())
    thread_ricevitore = Ricevitore(s)
    thread_ricevitore.start()

    while True:
        destinatario = input("A chi vuoi inviare un messagio? 127.0.0.1:56223 -> ")
        messaggio = input("--> ")
        dati_invio = f"{destinatario}|{messaggio}"
        
        s.sendall(dati_invio.encode())

    s.close()

    # USARE L'IA PER RISOLVERE IN MANIERA SEMPLICE IL PROBLEMA DELLE PRINT FATTE MALE IN RICEZIONE.

if __name__ == "__main__":
    main()