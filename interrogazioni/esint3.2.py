mac=input("inserisci un mac address->")
file=open("./mac.csv","r",encoding="utf-8")
righe=readlines(file)
macad=[]
owner=[]
for i in righe[]:
    campi=i.split(",")
    macad.append(campi[1])
    owner.append(campi[0])

for m,o in zip(macad,owner) :
     if mac==m :
        print(o) 