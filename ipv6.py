def add0s(string):
    """
    La funzione prende in input una stringa di max. 4 caratteri
    e aggiunge 0 a sinistra fino a ottenere 4 caratteri
    """
    if len(string) < 4:
        string = "0" * (4-len(string)) + string
    elif len(string) > 4:
        print("ERRORE: stringa troppo lunga")
    return string

def completeIpv6(ip_list):
    ip_final = ""
    for group in ip_list:
        ip_final += add0s(group) + ":"
    ip_final = ip_final[:-1]
    #print(ip_final)
    return ip_final

def shortToExtended(ip):
    ip_list = ip.split(":")
    n_groups = len(ip_list)
    #print(n_groups)
    #print(ip_list)
    ipv6 = ""

    if n_groups == 8:
        ipv6 = completeIpv6(ip_list)

    elif n_groups > 8 or n_groups < 3:
        # errore
        print("ERRORE: numero di gruppi errato >:( ")
        ipv6 = None

    else:
        n_missing = 8 - n_groups
        missing_0s = ["0" for _ in range(n_missing + 1)]
        missing_groups = ":".join(missing_0s)
        # join() concatena gli elementi di una lista mettendo il carattere in mezzo
        #print(missing_groups)

        ip1, ip2 = ip.split("::")
        #print(ip1)
        #print(ip2)
        
        ipv6 = ip1 + ":" + missing_groups + ":" + ip2
        ip_list = ipv6.split(":")
        ipv6 = completeIpv6(ip_list)

    return ipv6

def remove0s(string):
    """
    Prende in input stringhe da 4 caratteri
    Rimuove evenutali 0 a sinistra
    """
    counter = 0
    for c in string:
        if c == "0":
            counter += 1
        else:
            break
    if counter == 4:
        return "0"
    return string[counter:]

def extendedToShort(ip):
    """
    Assumiamo di avere al massimo un solo gruppo di 0 consecutivi
    Cerca il gruppo di 0 consecutivi, e lo sostituisce con un ::
    """
    ip_list = ip.split(":")
    n_groups = len(ip_list)
    #print(n_groups)
    #print(ip_list)
    ipv6 = ""

    if n_groups == 8:
        ip_list = [remove0s(group) for group in ip_list]
        # for k in range(n_groups):
        #     ip_list[k] = remove0s(ip_list[k])
        #print(ip_list)

        counter = 0
        start = -1
        for k, group in enumerate(ip_list):
            # enumerate() cicla sia sulla posizione che sul valore
            if group == "0":
                if start == -1: start = k
                counter += 1
            elif counter != 0:
                break
        #print(start, counter)

        if counter < 2:
            ipv6 = ":".join(ip_list)
        else:
            ip1 = ":".join(ip_list[:start])
            #print(ip1)
            ip2 = ":".join(ip_list[start+counter:])
            #print(ip2)
            ipv6 = ip1 + "::" + ip2
    else: # n_groups != 8
        print("ERRORE: numero di gruppi errato >:(")
        ipv6 = None
    
    return ipv6

def main():
    ipv6_short = "FDEC:74::B0FF:0:FFF0"
    ipv6_extended = shortToExtended(ipv6_short)
    # Finché questa (^) non restituisce, ipv6_extended = None
    print(ipv6_extended)

    print("-"*86)
    ipv6_newShort = extendedToShort(ipv6_extended)
    print(ipv6_newShort)
    
    print("-"*86)
    print(f"RISULTATI:\nIP breve: {ipv6_short}\nIP esteso: {ipv6_extended}\nIP breve 2: {ipv6_newShort}")

if __name__ == "__main__":
    # se ipv6 viene richiamato, la if è falsa, e non esegue
    main()