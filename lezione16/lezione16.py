"""
Obiettivo:
Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) e una classe derivata Film che rappresenti specificamente un film. 
Gli studenti dovranno anche creare oggetti di queste classi, aggiungere valutazioni e visualizzare le recensioni.

Specifiche della Classe Media:
 
Attributi:
- title (stringa): Il titolo del media.
- reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5, dove 1=Terribile, 2=Brutto, 3=Normale, 4=Bello, 5=Grandioso.

Metodi:
- set_title(self, title): Imposta il titolo del media.
- get_title(self): Restituisce il titolo del media.
- aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
- getMedia(self): Calcola e restituisce la media delle valutazioni.
- getRate(self): Restituisce una stringa che descrive il giudizio medio basato sulla media delle valutazioni, ovvero mostra "Terribile" se il voto medio si avvicina a 1, 
  "Brutto" se il voto medio si avvicina a 2, "Normale" se il voto medio si avvicina a 3, "Bello" se il voto medio si avvicina a 4, "Grandioso" se il voto medio si avvicina a 5.
- ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
- recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, il voto medio, il giudizio e le percentuali di ciascun voto. Esempio di riassunto:
 
Titolo del Film: The Shawshank Redemption
Voto Medio: 3.80
Giudizio: Bello
Terribile: 10.00%
Brutto: 10.00%
Normale: 10.00%
Bello: 30.00%
Grandioso: 40.00%

Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film, aggiunga a ognuno dei due almeno dieci valutazioni e richiami il metodo recensione().
"""

class Media:

    def __init__(self):
        self.title: None|str = None
        self.reviews: None|list[int] = []

    def set_title(self, title: str):
        self.title = title

    def get_title(self):
        return self.title       

    def aggiungiValutazione(self, voto: int):
        if 1 <= voto <= 5:
            self.reviews.append(voto)

    def getMedia(self):
        somma = sum(self.reviews)
        media = somma/len(self.reviews)
        return media
    
    def getRate(self):
        media = self.getMedia()
        if media <= 1:
            return "Terribile"
        elif media <= 2:
            return "Brutto"
        elif media <= 3:
            return "Normale"
        elif media <= 4:
            return "Bello"
        elif media <= 5:
            return "Grandioso"

    def ratePercentage(self, voto: int):
        quantità: int = 0
        for elem in self.reviews:
            if elem == voto:
                quantità += 1
        percentage: float = (quantità * 100)/len(self.reviews)
        return percentage

    def recensione(self):
        recensioni: list[str] = ["Zero", "Terribile", "Brutto", "Normale", "Bello", "Grandioso"]
        testo: str = f"Titolo del Film: {self.title} \n" 
        testo += f"Voto Medio: {self.getMedia()} \n"
        testo += f"Giudizio: {self.getRate()} \n"
        for elem in range(1, 6):
            testo += f"{recensioni[elem]}: {self.ratePercentage(elem)}% \n"
        return testo 

    def __str__(self) -> str:
        return f"{self.title}"

class Film(Media):

    def __init__(self):
        super().__init__()

media1: Media = Media()
media1.set_title("Lo Squalo")
print(media1.get_title())
media1.aggiungiValutazione(5)
media1.aggiungiValutazione(1)
media1.aggiungiValutazione(3)
media1.aggiungiValutazione(5)
media1.aggiungiValutazione(4)
media1.aggiungiValutazione(3)
media1.aggiungiValutazione(4)
media1.aggiungiValutazione(3)
print(media1.getMedia())
print(media1.ratePercentage(5))
print(media1.recensione())

