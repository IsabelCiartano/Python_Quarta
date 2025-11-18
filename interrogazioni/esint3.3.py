def funzione(m1,m2):
    n1=m1.split("-")
    n2=m2.split("-")
    i=0
    for t,v in zip(n1,n2):
        if(t==v):
            i=i+1
    return i

m1='A0-FF-51-B3-D1-FF'
m2='A0-F2-51-B5-D13-FF'

i=funzione(m1,m2)
print(i)
