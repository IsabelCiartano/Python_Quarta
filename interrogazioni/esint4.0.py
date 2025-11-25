def main():
    ip=input("inserisci un ip:")
    isTrue=controlla(ip)
    print(isTrue)

def controlla(ip):
    fields=ip.split(".")
    if len(fields)==4:
        return true

