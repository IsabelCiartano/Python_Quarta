
file=open("./testo.txt","r")
testo = file.read()
file.close()

d={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"y":0,"z":0}
count =0
for car in testo:
    car.lower()
    if(car.isalpha()):
        count=count+1
        for l in d:
            if(car==l):
                d[l]=d[l]+1

print(d)
print(count)
for l in d :
    d[l]=(d[l]/count)*100
    print(f"{d[l]}")
