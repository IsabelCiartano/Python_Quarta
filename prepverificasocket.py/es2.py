class Studente():
    def __init__(self,nome,cognome):
        self.nome=nome
        self.cognome=cognome
        self.voti=[]
    def aggiungi_voto(self,v):
        if v>=1 and v<=10:
            self.voti.append(v)
            return True
        else:
            print("err:voto non nel range")
            return False
    def media(self):
        n=len(self.voti)
        media=(sum(self.voti))/n
        return float(media)
    def e_promosso(self):
        if self.media() > 6:
            return True
        else:
            return False
    def __str__(self):
        if self.e_promosso():
            stringa=f"{self.cognome} {self.nome}: media {self.media():.1f} [promosso]"
        else:
            stringa=f"{self.cognome} {self.nome}: media {self.media():.1f} [non promosso]"
        return stringa 

def cognomi_promossi(classe):
    promossi=[studente.cognome for studente in classe if studente.e_promosso()]
    return promossi
def tre_voti(classe):
    lista=[studente for studente in classe if len(studente.voti) >= 3]
    return lista 

def main():
    classe=[Studente("Rossi","mario"),Studente("ciartano","isabel"),Studente("bruno","carlotta")]
    classe[0].aggiungi_voto(4)
    classe[0].aggiungi_voto(3)
    classe[0].aggiungi_voto(1)

    classe[1].aggiungi_voto(7)
    classe[1].aggiungi_voto(8)
    

    classe[2].aggiungi_voto(7)
    classe[2].aggiungi_voto(8)
    classe[2].aggiungi_voto(9)

    promossi=cognomi_promossi(classe)
    print(promossi)
    lista=tre_voti(classe)
    for studente in lista:
        print(studente)


if __name__=="__main__":
    main()

