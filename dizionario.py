def main():
    #un dizionario è una sequenza di coppie di chiave :valore 
    elenco={"A0-FF-51-B3-D1-FF":"luca","A0-FF-51-B3-D5-FF":"mario"}
    #prima parte chiave seconda valore 
    mac="A0-FF-51-B3-D1-FF"
    if mac in elenco :
        print(elenco[mac])#ricerca si può sempre fare sulla chiave 
        #hanno come indice le loro chiavi 
    else:
        print("mac non trovato") 

    elenco["A0-FF-FF-B3-FF-FF"]="broadcast"
    print(elenco)

if __name__=="__main__":
    main()