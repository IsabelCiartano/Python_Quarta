#Legga il file e costruisca un dizionario {nome: [lista_voti]}
#Calcoli la media di ogni studenteProduca una classifica ordinata per media decrescente
#Mostri il "podio" (i primi 3) e gli studenti in difficoltà (media < 6)

def leggi_registo(nome_file):
    file=open(nome_file,"r")
    righe=file.readlines()
    file.close()
    d={}
    #print(righe)
    for r in righe:
        campi=r.split(";")
       # print (campi)
        d[campi[0]]=campi[1:]
    
  
    return d

def calcola_media(voti):
    media=0
    k=0
    for v in voti:
        v=int(v)
        media=media+v
        k=k+1
    media=media/k
    return media



def classifica(registro):
    lista=[]
    
    for el in registro:
        media=calcola_media(registro[el])
        elemento_lista=(el,media)#crea lista tuple
        lista.append(elemento_lista)

def classifica(registro):
    lista=[]
    
    for el in registro:
        media=calcola_media(registro[el])
        elemento_lista=(el,media)#crea lista tuple
        lista.append(elemento_lista)

    n = len(lista)
    for i in range(n - 1):
        for k in range(n - 1 - i):
            if lista[k][1] < lista[k + 1][1]:   # confronto delle medie
                lista[k], lista[k + 1] = lista[k + 1], lista[k]  # swap

    return lista


def stampa_podio(classifica):
   print(f"la classifica è:{classifica[:3]}")

def trova_insufficienti(classifica):
    lista_insufficenti=[]
    n = len(classifica)
    for n in range(n):
        if(classifica[n][1]<6):
            lista_insufficenti.append(classifica[el])
    return lista_insufficenti

def main():
    d=leggi_registo("./registro.txt")
    print(d)
    voti=calcola_media(d["Bianchi Mario"])
    print (voti)
    lista=classifica(d)
    print (lista)
    stampa_podio(lista)
    insufficenti=trova_insufficienti(lista)
   
  
    print(insufficenti)

if __name__=="__main__":
    main()

