import math
import turtle
#pigame libreria per vidogioco

class Punto:
    # costruttore
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def distanza_origine(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def scambia_coordinate(self):
        return Punto(self.y, self.x)
    
    def disegna(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.dot(5, "red")   # disegna il punto
        turtle.goto(0, 0)
    
    def distanza(self, altro):
        # distanza tra due punti
        return math.sqrt(
            (self.x - altro.x)**2 + (self.y - altro.y)**2
        )


def main():
    a = Punto(1, 2)
   

    print(a)
    print(f"Distanza dall'origine: {a.distanza_origine():.2f}")
    b=a.scambia_coordinate()
    print(b)
    print(f"Distanza tra a e b: {a.distanza(b):.2f}")

    a.disegna()
    b.disegna()
    turtle.done()


if __name__ == "__main__":
    main()
