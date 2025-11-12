def main_0():
    lista=["alice","luca","giovanni","mario"]
    nome_max= None
    len_max =0
    for nome in lista :
        if len(nome)>len_max:
            nome_max=nome
            len_max=len(nome)
    print(nome_max)

def main():
    lista=["alice","luca","giovanni","mario"]
   
    for i, nome in enumerate(lista) :
        print(f"{i} {nome}")

if __name__ =="__main__": #dunder doppio under __
    print(__name__)
    main()
