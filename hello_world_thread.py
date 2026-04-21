from threading import Thread #importo la classe thread che sta in una librearia built in di python 
import time
#per creare un thread dobbiamo creare una classse figlia di Thread(EREDITARIETA')

class mioThread(Thread):#per ereditare al posto di self inserisco thread cioè la classe è figlia di thread 
    def __init__(self,nome):
        super().__init__() #costruttore della classe genitore
        self.nome=nome
        print("OK")
    def run(self):
        #contiene il codice de thread
        for i in range(10):
            print(f"print n°{i} : io sono {self.nome}")
            time.sleep(0.5)#pausa tra una print e l'altra 

def main():
    t1=mioThread("t1")
    t2=mioThread("t2")
    t1.start()#metodo del genitore che va a chiamare run ed esegue cosi il thread 
    t2.start()
    t1.join()#operazione che riposta il filo del thread su quello principale
    t2.join()#è bloccante aspetta che il thread finisca
if __name__=="__main__":
    main()