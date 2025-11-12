risp=int(input("inserire un numero per cio che si vuole fare 0-somma,1-sottrazione,2-moltiplicazione,3-divisione -> "))
if risp == 0:
    print("somma")
    a=int(input("inserire il primo numero-> "))
    b=int(input("inserire il secondo numero-> "))
    somma=a+b
    print(f"la somma e' :{somma}")
elif risp ==1:
    print("sottrazione")
    a=int(input("inserire il primo numero-> "))
    b=int(input("inserire il secondo numero-> "))
    diff=a-b
    print(f"la differenza e' :{diff}")
elif risp ==2:
    print("prodotto")
    a=int(input("inserire il primo numero-> "))
    b=int(input("inserire il secondo numero-> "))
    p=a*b
    print(f"il prodotto e':{p}")
elif risp ==3:
    print("quoziente")
    a=int(input("inserire il primo numero-> "))
    b=int(input("inserire il secondo numero-> "))
    q=a/b
    print(f"il quoziente e'{q}")
else:
    print("numero non valido")
