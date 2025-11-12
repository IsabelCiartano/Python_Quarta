#In python abbiamo le collezioni (inisemi di diversi elementi )
#tra le collezioni abbiamo:
#liste,tuple,dizionari.

#vediamo le liste 
#creare una lista 
l=[3,3.14,10,"ciao",True]

#per accedere agli elementi esistono le stesse regole di:
#indicizzazione e slicingdelle stringhe 

print(f"l'ultimo elemento della lista {l[-1]}")
print(l) #stampa tutta la lista 
print(f"tutta la lista senza il primo e l'ultimo elemento {l[1:-1]}")

#aggiungere un elemento alla lista 
l.append("NUOVO") #non restituisce nulla ,ma modifica l !!!!
print(l)
l.pop() #rimuove l'ultimo elemento della lista 
print(l)