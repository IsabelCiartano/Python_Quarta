import turtle

def main():
    file = open("./disegno.txt", "r")
    righe = file.readlines()
    file.close()

    for riga in righe:
        
        comandi = riga.split(" ")
        cmd = comandi[0]

        if cmd == "avanti":
            turtle.forward(int(comandi[1]))

        if cmd == "destra":
            turtle.right(int(comandi[1]))

        if cmd == "colore":
            turtle.pencolor("red")

        if cmd == "salta":
            x = int(comandi[1])
            y = int(comandi[2])
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()

        if cmd == "cerchio":
            turtle.circle(int(comandi[1]))

    turtle.mainloop()

if __name__ == "__main__":
    main()