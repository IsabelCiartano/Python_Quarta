#definizione social network una rete in cui gli utenti si connettono

class Rete():
    pass
class Utente():
    def __init__(self,nome):
        self.nome=nome
        self.amici=[] #lista di altri oggetti Utente
    def aggiungi_amico(self,utente):
        pass
    def __str__(self):
        #stampa utente e i sui contatti 