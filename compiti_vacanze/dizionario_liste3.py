#4. Squadre e giocatori
#Un dizionario associa nomi di squadre a liste di giocatori. Scrivere funzioni per: (a)
#trovare la squadra con più giocatori, (b) verificare se un giocatore è in una squadra, (c)
#trasferire un giocatore da una squadra all’altra.

def a(squadre):
    massimo=0
   
    for squadra in squadre:
        if len(squadre[squadra])>massimo:
            massimo=len(squadre[squadra])
            squadra_max=squadra
    return squadra_max

def b(Squadre,giocatore):
    for squadra in squadre:
        for g in squadre[squadra]:
            if g ==giocatore:
                return squadra
    return None

def c(Squadre,giocatore,s2):
    for squadra in squadre:
        for g in squadre[squadra]:
            if g ==giocatore:
                squadre[s2].append(g)
                squadre[squadra].remove(g)




squadre = {
"Juventus": ["Vlahovic", "Chiesa", "Locatelli", "Bremer"],
"Inter": ["Lautaro", "Thuram", "Barella", "Bastoni", "Calhanoglu"],
"Milan": ["Leao", "Theo", "Reijnders"]
}

print(a(squadre))
print(b(squadre,"Chiesa"))
c(squadre,"Leao","Inter")
print(squadre)