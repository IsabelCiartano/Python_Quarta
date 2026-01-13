#Classifica giocatori
#Una lista contiene dizionari con chiavi nome, punteggio. Scrivere una funzione che
#stampi la classifica ordinata per punteggio decrescente, numerando le posizioni.


def stampa_classifica(giocatori):
    # Ordina i giocatori per punteggio decrescente
        # Copia della lista per non modificare l'originale
    classifica = giocatori[:]

    n = len(classifica)
    for i in range(n):
        #max_ è l'indice del giocatore con il punteggio più alto
        max_ = i#punteggio massimo inizializzato come il primo inizialmente 
        for j in range(i + 1, n):#i indica la posizione da riempire
            if classifica[j]["punteggio"] > classifica[max_]["punteggio"]:
                max_ = j#aggiorna il massimo se si è trovato un punteggio maggiore 
        # Scambio
        classifica[i], classifica[max_] = classifica[max_], classifica[i]

    
    # Stampa la classifica numerata
    for posizione, giocatore in enumerate(classifica, start=1):
        print(f"{posizione}. {giocatore['nome']} - {giocatore['punteggio']} punti")


def main():
    giocatori = [
    {"nome": "Player1", "punteggio": 4500},
    {"nome": "Player2", "punteggio": 7200},
    {"nome": "Player3", "punteggio": 3100},
    {"nome": "Player4", "punteggio": 8900},
    {"nome": "Player5", "punteggio": 5600}
    ]

    stampa_classifica(giocatori)

if __name__=="__main__":
    main()


