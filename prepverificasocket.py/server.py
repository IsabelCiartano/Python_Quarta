import socket

BUFFER_SIZE = 4096
IP_PORTA=("127.0.0.1",5005)
def main():
    d={"cuneo":20,"catania":27,"roma":25,"aosta":14,"cagliari":24}
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
   
    s.bind(IP_PORTA)

    print(" server in ascolto....")

    while True:
        dati,ip_porta_mittente= s.recvfrom(BUFFER_SIZE)
        stringa= dati.decode()
        print(f"ho ricevuto da {ip_porta_mittente} la stringa :{stringa}")
        citta=stringa
        msg="ERROR città non esistente "
        for i in d:
            if stringa.lower()==f"get {i}":
                msg=f"TEMP {i} {d[i]}"
            break
          
        s.sendto(msg.encode(),ip_porta_mittente)
        if stringa.upper()=="EXIT":
            break
    s.close()
if __name__=="__main__":
    main()