#Scacchiera
#Disegnare una scacchiera 8×8 con caselle alternate bianche e nere.

import turtle

lato_casella = 40

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-160, 160)  # posizione iniziale
t.pendown()

def disegna_quadrato(colore):
    t.fillcolor(colore)
    t.begin_fill()
    for _ in range(4):
        t.forward(lato_casella)
        t.right(90)
    t.end_fill()

for riga in range(8):
    for colonna in range(8):
        if (riga + colonna) % 2 == 0:
            colore = "white"
        else:
            colore = "black"
        disegna_quadrato(colore)
        t.forward(lato_casella)
    
    # torna all'inizio della riga successiva
    t.backward(8 * lato_casella)
    t.right(90)
    t.forward(lato_casella)
    t.left(90)

turtle.done()
