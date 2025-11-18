file=open("./voti.csv","r",encoding="utf-8")
righe=file.readlines()
somma=0
for element in righe:
    v=element.split(",")
    somma=somma+int(v[1])
media=float(somma/len(righe))
file.close()
    



    