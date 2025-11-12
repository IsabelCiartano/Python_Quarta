def oscura(s):
    password_blanked = s[0]+"*" * (len(s)-1)
    return password_blanked    

def main():
    lista=["ciao","password"]
    for p in lista:
        print(oscura(p))


if __name__ =="__main__":
    main()
