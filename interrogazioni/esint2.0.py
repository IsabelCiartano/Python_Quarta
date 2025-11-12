file=open("./nome.txt","r")
righe=file.readlines()
for r in righe:
    if(r[0:2]=="##"):
       print(r)
close(file)

    