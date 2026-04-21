def addZeros(stringa):
    """ la funzione prende in input una stringa di al massimo 4 carratteri e
     aggiunge degli zero davanti fino a ottenere 4 caratteri """
    return "0" * (4 * len(string)) + string
def remove_zeros(string):
    """prende in unput stringhe di 4 caratteri e toglie gli 0 a sinistra"""
    count=0
    for c in string:
        if c ==0:
            counter+=1
        else:
            break 
    if counter==4:
        return "0"
    else:
        return string[counter:]



def shortToExtended(ip):
    ip_list=ip.split(":")
    n_grups=len(ip_list)
    print(n_grups)
    print(ip_list)
    if n_grups== 8:
        #caso facile 
        #in questo caso dobbiamo sol controllare gli zeri nei gruppi che non li hanno 
        pass
    elif n_grups >8 or n_grups <3:
        print("ERRORE: numero di gruppi errato ")
    else:
        n_missing=8-n_grups
        missing_zeros=["0" for _ in range(n_missing )]
        print(missing_zeros)
        #join serve per concatenare tutte le stringhe della lista che gli viene passato 
        missing_groups=":".join(missing_zeros)
        print(missing_groups)
        ip1,ip2=ip.split("::")
        print (ip1)
        print(ip2)
        ip_nogap=ip1+missing_groups+ip2
    return ip_nogap
def extended_to_short(indirizzo):
    """
    assumiamo di avere al massimo un solo gruppo di 0 consecutivi 
    cerca gruppi di 0 consecutivi e lo sostituisce con ::
    """
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

def extended(ip):
    ipv6=""
    ip_list=ip.split(":")
    n=len(ip_list)
    if n == 8:
        ip_list=[remove_zeros(group) for group in ip_list]

        #for k in range(n):
           # ip_list[k]=remove_zeros(ip_list[k])

        print(ip_list)
        counter=0
        start=-1

        for k,group in enumerate (ip_list)  :
            if group =="0" :
                if start==-1:start=k
                counter+=1
            elif counter !=0:
                break
        print(start, counter)


        #for k in range(n):
           # if ip_list[k]=="0":
               # if start==-1:start=k
               # counter+=1
            #elif counter !=0:
                #break
        #print(start, counter)

        if counter < 2:
            ipv6=":".join(ip_list)
        else:
            ip1=":".join(ip_list[:start])
            ip2=":".join(ip_list[start+counter:])
            ipv6=ip1+"::"+ip2
    return ipv6
    


def main():
    ipv6_short="FDEC:74::B0FF:0:FFF0"
    ipv6_Extended=shortToExtended(ipv6_short)
    print(ipv6_Extended)
    ipv6_short=extended(ipv6_Extended)
    print(ipv6_short)



if __name__=="__main__":
    main()