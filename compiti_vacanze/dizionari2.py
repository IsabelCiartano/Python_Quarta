studenti_voti={
    "marco":7,
    "sara":9,
    "mendy":5,
    "isa":6,
    "luca":7
}

dizionario_contatori={}#la chiave è il voto, il valore è il numerodi occorrenze 
for studente in studenti_voti:
    voto=studenti_voti[studente]#valore del voto studente invece è il nome 
    if voto in dizionario_contatori:
        dizionario_contatori[voto] +=1
    else:
        dizionario_contatori[voto]=1
print(dizionario_contatori)

voto_piu_frequente=6
frequenza_max=6
for voto in dizionario_contatori:
    if dizionario_contatori[voto]>frequenza_max:
        frequenza_max=dizionario_contatori[voto]
        voto_piu_frequente=voto
print(f"il voto più frequente è {voto_piu_frequente} e la frequenza massima è di {frequenza_max}")