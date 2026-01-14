#3. Filtro prodotti
#Una lista contiene dizionari con chiavi nome, categoria, prezzo. Scrivere una funzione
#che restituisca solo i prodotti di una certa categoria con prezzo inferiore a un valore dato.

def funz(prodotti,categoria,prezzo):
    lista_prod=[]
    for prodotto in prodotti:
        if prodotto["categoria"]== categoria:
            if prodotto["prezzo"]<prezzo:
                lista_prod.append(prodotto)
    return lista_prod



def main():

    prodotti = [
    {"nome": "Laptop", "categoria": "elettronica", "prezzo": 899.99},
    {"nome": "Mouse", "categoria": "elettronica", "prezzo": 29.99},
    {"nome": "Scrivania", "categoria": "arredamento", "prezzo": 199.99},
    {"nome": "Tastiera", "categoria": "elettronica", "prezzo": 79.99},
    {"nome": "Sedia", "categoria": "arredamento", "prezzo": 149.99},
    {"nome": "Monitor", "categoria": "elettronica", "prezzo": 349.99}
    ]

    print(funz(prodotti,"elettronica",80))

if __name__=="__main__":
    main()