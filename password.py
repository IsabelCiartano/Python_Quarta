##l'utente inserisce in input una password 
#il programma stampa la password oscurate da *

password=input("inserisci una password :")
password_blanked = "*" * len(password)     #len restituisce una lunghezza stirnghe/array ....

print(f"Hai  inserito la password : {password_blanked}")
