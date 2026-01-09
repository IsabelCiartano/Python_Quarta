import turtle

def sposta (x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()


def poligono(n,lung):
    angolo=360/n 
    for _ in range(n):
        turtle.forward(lung)
        turtle.left(angolo)

def main():
    nPoligoni=4
    lato=100
    shift=200
    x0,y0=-300,-lato/2
    for i in range (nPoligoni):
        y=y0
        x=x0+shift*i
        sposta(x,y)
        poligono(i+3,lato)
    turtle.mainloop()

if __name__=="__main__":
    main()