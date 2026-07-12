import socket
from threading import Thread

SERVER_ADDRESS = ("127.0.0.1", 9090)
BUFFER = 4096

class Ricevitore(Thread):
    def __init__(self, s: socket.socket):
        super().__init__(daemon=True)
        self.s = s
        self.attivo = True

    def run(self):
        while self.attivo:
            dati = self.s.recv(BUFFER)
            print(f"\n<- {dati.decode()}\n-> ", end="", flush=True)

    def stop(self):
        self.attivo = False

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)
    print("Connesso al server.")

    nickname = input("Inserisci il tuo nickname: ")
    s.sendall(nickname.upper().encode())

    ricevitore = Ricevitore(s)
    ricevitore.start()

    while True:
        testo = input("-> ").strip()

        s.sendall(testo.encode())

        if testo.upper() == "EXIT":
            break

    ricevitore.stop()
    s.close()

if __name__ == "__main__":
    main()
