from threading import Thread

class SommaParziale(Thread):# ricordsre self 
    def __init__(self,dati):
        super().__init__()
        self.dati=dati
        self.risultato=0
    def run(self):
        for n in self.dati :
            self.risultato += n
        #self.risultato=sum(self.lista)
    
def main():
    n_thread=4
    somma=0
    lista_dati=list(range(1,101))
    l=len(lista_dati)#lunghezza dei dati 
    lista_liste=[]

    #for k in range(n_thread):
        #indice1=int(l*k/n_thread)#0 1
        #indice2=int(l*(k+1)/n_thread)#l/4 l/2
        #lista_liste.append(lista_dati[indice1:indice2])

    for i in range(0,l,l//4): # divisione intera //
        sottolista=lista_dati[i:i+l//4]
        lista_liste.append(sottolista)

    lista_thread=[SommaParziale(lista) for lista in lista_liste ]
    for t in lista_thread:
        t.start()
    for t in lista_thread:
        t.join()
        somma+=t.risultato
    if somma==sum(lista_dati):
        print("somma uguale")
    else:
        print("somma diversa")

if __name__=="__main__":
    main()

