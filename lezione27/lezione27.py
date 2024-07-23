def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
    for key, value in dizionario.items():
        if dizionario[key] == valore:
            return key
        else:
            pass
    return None


print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 200))
print(trova_chiave_per_valore({'k1': 'v1', 'k2': 'v2'}, 'v3'))


def classifica_numeri(lista: int) -> dict[str:list[int]]:
    pari: list = []
    dispari: list = []
    dizionario: dict[str:list[int]] = {"pari": pari,
                                    "dispari": dispari}
    for elem in lista:
        if elem % 2 == 0:
            pari.append(elem)
            dizionario.update({"pari": pari})
        else:
            dispari.append(elem)
            dizionario.update({"dispari": dispari})
    return dizionario

print(classifica_numeri([1, 2, 3, 4, 5, 6]))
print(classifica_numeri([]))


class Movie:

    def __init__(self, movie_id: str, title: str, director: str) -> None:
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = False

    def rent(self):
        if self.is_rented == False:
            self.is_rented = True
        else:
            print(f"Il film {self.title} è già noleggiato.")

    def return_movie(self):
        if self.is_rented == True:
            self.is_rented = False
        else:
            print(f"Il film {self.title} non è attualmente noleggiato.")

class Customer:

    def __init__(self, costumer_id: str, name: str) -> None:
        self.costumer_id = costumer_id
        self.name = name
        self.rented_movies: list[Movie] = []        

    def rent_movie(self, movie: Movie):
        if movie in self.rented_movies:
            print(f"Il film {movie.title} è già noleggiato.")
        else:
            self.rented_movies.append(movie)
            movie.rent()

    def return_movie(self, movie: Movie):
        if movie in self.rented_movies:
            self.rented_movies.remove(movie)
            movie.return_movie()
        else:
            print(f"Il film {movie.title} non è stato noleggiato da questo cliente.")

class VideoRentalStore:

    def __init__(self) -> None:
        self.movies: dict[str, Movie] = {}
        self.customers: dict[str, Customer] = {}

    def add_movie(self, movie_id: str, title: str, director: str):
        key = list(self.movies.keys())
        if movie_id in key:
                print(f"Il film con ID {movie_id} esiste già.")
        else:
            movie = Movie(movie_id, title, director)
            self.movies.update({movie_id: movie})


    def register_customer(self, customer_id: str, name: str):
        key = list(self.customers.keys())
        if customer_id in key:
                print(f"Il cliente con ID {customer_id} è già registrato.")
        else:
            customer = Customer(customer_id, name)
            self.customers.update({customer_id: customer})

    def rent_movie(self, customer_id: str, movie_id: str):
        movie_keys = list(self.movies.keys())
        customer_keys = list(self.customers.keys())
        if customer_id in customer_keys and movie_id in movie_keys:
            movie: Movie = self.movies.get(movie_id)
            customer: Customer = self.customers.get(customer_id)
            customer.rent_movie(movie)
        else:
            print("Cliente o film non trovato.")

    def return_movie(self, customer_id: str, movie_id: str):
        movie_keys = list(self.movies.keys())
        customer_keys = list(self.customers.keys())
        if customer_id in customer_keys and movie_id in movie_keys:
            movie: Movie = self.movies.get(movie_id)
            customer: Customer = self.customers.get(customer_id)
            customer.return_movie(movie)
        else:
            print("Cliente o film non trovato.")
        
    def get_rented_movies(self, customer_id: str) -> list[Movie]:
        customer_keys = list(self.customers.keys())
        if customer_id in customer_keys:
            customer: Customer = self.customers.get(customer_id)
            return customer.rented_movies
        else:
            print("Cliente non trovato.")
            return []

# Creazione di un nuovo videonoleggio
videonoleggio = VideoRentalStore()

# Aggiunta di nuovi film
videonoleggio.add_movie("1", "Inception", "Christopher Nolan")
videonoleggio.add_movie("2", "The Matrix", "Wachowski Brothers")

# Registrazione di nuovi clienti
videonoleggio.register_customer("101", "Alice")
videonoleggio.register_customer("102", "Bob")

# Noleggio di film
videonoleggio.rent_movie("101", "1")
videonoleggio.rent_movie("102", "2")

# Tentativo di noleggiare un film già noleggiato
videonoleggio.rent_movie("101", "1")

# Restituzione di film
videonoleggio.return_movie("101", "1")

# Tentativo di restituire un film non noleggiato
videonoleggio.return_movie("101", "1")

# Ottenere la lista dei film noleggiati da un cliente
rented_movies_alice = videonoleggio.get_rented_movies("101")
print(f"Film noleggiati da Alice: {[movie.title for movie in rented_movies_alice]}")

rented_movies_bob = videonoleggio.get_rented_movies("102")
print(f"Film noleggiati da Bob: {[movie.title for movie in rented_movies_bob]}")

def print_seq(): 
    
    print("Sequenza a):")
    for i in range(1, 8, 1):
        print(f"{i}") 
    print ()

    print("Sequenza b):")
    for i in range(3, 25, 5):
        print(f"{i}")
    print ()
    
    print("Sequenza c):")
    for i in range(20, -11, -6):
        print(f"{i}")  
    print ()

    print("Sequenza d):")
    for i in range(19, 52, 8):
        print(f"{i}") 
    print ()
    
    return



def check_access(username: str, password: str, is_active: bool) -> str:
    if username == "admin" and password == "12345" and is_active == True:
        return "Accesso consentito"
    else:
        return "Accesso negato"
    


"""Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare, e cercare ricette basate sugli ingredienti.
Il sistema dovrà essere capace di gestire una collezione (dizionario) di ricette e i loro ingredienti.

Classe:
- RecipeManager:
    Gestisce tutte le operazioni legate alle ricette.

    Metodi:
    - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. Restituisce un nuovo dizionario con la sola ricetta appena creata o 
un messaggio di errore se la ricetta esiste già.

    - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.

    - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o 
la ricetta non esiste.

    - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di
errore se l'ingrediente non è presente o la ricetta non esiste.

    - list_recipes(): Elenca tutte le ricette esistenti.

    - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.

    - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. Restituisce un elenco di ricette o un messaggio di errore se nessuna
ricetta contiene l'ingrediente.

class RecipeManager:
"""


def sum_above_threshold(numbers: list[int], threshold: int) -> int:
    result: int = 0
    for elem in numbers:
        if elem > threshold:
            result += elem
    return result


def transform(x: int) -> int:
    if x % 2 == 0:
        x = x / 2
    else: 
        x = x * 3 - 1
    return x


def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if (conditionA == True) or (conditionB == True and conditionC == True):
        return "Operazione permessa"
    else:
        return "Operazione negata"
    


def frequency_dict(elements: list) -> dict:
    dizionario = {}
    key = list(dizionario.keys())
    for elem in elements:
        if elem not in key:
            dizionario.update({elem: 1})
        else:
            for key, value in dizionario.items():
                if elem == key:
                    dizionario.update({key: value + 1})
    return dizionario

print(frequency_dict(['mela', 'banana', 'mela']))