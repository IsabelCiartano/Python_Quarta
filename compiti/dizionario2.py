import uuid

def getMyMac():
    mac=uuid.getnode()
    mac_str=":".join(f"{(mac>>i)&0xff:02x}"for i in range (40,-1-8))
    return mac_str

def preparaMac(mac_str):
    mac_str=mac_str.replace("-",":")
    mac_str.upper()
    return mac_str

def main():
    file=open("./mac-vendors-export.csv","r",encoding ='utf-8')
    righe=file.readlines()#righe è una lista di stringhe 
    file.close
    elenco={}
    mac=[]
    vendors=[]
    for riga in righe[1:]:#riga è una stringa 
        campi=riga.split(",")#campi è una lista di stringhe 
        mac.append(campi[0])
        vendors.append(campi[1])
    for m,v in zip(mac,vendors):
        chiave=m.upper()
        valore=v
        elenco[chiave]=valore
    ricerca=getMyMac()
    ricerca=preparaMac(ricerca)[:8]
    if ricerca in elenco:
        print(elenco[ricerca])
    else:
        print("mac non trovato")
         
if __name__ == "__main__":
    main()

