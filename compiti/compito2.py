#dato un numero intero dire se è divisibile per 2,3, 5

numero=int(input("inserisci un numero intero ->"))
print(numero)

if numero % 2==0:
    print(f"il numero {numero} e' divisibile per 2")
if numero % 3 ==0 :
    print(f"il numero {numero} e' divisibile per 3")
if numero % 5 == 0:
    print(f"il numero {numero} e' divisibile per 5")
else:
    print("non e' divisibile per i numeri dati ")