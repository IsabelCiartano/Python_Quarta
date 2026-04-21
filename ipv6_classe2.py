def add_zeros(string):
    """
    Aggiunge zeri a sinistra fino a ottenere 4 caratteri
    """
    return "0" * (4 * len(string)) + string

def short_to_extended(ip):
    ip_list = ip.split(":")

    if "::" in ip:
        ip1, ip2 = ip.split("::")

        part1 = ip1.split(":") 
        part2 = ip2.split(":") 

        n_missing = 8 - (len(part1) + len(part2))

        parts = []
        parts += [add_zeros(p) for p in part1]
        parts += ["0000"] * n_missing
        parts += [add_zeros(p) for p in part2]

        return ":".join(parts)

def remove_zeros(group):
    while len(group) > 1 and group[0] == "0":
        group = group[1:]
    return group

def completeipv6(ip_list):
    ipv6=""
    
    return ipv6


def extended_to_short(ip):
    groups = ip.split(":")

    # 1. rimuovere zeri iniziali
    groups = [remove_zeros(g) for g in groups]

    # 2. trovare sequenza più lunga di "0"
    max_start = -1
    max_len = 0
    current_start = -1
    current_len = 0

    for i, g in enumerate(groups):
        if g == "0":
            if current_start == -1:
                current_start = i
            current_len += 1
        else:
            if current_len > max_len:
                max_start = current_start
                max_len = current_len
            current_start = -1
            current_len = 0

    if current_len > max_len:
        max_start = current_start
        max_len = current_len

    # 3. comprimere con ::
    if max_len > 1:
        groups = groups[:max_start] + [""] + groups[max_start + max_len:]

        if max_start == 0:
            groups = [""] + groups
        if max_start + max_len == 8:
            groups = groups + [""]

        return ":".join(groups).replace(":::", "::")

    return ":".join(groups)

def main():
    # corto a esteso
    ipv6_short = "FDEC:74::B0FF:0:FFF0"
    ipv6_extended = short_to_extended(ipv6_short)
    print("Esteso:", ipv6_extended)

    # esteso a corto
    ipv6_short_again = extended_to_short(ipv6_extended)
    print("Compresso:", ipv6_short_again)

if __name__ == "__main__":
    main()