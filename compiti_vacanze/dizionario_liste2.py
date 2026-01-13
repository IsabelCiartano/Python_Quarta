#Playlist
#Un dizionario associa nomi di playlist a liste di titoli di canzoni. Scrivere funzioni per:
#(a) contare le canzoni totali, (b) cercare in quale playlist si trova una canzone, (c) unire
#due playlist in una nuova.
def contaCanzoni(lista):
    numero_canzoni=0
    for genere in lista:
       numero_canzoni+=len(lista[genere])#linghezza della liste quindi numero di elementi 
    return numero_canzoni

def cercacanzone(lista,canzone_cercata):
    for genere in lista:
        for canzone in lista[genere]:# nel for bisongna mettere lista generi non posso ciclare su generi 
            if canzone.lower() == canzone_cercata.lower():
                return genere
    return None

def unisciPlaylist(lista,genere1,genere2):
    new_playlist=[]
    for genere in lista:
        if (genere ==genere1) or (genere ==genere2):
            for canzone in lista[genere]:
                new_playlist.append(canzone)
    return new_playlist

def main():

    playlist = {
    "Rock": ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"],
    "Pop": ["Thriller", "Like a Prayer", "Billie Jean"],
    "Relax": ["Hotel California", "Imagine", "Let It Be"]
    }
    n=contaCanzoni(playlist)
    print(n)
    print(cercacanzone(playlist,"Billie Jean"))
    print(unisciPlaylist(playlist,"Rock","Pop"))

if __name__=="__main__":
    main()