#3. Numeri da file
#Un file contiene un numero intero per riga. Leggere il file e calcolare: somma, media,
#minimo e massimo.
file=open("./numeri.txt","r")
numeri=file.readlines()
file.close()
somma=0
media=0
cont=0


print(numeri)
print(min(numeri))
print(max(numeri))

for n in numeri:
    n=int(n)
    somma=somma+n
    cont=cont+1

print(somma)
media=somma/cont
print(media)
