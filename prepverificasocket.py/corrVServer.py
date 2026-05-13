import socket

IP_PORTA=("127.0.0.1",5005)
BUFFER_SIZE=4096

def ordinaClassifica(classifica):
    lista_tuple=[(classifica[citta],citta) for citta in classifica]
    lista_tuple.sort()
    classifica_ordinata={tupla[1]: tupla[0] for tupla in lista_tuple}#dictionary coprehention
    return classifica_ordinata

def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(IP_PORTA)

    classifica={}

    while True:
        dati,ip_porta_mittente=s.recvfrom(BUFFER_SIZE)
        messaggio=dati.decode().upper()

        if messaggio[0:5]=="VOTA ":
            _,citta=messaggio.split(" ")
            if citta in classifica:
                classifica[citta]+=1
            else:
                classifica[citta]=1
            s.sendto(f"OK {citta} : {classifica[citta]}".encode(),ip_porta_mittente)
        elif messaggio[0:10]=="CLASSIFICA":
            risposta=""
            if len(classifica)==0:
                s.sendto(f"err: nessun voto")
            else:
                for i,citta in enumerate(classifica):
                    risposta=risposta+f"{i+1} {citta} {classifica[citta]}\n"
                s.sendto(risposta.encode(),ip_porta_mittente)
        else:
            s.sendto(f"ERR: comando sconosciuto".encode(),ip_porta_mittente)
        
if __name__=="__main__":
    main()