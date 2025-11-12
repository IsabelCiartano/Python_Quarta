# il carattere # (sharp) serve per i commenti
#in questo programma useremo l'assegnazione
# in python non ci sono dichiarazioni --> dynamic type checking (controllo dinamico dei tipi) sulla base dei valori assegnati alle variabili 

a = input("Scrivi qualcosa -> ") #simile a scanf
                                 #input restituisce SEMPRE stringhe!

#facciamo una print con una f-string
print(f"Hai inserito {a} che è di tipo {type(a)}")