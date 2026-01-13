#1. Catalogo libri
#Una lista contiene dizionari con chiavi titolo, autore, anno, prezzo. Scrivere funzioni
#per: (a) cercare libri di un autore, (b) calcolare il prezzo medio, (c) trovare il libro più
#recente.

def a(libri,autore_ricercato):
    """
    cerca i libri di un autore
    """
    libriTrovati=[]
    for l in libri:
            if l["autore"].lower() == autore_ricercato.lower():
                libriTrovati.append(l)

    return libriTrovati

def b(libri):
    """
    calcola il prezzo medio
    """
    prezzo_medio=0
    k=0
    for l in libri:
            p=int(l["prezzo"])
            prezzo_medio=p+prezzo_medio
            k=k+1
    prezzo_medio=prezzo_medio/k
    return prezzo_medio

def c(libri):
    """
    trova il libro più recente
    """
    anno=0
    for l in libri:
            a=int(l["anno"])
            if a > anno:
                anno=l["anno"]
    return anno


def main():
    libri = [
    {"titolo": "Il nome della rosa", "autore": "Umberto Eco", "anno": 1980, "prezzo": 15.50},
    {"titolo": "1984", "autore": "George Orwell", "anno": 1949, "prezzo": 12.00},
    {"titolo": "Il pendolo di Foucault", "autore": "Umberto Eco", "anno": 1988, "prezzo": 18.00},
    {"titolo": "Fahrenheit 451", "autore": "Ray Bradbury", "anno": 1953, "prezzo": 11.50},
    {"titolo": "Il mondo nuovo", "autore": "Aldous Huxley", "anno": 1932, "prezzo": 13.00}
    ]

    libriTrovati=[]
    libriTrovati=a(libri,"Umberto Eco")
    print(libriTrovati)
    prezzo_medio=b(libri)
    print(prezzo_medio)
    anno=c(libri)
    print(anno)

if __name__=="__main__":
    main()