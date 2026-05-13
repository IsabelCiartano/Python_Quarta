#Due coniugi, Anna e Bruno, condividono lo stesso conto corrente con saldo iniziale di 1000 euro. Durante la stessa giornata effettuano ciascuno una serie di operazioni indipendenti: versamenti, prelievi, e bonifici verso amici.
# La banca registra ogni operazione modificando il saldo del conto.
#Modella questa situazione con due thread (Anna e Bruno) che operano contemporaneamente su una variabile condivisa saldo. Ogni thread esegue 50 operazioni casuali scelte tra:
 #versamento di un importo casuale tra 10 e 100 euro;
 #prelievo di un importo casuale tra 10 e 100 euro (solo se il saldo è sufficiente);
 #bonifico di un importo casuale tra 10 e 50 euro (solo se il saldo è sufficiente).
#Ogni operazione deve:leggere il saldo corrente;attendere un breve istante (time.sleep(0.001)) per simulare il tempo di elaborazione della banca;calcolare il nuovo saldo;scrivere il nuovo saldo.
 #Scrivi una prima versione senza alcuna sincronizzazione. 
#Tieni traccia, in una variabile separata totale_movimenti, della somma di tutte le operazioni effettivamente eseguite (positiva per i versamenti, negativa per prelievi e bonifici). Al termine, verifica che

#saldo_finale == saldo_iniziale + totale_movimenti

#Esegui il programma più volte. Dove sono finiti i soldi mancanti? Sono stati creati dal nulla quelli in eccesso? 

#Aggiungi un threading.Lock per proteggere la sezione critica. Verifica che ora l'invariante contabile è sempre rispettata, su qualunque numero di esecuzioni

from threading import Thread,Lock
import random 
import time

CONTO =1000
tot_movimenti=0
lucchetto=Lock()
saldo_iniziale=1000
def versamento():
    global CONTO,tot_movimenti
    importo=random.uniform(10,100)
    print(f"vers:{importo:.2f}")
    CONTO+=importo
    tot_movimenti+=importo

def prelievo():
    global CONTO,tot_movimenti
    importo=random.uniform(10,100)
    print(f"pre:{importo:.2f}")
    if CONTO >= importo:
        CONTO=CONTO-importo
        tot_movimenti-=importo
def bonifico():
    global CONTO,tot_movimenti
    importo=random.uniform(10,100)
    print(f"bon:{importo:.2f}")
    if CONTO >= importo:
        CONTO=CONTO-importo
        tot_movimenti-=importo

class Persona(Thread):
    def __init__(self, nome):
        super().__init__()
        self.nome=nome
    def run(self):
        for _ in range(50):
            with lucchetto:
                cmd=random.randint(1,3)
                if cmd==1:
                    versamento()
                    time.sleep(0.001)
                if cmd==2:
                    prelievo()
                    time.sleep(0.001)
                if cmd==3:
                    bonifico()
                    time.sleep(0.001)
                print(f"conto:{CONTO:.2f}") 



def main():

    lista_nomi = ["ANNA", "BRUNO"]

    lista_persone = [Persona(nome) for nome in lista_nomi]

    for t in lista_persone:
        t.start()

    for t in lista_persone:
        t.join()

    print(f"\nTotale movimenti:{tot_movimenti:.2f}")

    finale = saldo_iniziale + tot_movimenti

    print(f"Saldo finale reale: {CONTO:.2f}")
    print(f"Saldo finale atteso: {finale:.2f}")

    if round(CONTO, 2) == round(finale, 2):
        print("ok")
    else:
        print("non ok")


if __name__=="__main__":
    main()
