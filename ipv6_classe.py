def addZeros(stringa):
    """ la funzione prende in input una stringa di al massimo 4 carratteri e
     aggiunge degli zero davanti fino a ottenere 4 caratteri """


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

def main():
    ipv6_short="FDEC:74::B0FF:0:FFF0"
    ipv6_Extended=shortToExtended(ipv6_short)
    print(ipv6_Extended)



if __name__=="__main__":
    main()