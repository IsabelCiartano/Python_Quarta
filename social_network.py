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
    def amici_in_comune(self,utente1,utente2):
        #restituisce la liste degli amici in comune tra la lista degli amici di utente 1 e utente 2
        amici_comuni=[]
        for amico1 in utente1.amici:
            for amico2 in utente2.amici:
                if(amico2==amico1):
                    amici_comuni.append(amico2)
        return(amici_comuni)
    def suggerisci_amici(self,utente):
        pass

class Utente():
    def __init__(self,nome):
        self.nome=nome
        self.amici=[] #lista di altri oggetti Utente
    def aggiungi_amico(self,utente):
        self.amici.append(utente)
    def __str__(self):
        #stampa utente e i sui contatti(=amici)
        lista_nomi=[amico.nome for amico in self.amici]# lista di stringhe 
        #list comprehension 
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
    social_network.aggiungi_amicizia(mario,luca)
    social_network.aggiungi_amicizia(mario,andrea)
    print(mario)
    print(luca)
    comune=social_network.amici_in_comune(luca,andrea)
    lista=[amico.nome for amico in comune]
    print(lista)

if __name__=="__main__":
    main()
    