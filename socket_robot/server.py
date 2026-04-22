import socket
from turtle import Turtle,Screen

alphabot=Turtle() #istanza di turtle 
screen=Screen()

def isOK(stringa):
    ok=True
    fields=stringa.split(",")
    if fields[0].lower()=="forward" or fields[0].lower()=="backward" or fields[0].lower()=="right" or fields[0].lower()=="left":
        return ok
    else:
        ok=False
        return ok

def main():
    #alphabot.forward(100)
#il server deve ricevere messaggi con questo formato:
#f"{comando},{valore}"
#a seconda del messaggio ricevuto esegue il comando sulla turtle 
#creare un server udp che sta in ascolto di messaggi, li verifica (formattazione corretta)
#se il messaggio è corretto esegue e manda al client messaggio di OK
#gestire il comando exit 
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    IP_PORTA = ("127.0.0.1",9000)
    s.bind(IP_PORTA)
    BUFFER_SIZE = 4096
    print("server in ascolto .....")
    while True:
        dati, ip_porta_mittente = s.recvfrom(BUFFER_SIZE)
        stringa = dati.decode()
        if stringa.upper()=="EXIT":
            break
        print(f"Ho ricevuto {stringa} da {ip_porta_mittente}")
        if isOK(stringa):
            ok="ok"
            s.sendto(ok.encode(), ip_porta_mittente) 
            fields=stringa.split(",")
            if fields[0].lower()=="forward":
                alphabot.forward(int(fields[1]))
            if fields[0].lower()=="backward":
                alphabot.backward(int(fields[1]))
            if fields[0].lower()=="right":
                alphabot.right(int(fields[1]))
            if fields[0].lower()=="left":
                alphabot.left(int(fields[1]))
        else:
            ok="not ok"
            s.sendto(ok.encode(), ip_porta_mittente) 
    s.close()
    screen.mainloop()
if __name__=="__main__":
    main()