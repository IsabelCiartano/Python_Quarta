from threading import Thread #importo la classe thread che sta in una librearia built in di python 
import time
#per creare un thread dobbiamo creare una classse figlia di Thread(EREDITARIETA')

GLOBALE = 42
class mioThread(Thread):#per ereditare al posto di self inserisco thread cioè la classe è figlia di thread 
    def __init__(self,nome):
        super().__init__() #costruttore della classe genitore
        self.nome=nome
        print("OK")
    def run(self):
        #contiene il codice de thread
        for i in range(10):
            print(f"print n°{i} : io sono {self.nome} e la variabile globale è {GLOBALE}")
            time.sleep(0.5)#pausa tra una print e l'altra 

def main():
    n_thread= 5
    lista_nomi=["t"+str(n) for n in range(1,n_thread+1)] #str()serve per convertire in stringa 
    lista_thread[mioThread(nome) for nome in lista_nomi]
    for thread in lista_thread:
        thread.start()
    for thread in lista_thread:
        thread.join()

if __name__=="__main__":
    main()