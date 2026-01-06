#Classifica giocatori
#Una lista contiene dizionari con chiavi nome, punteggio. Scrivere una funzione che
#stampi la classifica ordinata per punteggio decrescente, numerando le posizioni.
def stampa_classifica(giocatori):
    # Ordina i giocatori per punteggio decrescente
    classifica = sorted(giocatori, key=lambda g: g["punteggio"], reverse=True)
    
    # Stampa la classifica numerata
    for posizione, giocatore in enumerate(classifica, start=1):
        print(f"{posizione}. {giocatore['nome']} - {giocatore['punteggio']} punti")



giocatori = [
    {"nome": "Player1", "punteggio": 4500},
    {"nome": "Player2", "punteggio": 7200},
    {"nome": "Player3", "punteggio": 3100},
    {"nome": "Player4", "punteggio": 8900},
    {"nome": "Player5", "punteggio": 5600}
]

stampa_classifica(giocatori)
