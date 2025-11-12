def main():
    Mac="C0:A5:E8:A3:B6:69" #input("inserire il mac addres che si vuole ricercare ->")
    macutile=Mac[:8]
    file=open("./mac-vendors-export.csv","r",encoding ='utf-8')#risolve i problemi di apertura caso utilizzo windows
    righe = file.readlines()
    file.close()

    for i in righe:
        if i[:8] == macutile:
            print(i)


if __name__ =="__main__": #dunder doppio under __
    main()  