from threading import Thread 
import time 

class Cronometro(Thread):
    def __init__(self,nome,tempo):
        super().__init__()
        self.nome=nome
        self.tempo=tempo
    def run(self):
        time.sleep(self.tempo)
        print(f"{self.nome} è terminato")

def main():
    lista_nomi=["a","b","c"]
    lista_tempi=[3,1,10]
    lista_thread=[Cronometro(nome,tempo) for nome ,tempo in zip(lista_nomi,lista_tempi)]#usare la zip se si vuole ciclare su più liste pk si hanno piu campi 
    tempo_t=time.time()
    for t in lista_thread:
        t.start()

    for t in lista_thread:
        t.join()
    print(f"temp totale {time.time()-tempo_t:.2f}")#:.2f due cifre dopo la virgola utile per le print più leggibili 

    print("considerazioni : il tempo totale è come il thread più lungo pk essi girano in parallelo e non uno dopo l'altro ")
    

if __name__=="__main__":
    main()
