from threading import Thread
import time
import random 
class Rilevatore(Thread):
    def __init__(self,citta,n_misurazioni):
        super().__init__()
        self.citta=citta
        self.n_misurazioni=n_misurazioni
        self.misurazioni=[]
    def run(self):
        for i in range(self.n_misurazioni):
            time.sleep(random.uniform(0.1,0.5))
            t=random.uniform(-10,30)
            self.misurazioni.append(t)

    def media(self):
        if len(self.misurazioni)==0:
            return 0.0
        else:
            return sum(self.misurazioni)/len(self.misurazioni)
    def __str__(self):
        return f"{self.citta} : {self.n_misurazioni} misurazioni, media {self.media():.2f}"

def main():
    rete={
        "cuneo":Rilevatore("cuneo",5),
        "torino":Rilevatore("torino",3),
        "milano":Rilevatore("milano",4),
        "roma":Rilevatore("roma",7)
    }

    for citta in rete:
        rete[citta].start()
    for citta in rete:
        rete[citta].join()
    for citta in rete:
        print(rete[citta])

    tempMax,tempMin = -10,30
    cittaMax,cittaMin=None, None

    for citta in rete:
        if rete[citta].media()<tempMin:
            tempMin=rete[citta].media()
            cittaMin=citta
        if rete[citta].media()>tempMax:
            tempMax=rete[citta].media()
            cittaMax=citta
    print(f"{cittaMax} maggiore e {cittaMin} minore")


if __name__=="__main__":
    main()