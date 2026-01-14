print("apertura file...")
file=open("./testo.txt","r")
print("lettura file....")
testo = file.read()#legge ogni carattere
file.close() 
print("file letto!")

d={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,
   "g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,
   "r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"y":0,"z":0}
count =0
print("="*30)
print("calcolo percentuali in corso....")
for car in testo:
    car.lower()
    if(car.isalpha()):
        count=count+1
        for l in d:
            if(car==l):
                d[l]=d[l]+1
#print(d)
#print(count)
#percentuali={(d[l]/count)*100 for l in d } calcola la percentuale con la comprehention
for l in d :
    d[l]=(d[l]/count)*100
    print(f"lettera: {l}\n percentuale:{d[l]: .2f} %") 
print("="*30) 
 
