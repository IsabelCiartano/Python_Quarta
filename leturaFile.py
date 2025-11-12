file=open("./dati.csv","r")

righe = file.readlines()#lista che contiene le stringhe del file
file.close()
print(righe[0])

titoli=righe[0][:-1].split(",")#[:-1] slicing che elimina lo \n dell'ultima parola 
print(titoli)
titolo1,titolo2,titolo3=righe[0][:-1].split(",")#unpacking spacchettamento 
print(titolo1)
#leggere tutte le altre righe del file e stamparle 
#usare un ciclo for pythonico 
for elemento in righe:
    print(elemento)