# in python possiamo delimitare con "" oppure ' '
stringa= "ciao mondo!"
print(stringa)

#esempio di indicizzazione della stringa 
print(f"l'ultimo caratteredella stringa è {stringa[-1]}")

# esempio di slicing delle stringhe 
print(f"la sotto stringa 2-5 è {stringa[2:5]}.")

#assegnazione multipla ( vale per igni tipop di dato)
nome,cognome="mario","rossi"
#concatenazione tra stringhe 
x =nome + " " + cognome 
print (x)

#concatenazione di una stringa con se stessa piu volte 
y=nome*5
print(y)

y=(nome+" ")*5
print(y)