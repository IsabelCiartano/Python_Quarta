def main():
    
   
    file=open("./mac-vendors-export.csv","r",encoding ='utf-8')#risolve i problemi di apertura caso utilizzo windows
    righe = file.readlines()
    file.close()
    mac_addres=[]
    vendor=[]

    for i in righe[1:]:
        campi=i.split(",")
        mac_addres.append(campi[0])
        vendor.append(campi[1])

    mac="C0:A5:E8:00:00:00" #input("inserire il mac addres che si vuole ricercare ->")
    for m,v,in zip(mac_addres,vendor):
        if m==mac[:8]:
            print(v)
#stampare anche la data di produzione 
   
      
        


if __name__ =="__main__": #dunder doppio under __
    main() 