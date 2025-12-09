file=open("./temp.csv","r")
righe=file.readlines()
file.close()
campo=righe[0].split(",")
d={}

for riga in righe[1:]:
    campi=riga.split(",")
    print(campi)
    lista=campi[0]
    lista2=campi[1]

d[campo[0]]=lista
d[campo[1]]=lista2
print(d)