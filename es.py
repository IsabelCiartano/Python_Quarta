a=input("inserire una stringa->")
n=int (input("inserire un numero ->"))
if n <= len(a):
    s=a[0:n]+ '*'*(len(a)-n)
    print(s)