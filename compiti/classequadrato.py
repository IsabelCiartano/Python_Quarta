#classe quadrato
#attributi : colore + lato +x+y dal vertice in alto a sinistra 
#funzioni area preimetro e disegna
#disegna 100 quadrati casuali 

import random
import turtle

turtle.colormode(255)


class Quadrato:
    def __init__(self, colore, x, y, lato):
        self.colore = colore
        self.x = x
        self.y = y
        self.lato = lato
    def __str__(self):
        return f"({self.x},{self.y}) colore:{self.colore} lato:{self.lato}"

    def area(self):
        return self.lato ** 2

    def perimetro(self):
        return self.lato * 4

    def disegnaQuadrato(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.colore,self.colore)
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(self.lato)
            turtle.right(90)
        turtle.end_fill()


    def disegna_quadrati():
        for _ in range(100):
            x = random.randint(-300, 300)
            y = random.randint(-200, 200)
            lato = random.randint(10, 80)
            colore = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )#variabile tuple con 3 colori 
            #se è su una lista colori=["red","yellow",...]
            #si usa random.choice(colori) per scegliere un colore dalla lista 

            q = Quadrato(colore, x, y, lato)
            q.disegnaQuadrato()

       

def main():
    q = Quadrato("red", 0, 0, 50)
    print("Area:", q.area())
    print("Perimetro:", q.perimetro())
    q.disegnaQuadrato()
    print(q)

    Quadrato.disegna_quadrati()
    turtle.mainloop()

if __name__=="__main__":
    main()
