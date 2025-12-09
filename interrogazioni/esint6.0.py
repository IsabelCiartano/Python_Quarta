comand={0:"forward",1:"backward",2:"left",3:"right"}
file=open("./interrogazione.csv","r")
righe=file.readlines()
file.close()
for riga in righe:
    n=int(riga)
    print(comand[n])