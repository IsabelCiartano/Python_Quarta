#Un dizionario associa nomi di materie a liste di voti. Scrivere funzioni per: (a) calcolare
#la media di una materia, (b) trovare la materia con media più alta, (c) aggiungere un
#voto a una materia.

def media_materia(voti_materie, materia):
    voti = voti_materie[materia]
    return sum(voti) / len(voti)



def materia_media_piu_alta(voti_materie):

    media_max = 0

    for materia in voti_materie:
        media = sum(voti_materie[materia]) / len(voti_materie[materia])
        if media > media_max:
            media_max = media
            

    return media_max



def aggiungi_voto(voti_materie, materia, voto):
    voti_materie[materia].append(voto)


voti_materie = {
    "Matematica": [6, 7, 5, 8, 7],
    "Italiano": [7, 8, 7, 6],
    "Inglese": [8, 8, 9, 7, 8],
    "Informatica": [9, 8, 9, 10, 8]
}

print(media_materia(voti_materie, "Matematica"))
print(materia_media_piu_alta(voti_materie))
aggiungi_voto(voti_materie, "Matematica", 5)
print(voti_materie)
