class Libro():
    def __init__(self,titolo,autore,anno,pagine):
        self.letto=False
        self.titolo=titolo
        self.autore=autore
        self.anno=anno
        self.pagine=pagine
    def eta(self,anno_corrente):
        return anno_corrente-self.anno
    def e_classico(self,anno_corrente):
        ok=False
        if eta(anno_corrente)>=50:
            ok=True
        return ok
    def __str__(self):
        if self.letto==True:
            stringa=f"{self.autore}-{self.titolo}({self.anno}),{self.pagine}pp. [letto] "
        else:
            stringa=f"{self.autore}-{self.titolo}({self.anno}),{self.pagine}pp. [ da leggere] "
        return stringa
def dopo_soglia(biblioteca,soglia):
    libri=[]
    libri=[l for l in biblioteca if l.anno > soglia]
    return libri 
def main():
    
    biblioteca=[Libro("signore degli anelli","tolkien",1820,1500),Libro("children of a minor sport", "manuel nordio",2026,160)]
    gia_letti=[l for l in biblioteca if l.letto == True]
    print("libri-------------------------------")
    for l in biblioteca:
        print(l)
    print("libri già letti-------------------------------------")
    for l in gia_letti:
        print(l)
    soglia=dopo_soglia(biblioteca,1800)
    print("soglia--------------------------------------------")
    for l in soglia:
        print(l)

if __name__=="__main__":
    main()

        
