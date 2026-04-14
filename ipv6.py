#fare un programma che prenda in input un ipv6 in versione estesa e lo abbrevi 
#2001:0db8:85a3:0000:0000:8a2e:0370:7334


def comprimi(indirizzo):
    abbreviato=""
    divisioni=indirizzo.split(":")
    for d in divisioni:
        n=0
        while n<len(d) and d[n] == "0": 
            n+=1
        if n == 4:
            d=""  
        else:
            d=d[n:]
        abbreviato=abbreviato+d+":"
    return abbreviato[:-1]
def espandi(abbreviato):
    indirizzo=""
    divisioni=abbreviato.split(":")
    for d in divisioni:
        n=0
        while n<len(d) and d[n] !="0":
            n+=1
        if n==0:
            d="00"
        if n<4:
            cont=3-n
            d="0"*cont+d
        else:
            d=d
        abbreviato=abbreviato+d+":"
    return abbreviato


def main():
    indirizzo=input("inserire un indirizzo ipv6 ->")
    c=comprimi(indirizzo)
    print (c)
    c=espandi(c)
    print(c)

if __name__=="__main__":
    main()

