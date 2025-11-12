intero = int(input("Inserisci un numero intero -> "))
print(f"Hai inserito {intero} che è di tipo {type(intero)}")

decimale = float(input("Inserisci un numero decimale -> "))
print(f"Hai inserito {decimale} che è di tipo {type(decimale)}")

somma = intero + decimale
print(f"La somma tra i due numeri vale {somma} ed è di tipo {type(somma)}")