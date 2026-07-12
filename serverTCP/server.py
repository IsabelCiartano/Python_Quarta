import socket
from threading import Thread,Lock

# 1) TCP è un protocollo aaffidabile = garanzia che i messaggi arrivino a destinazione
# 2) TCP ha il concetto di connessione: un client e un server che comunicano sono legati da una connsessione (= canale di comunicazione)

MY_ADDRESS = ("127.0.0.1", 9090)
BUFFER = 4096
lock_print = Lock()

rubrica={}#chiave =nickname valore =connessione

class GestoreClient(Thread):
    def __init__(self, connessione, indirizzo):
        super().__init__()
        self.connessione = connessione
        self.indirizzo = indirizzo
        self.attivo = True
    
    def run(self):
        global rubrica
        dati= self.connessione.recv(BUFFER)
        if dati.decode().upper()=="RUBRICA":
            with lock_print:
                print(rubrica)
        nickname=dati.decode().upper()
        if nickname not in rubrica:
            rubrica[nickname]=self.connessione
        with lock_print:
            print(rubrica)

        while self.attivo:
            dati = self.connessione.recv(BUFFER) # metodo di connessione, NON del socket
            with lock_print:
                print(f"Ho ricevuto {dati.decode()}")
            nick_destinatario,messaggio=dati.decode().split("|")

            connessione_destinatario=rubrica[nick_destinatario.upper()] 
            connessione_destinatario.sendall(messaggio.encode())

            if messaggio.decode().upper() == "EXIT":
                self.attivo = False
        
        self.connessione.close()
        print(f"Client {self.indirizzo} disconnesso")

    def stop(self):
        self.attivo = False
        self.connessione.close()

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket ipv4, TCP
    s.bind(MY_ADDRESS)
    print("Server attivo...")

    s.listen() # alloca risorse per le connessioni TCP
    print("Server in attesa di connessioni")
    
    lista_client = []
    attivo = True

    while attivo:
        connessione, indirizzo = s.accept() # BLOCCA il server in attesa di connessione
                                            # quando si sblocca restituisce una connessione e un indirizzo
                                            # l'oogetto connessione è fondamentale per comunicare col client
      
        thread = GestoreClient(connessione, indirizzo)
        thread.start()
        lista_client.append(thread)
        with lock_print:
            print(f"Un client si è connesso, si tratta di {indirizzo}")

        if not attivo:
            break
    
    s.close()

if __name__ == "__main__":
    main()

# meccanismo per interrompere i thread e fare la join
#rendere client e server il più possibile robusti 
#uso l'ai per risolvere problema delle print in modo semplice 
#implementare un messaggio rubrica che quando ricevuto dal client restituisce l'elenco dei nickname iscritti 