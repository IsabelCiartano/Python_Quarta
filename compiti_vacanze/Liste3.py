def secondoMassimo(valori):
    massimo=valori[0]
    minimo=valori[0]
    #cerco massimo e minimo 
    for v in valori:
        if v>massimo:
            massimo=v
        if v<minimo: 
            minimo=v
    #assegno a secondo massimo il minimo 
    secondoMassimo=minimo
    #cerco il valore più grande che sia diverso dal massimo 
    for v in valori:
        if (v>secondoMassimo)and(v!=massimo):
            secondoMassimo=v
    return secondoMassimo


def main():
    valori=[1,5,3,7,8,12]
    m=secondoMassimo(valori)
    print(m)


if __name__=="__main__":
    main()