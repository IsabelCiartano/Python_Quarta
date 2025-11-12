def main():
    lista_nomi=["alice","luca","giovanni","mario"]
    lista_voti=[[6,10,5],
                [7,8],
                [6,8,4,6],
                [5,8]]
#modificare il codice per stampare la media di ognuno, il numero di voti per ognuno,stampare il massimo voto e il minimo 
    #voglio stampare il voto a fianco di ogni nome
    for nome,voto in zip(lista_nomi,lista_voti):
        print(f"{nome}:{voto}") #zip permette di ciclare in parallelo su due o più liste
        media=0
        nNum=len(voto)
        max=voto[0]
        min=voto[0]
        for vot in voto:
            media=media+vot
            if(vot>max):
                max=vot
            elif(vot<min):
                min=vot
        
        media=media/len(voto)
      
        print(f"media ->{media}")
        print(f"voto massimo ->{max}")
        print(f"voto minimo ->{min}")
        print(f"numero voti ->{nNum}")
        print("\n")
   

if __name__ =="__main__": #dunder doppio under __     
    main()
