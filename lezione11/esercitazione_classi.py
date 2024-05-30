"""Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. Il cinema ha diverse sale, ognuna con un diverso film in programmazione. 
Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.
 
Classi:
- Film: Rappresenta un film con titolo e durata.
 
- Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.

Metodi:
    - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.
    - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
- Cinema: Gestisce le operazioni legate alla gestione delle sale.

Metodi:
    - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
    - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.
"""

class Film:

    def __init__(self, titolo: str, durata: int):
        self.titolo: str = titolo
        self.durata: int = durata

    def __str__(self) -> str:
        return f"titolo: {self.titolo}, durata: {self.durata}"

class Sala:

    def __init__(self, numero: int, titolo_film: str, posti_totali: int):
        self.numero: int = numero
        self.titolo_film: str = titolo_film
        self.posti_totali: int = posti_totali
        self.posti_prenotati: int = 0

    def __str__(self) -> str:
        return f"numero sala: {self.numero}, titolo film: {self.titolo_film}, posti totali: {self.posti_totali}, posti disponibili: {self.posti_disponibili}"

    def prenota_posti(self, num_posti: int):
        if self.posti_prenotati < self.posti_totali:
            if num_posti <= (self.posti_totali - self.posti_prenotati):
                self.posti_prenotati += num_posti
                print("Prenotazione confermata")
        else:
            print("Posti non disponibili")

    def posti_disponibili(self):
        print(f"Posti disponibili: {self.posti_totali - self.posti_prenotati}")


class Cinema(Film, Sala):

    def __init__(self):
        self.sale: dict[str, Sala] = {}

    def aggiungi_sala(self, sala: Sala):
        self.nuova_sala = Sala(sala.numero, sala.titolo_film, sala.posti_totali)
        self.sale.update({sala.titolo_film: self.nuova_sala})

    def prenota_film(self, titolo_film: str, num_posti: int):
        if titolo_film in self.sale:
            self.sala: Sala = self.sale.get(titolo_film)
            self.sala.prenota_posti(num_posti)
    

"""
Test case:

    Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
    Un cliente sceglie un film e prenota un certo numero di posti.
    Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.
"""

sala_1: Sala = Sala(1, "Shrek", 56)
print(sala_1)
sala_1.prenota_posti(15)
sala_1.posti_disponibili()



"""Gestione di un magazzino
Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere di aggiungere prodotti al magazzino, 
cercare prodotti per nome e verificare la disponibilità di un prodotto.

Definisci una classe Prodotto con i seguenti attributi:
- nome (stringa)
- quantità (intero)
 
Definisci una classe Magazzino con i seguenti metodi:
- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
"""

class Prodotto:

    def __init__(self, nome: str, quantità: int):
        self.nome: str = nome
        self.quantità: int = quantità

class Magazzino(Prodotto):

    def __init__(self):
        self.prodotti: dict[str, Prodotto] = {}

    def aggiungi_prodotto(self, prodotto: Prodotto):
        nuovo_prodotto: Prodotto = Prodotto(prodotto.nome, prodotto.quantità)
        self.prodotti.update({nuovo_prodotto.nome: nuovo_prodotto})

    def cerca_prodotto(self, nome: str):
        if nome in self.prodotti:
            return "Il prodotto esiste"
        else:
            return "Il prodotto non esiste"

    def verifica_disponibilità(self, nome: str):
        if nome in self.prodotti:
            prodotto = self.prodotti.get(nome)
            return prodotto.quantità


"""Test case:
    Un gestore del magazzino crea un magazzino e diversi prodotti in diverse quantità. Successivamente, aggiunge i prodotti al magazzino.
    Il sistema cerca un prodotto per verificare se esiste nell'inventario.
    Il sistema verifica la disponibilità dei prodotti in inventario.
"""
magazzino: Magazzino = Magazzino()
prodotto_1 = Prodotto("shampoo", 50)
prodotto_2 = Prodotto("candegina", 34)
magazzino.aggiungi_prodotto(prodotto_1)
magazzino.aggiungi_prodotto(prodotto_2)

print(magazzino.cerca_prodotto("candegina"))
print(magazzino.verifica_disponibilità("shampoo"))