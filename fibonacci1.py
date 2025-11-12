#sequenza di fibonacci

n=int(input("inserisci quanti numeri di Fibonacci vuoi? ->"))
a,b=1,1 #inizializzazione NON dichiarazione !!!
if n>2:
    print(a, end=" - ") #stampa " - "
    print(b,end=" - ")
    for i in range (n-2):
     #pass istruzione vuota che rende il codice corretto e poterlo eseguire anche se non si ha fatto qualcosa nel if
        a,b=b,a+b #stampa " - "
        print(b,end=" - ")
      
elif n==2:
    print(a, end=" - ") 
    print(b)
elif n==0:
    print("nessun numero")
elif n==1:
    print(a)  
    
