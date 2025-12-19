# Simulare n partite a pari e dispari.
# Input utente:
# - n numero di partite
# - nome primo giocatore (quello che vince se esce pari)
# - nome secondo giocatore.
# 1) Per simulare le partite usiamo un dizionario:
# esempio nel caso n = 3
#d = {"Nome giocatore 1" : [3,2,5], "Nome giocatore 2" : [1,2,4]}
# Le singole giocate sono generate con random.randint()
# 2) Creare una lista che contiene i nomi dei vincitori per ogni partita e stamparla.
# Ipotesi: il primo giocatore vince se esce pari, il secondo se esce dispari.

import random
MAX=10
MIN=1


def simulaPartite(d):
    i = 0
    while i < n:
        d[g1].append(random.randint(MIN, MAX))
        d[g2].append(random.randint(MIN, MAX))
        i = i + 1
    
    return d

def gioco(d):
    for i in range(n):
        somma = d[g1][i] + d[g2][i]
        if somma % 2 == 0:
            vincitori.append(g1)
        else:
            vincitori.append(g2)
    
    return d

def main():
    n = int(input("Quante partite vuoi simulare? "))
    g1 = input("Nome del primo giocatore (vince se esce PARI): ")
    g2 = input("Nome del secondo giocatore (vince se esce DISPARI): ")

    d = {g1: [], g2: []}

    d = simulaPartite(d)

    print("\nDizionario delle giocate:")
    print(d)

    vincitori = []

    d = gioco(d)

    print("\nVincitori:\n")
    print(vincitori)

if __name__=="__main__":
    main()