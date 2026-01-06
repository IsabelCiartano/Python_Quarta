#Pari e dispari
#Data una lista di interi, scrivere una funzione che restituisca due liste separate: una con
#i numeri pari e una con i dispari.
def PariDispari(numeri):
    pari=[]
    dispari=[]
    for n in numeri:
        if n %2 ==0:
            pari.append(n)
        else:
            dispari.append(n)
    return pari,dispari

def main():

    numeri = [3, 8, 12, 7, 2, 15, 20, 9, 4]
    p=[]
    d=[]
    p,d=PariDispari(numeri)
    print(p)

    print(d)

if __name__ =="__main__": #dunder doppio under __
    print(__name__)
    main()