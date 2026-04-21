

import socket
BUFFER_SIZE = 4096
IP_PORTA = ("127.0.0.1", 9000)

def main():
  
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

    s.bind(IP_PORTA) 

    print("server in ascolto .....")
    while True:
        dati, ip_porta_mittente = s.recvfrom(4090)
        stringa = dati.decode() 
        print(f"Ho ricevuto {stringa} da {ip_porta_mittente}")
        s.sendto(dati, ip_porta_mittente) 
        if stringa.upper()=="EXIT" :
            break
    s.close()

if __name__ == "__main__":
    main()