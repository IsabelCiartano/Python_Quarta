# modularità :suddiviso in moduli (funzioni)

COSTANTE=3.14#costante è una variabile globale !!!!
#ATTENZIONE : costante è accessibile da tutte le funzioni ma soltanto in lettura 

def prima_lettera_maiuscola(stringa):#def +nome+parametri
    """
    la funzione restituisce  stringa con la lettera iniziale maiuscola 
    """
    #documentazione della funzione gestita da python nel suo help 
    #stringa è una variabile locale alla funzione esiste solo nella funzione 
    s=stringa[0].upper()+stringa[1:].lower()
    return s

def media(lista):
    """
    La funzione restituisce la media dei valori presenti in lista e il numero di elementi 
    """
    somma=0.
    n=len(lista)
    for v in lista:
        somma=somma+v #v èil valore non l'indice!!!
    return somma/n,n


def main():
    print(help(prima_lettera_maiuscola))
    nome=input("inserire un nome->")
    print(prima_lettera_maiuscola(nome))

    voti=[4,6,7,10]
    m,n=media(voti)
    print(m)
    print(n)
    if m >6:
        print("(⓿_⓿)")


if __name__ =="__main__":
    main()
