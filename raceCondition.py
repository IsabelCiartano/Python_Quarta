#Dichiara una variabile globale contatore = 0. Scrivi un thread che esegua 100 volte il seguente
#blocco:

#Crea 10 thread e attendi la loro terminazione con join(). Al termine stampa contatore. Esegui il
#programma più volte: ottieni sempre 1000? Spiega il risultato alla luce di quanto visto sulla race
#condition, identificando le tre fasi (lettura, calcolo, scrittura) della sezione critica.
#Obiettivo: osservare concretamente una race condition e riconoscere la struttura read–modify–
#write di una sezione critica non protetta.

#per fare una varibile globale all'interno di run devo scrivere global name= 0

from threading import Thread
import time 

contatore=0# inizializzare una varibile fuori da classi / funzioni = variabile Globale
class myThread(Thread):
    def __init__(self,nome):
        super().__init__()
        self.nome=nome

    def incrementa(self,c):#funzione della classe , esempio di funzione interna a una classe 
    #nel metodo ce self come paramentro mentre nella funzione no 
            temp = c
            time.sleep(0.0001)
            c = temp + 1
            return c

    def run(self):
        global contatore
        for i in range(100):
            #sezione critica
            contatore=self.incrementa(contatore)
            #fine sezione critica
        print(f"{self.nome} :{contatore}")
   

def main():
    n_thread=10
    lista_nomi=["t"+str(n) for n in range (n_thread)]
    threads=[myThread(nome) for nome in lista_nomi]
    for t in threads: #per lanciarli al contrario threads[::-1]
        t.start()
    for t in threads:
        t.join()

    print(f"risultato finale{contatore}")
if __name__=="__main__":
    main()

# soluzione per eliminare la race condition fare in modo che il thread accedano uno per volta alla risorsa condivisa 