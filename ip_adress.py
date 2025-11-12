ip= input("inserisci un indirizzo IP-> ")
#.split è unnmetodo delle stringhe che suddivide una stringa cercando il carattere separatore
ottetti_str=ip.split(".")
print(ottetti_str)
nbit=8
ottetti_int=[]#lista vuota 
for s in ottetti_str:
    ottetti_int.append(int(s))
print(ottetti_int)

for i in range(4):
    binar=(bin(ottetti_int[i]))
    if len(binar)<nbit:
        binario ='0'*(nbit-len(binar))+binar
    else:
        binario=binar
    print(binario, end='.')