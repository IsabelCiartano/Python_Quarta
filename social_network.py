#definizione social network una rete in cui gli utenti si connettono

class Rete():
    def __init__(self):
        self.utenti=[]
    def iscrivi_utente(self,utente):#utente è un oggetto di tipo Utente
        self.utenti.append(utente)
    
class Utente():
    def __init__(self,nome):
        self.nome=nome
        self.amici=[] #lista di altri oggetti Utente
    def aggiungi_amico(self,utente):
        pass
    def __str__(self):
        #stampa utente e i sui contatti(=amici)
        pass

def main():
    social_network=Rete()
    luca=Utente("luca")
    andrea=Utente("andrea")
    mario=Utente("mario")

    social_network.iscrivi_utente(luca)
    social_network.iscrivi_utente(andrea)
    social_network.iscrivi_utente(mario)

if __name__=="__main__":
    main()
    