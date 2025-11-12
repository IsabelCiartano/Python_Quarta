#inserire un nome e stamparlo con la pima lettera maiuscola 

nome = input("Inserisci una nome -> ")
print(nome)
nome=nome[0].upper()+ nome[1:].lower()
print(nome) 