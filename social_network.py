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
            #se uno dei due utenti non esiste creo l'utente mancante o entrambi  
    def amici_in_comune(self,utente1,utente2):
        #restituisce la liste degli amici in comune tra la lista degli amici di utente 1 e utente 2
        amici_comuni=[]
        for amico1 in utente1.amici:
            for amico2 in utente2.amici:
                if(amico2==amico1):
                    amici_comuni.append(amico2)
        return(amici_comuni)
    def suggerisci_amici(self,utente):
        suggeriti=[]
        for amico in utente.amici:
            for a in amico.amici:
                if a not in utente.amici and a!=utente:
                    suggeriti.append(a)
        return suggeriti

   def suggerisci_amici_nuovo(self, utente):
    listaSuggeriti = []

    # Raccolgo amici degli amici
    for amico in utente.amici:
        for amico2 in amico.amici:
            if amico2 not in utente.amici and amico2 != utente:
                listaSuggeriti.append(amico2)

    # Conteggio delle occorrenze
    conteggio = {}
    for persona in listaSuggeriti:
        if persona in conteggio:
            conteggio[persona] += 1
        else:
            conteggio[persona] = 1

    # Tengo solo quelli con più di una occorrenza
    suggeriti_finali = []
    for persona, numero in conteggio.items():
        if numero > 1:
            suggeriti_finali.append(persona)

    return suggeriti_finali

    def carica_da_file(self, file_nome):
        file = open(file_nome, "r")
        righe = file.readlines()
        file.close() 
        utenti_dict = {}
        amicizie = {}

        for riga in righe:
            fields = riga.split(":")
            nome = fields[0]
            utente = Utente(nome)
            self.iscrivi_utente(utente)
            utenti_dict[nome] = utente 
            amicizie[nome] = fields[1].split(",") if len(fields) > 1 else []

        for nome, lista_amici in amicizie.items():
            for nome_amico in lista_amici:
                if nome_amico in utenti_dict:
                    self.aggiungi_amicizia(utenti_dict[nome], utenti_dict[nome_amico])
            

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

def stampa_nomi(lista):
    #serve per stampare i nomi delle liste e non gli oggetti 
    listaNomi=[n.nome for n in lista ]
    return listaNomi

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
    suggeriti=social_network.suggerisci_amici(luca)
    suggeriti=[amico.nome for amico in suggeriti]
    print(suggeriti)
    social_network.carica_da_file("./utenti.txt")
    print (social_network)

if __name__=="__main__":
    main()
    