#server udp che riceve dei messaggi dentro i quali ci sono indirizzi ip 
#può abbreviare o scriverli in form estesa

import socket
from ipv6 import shortToExtended, extendedToShort
#messaggio del client= f"{comando},{indirizzo}"
#comando SHORT o EXTEDED

#il server ogni volta che rceve un messaggio scrive su file csv 

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
IP_PORTA = ("127.0.0.1", 13000)
s.bind(IP_PORTA)
BUFFER_SIZE = 4096
print("server in ascolto .....")
while True:
    dati, ip_porta_mittente = s.recvfrom(BUFFER_SIZE) 
    stringa = dati.decode() 
    print(f"Ho ricevuto {stringa} da {ip_porta_mittente}")
    fields=stringa.split(",")
    if(fields[0]=="SHORT"):
        ipv6=extendedToShort(fields[1])
    else:
        ipv6=shortToExtended(fields[1])
    print(ipv6)
    file=open("ipv6.csv","w")
    file.write(ipv6+",")
    file.close()
    if stringa.upper()=="EXIT":
        break

s.close()

