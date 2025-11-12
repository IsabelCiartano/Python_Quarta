import math #libreria matematica 

n=int(input("inserire un numero ->"))

somma=0
if n>=0:
    for i in range(1,2*n+1,2):
        somma=somma+i
        #print(i)
radice_intera=math.isqrt(somma)#radice quadrata
print(f"la somma e': {somma} ,il quadrato perfetto : {radice_intera**2==  somma}") #se la condizione è vera restituisce true 