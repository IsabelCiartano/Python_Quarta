class ContoCorrente():
    def __init__(self,intestatario,iban):
        self.intestatario=intestatario
        self.iban=iban
        self.saldo=0.0
    def versa(self,importo):
        if importo > 0 :
            self.saldo+=importo
            return True
        else:
            print("err importo negativo")
            return False
    def preleva(self,importo):
        if importo > 0 :
            if importo <= self.saldo:
                self.saldo-=importo
                return True
            else:
                print("err: importo maggiore del saldo")
                return False
        else:
            print("err: importo negativo")
            return False
    def bonifico(self,altro_conto,importo):
        if(self.preleva(importo)):
            if(altro_conto.versa(importo)):
                return True
            else:
                print("err: versamento non riuscito")
                return False
        else:
            print("err:prelievo non riuscito")
            return False
    def __str__(self):
        return f"{self.intestatario} ({self.iban}) : saldo {self.saldo} euro"

def main():
    c1=ContoCorrente("isa","IC1234")
    c2=ContoCorrente("vitto","VB5678")

    if(c1.versa(100)):
        print("versamento riuscito")
        print(c1)
    if(c1.preleva(50)):
        print("prelievo riuscito")
        print(c1)
    if(c1.bonifico(c2,30)):
        print("bonifico riuscito ")
        print(c1)
        print(c2)
    if(c1.preleva(200)):
        print("prelievo riuscito")
        print(c1)


if __name__=="__main__":
    main()