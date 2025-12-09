def ping(ip):
    return true

def main():
    l=['192.168.100.1','10.100.23.201']
    d={}
    for el in l:
        t=ping(el)
        d[el]=t

    print(d)

if __name__=="__main__"
    main()