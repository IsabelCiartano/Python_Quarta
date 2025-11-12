#chiede un numero binario come stringa ,se la lunghezza del numero inserito, se è minore delnumro di bit aggiungere degli 0 a sinistra per arrivare a 8 bit 
bin=input("inserire un numero binario ->")
nbit=int(input("quanti bit->"))
if len(bin)<nbit:
    binario='0'*(nbit-len(bin))+bin
print(binario)