#definizione social network una rete in cui gli utenti si connettono

class Rete():
    def __init__(self):
        self.utenti=[]
    def iscrivi_utente(self,utente):#utente è un oggetto di tipo Utente
        self.utenti.append(utente)
    def __str__(self):
        return f"N° utenti:{len(self.utenti)}"
    def aggiungi_amicizia(self,utente1,utente2):
        #crea un amicizia tra utente 1 e utente 2 
        if(utente1 in self.utenti)and(utente2 in self.utenti):
            utente1.aggiungi_amico(utente2)
            utente2.aggiungi_amico(utente1)
        else:
            print("almeno uno dei due utenti non è iscritto")
    
class Utente():
    def __init__(self,nome):
        self.nome=nome
        self.amici=[] #lista di altri oggetti Utente
    def aggiungi_amico(self,utente):
        self.amici.append(utente)
    def __str__(self):
        #stampa utente e i sui contatti(=amici)
        lista_nomi=[amico.nome for amico in self.amici]# lista di stringhe 
        return f"nome utente:{self.nome} amici:{lista_nomi}"

def main():
    social_network=Rete()
    luca=Utente("luca")
    andrea=Utente("andrea")
    mario=Utente("mario")

    social_network.iscrivi_utente(luca)
    social_network.iscrivi_utente(andrea)
    social_network.iscrivi_utente(mario)

    print(social_network)

if __name__=="__main__":
    main()
    