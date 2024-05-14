#1. Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.

    #3. Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. I recinti possono contenere uno o più animali. 
        #I recinti possono hanno gli attributi area, temperature e habitat.

        #2. Animal: questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi: name, species, age, height, width, preferred_habitat, health che è uguale a round(100 * (1 / age), 3).

    #4. ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo. I guardiani dello zoo hanno un nome, un cognome, e un id. 
        #Essi possono nutrire gli animali, pulire i recinti e svolgere altri compiti nel nostro zoo virtuale.

#Funzionalità:

#1. add_animal(animal: Animal, fence: Fence) (Aggiungi nuovo animale): consente al guardiano dello zoo di aggiungere un nuovo animale allo zoo. L'animale deve essere collocato 
    #in un recinto adeguato in base alle esigenze del suo habitat e se c'è ancora spazio nel recinto, ovvero se l'area del recinto è ancora sufficiente per ospitare questo animale.

#2. remove_animal(animal: Animal, fence: Fence) (Rimuovi animale): consente al guardiano dello zoo di rimuovere un animale dallo zoo. L'animale deve essere allontanato dal suo recinto. 
    #Nota bene: L'area del recinto deve essere ripristinata dello spazio che l'animale rimosso occupava.

#3. feed(animal: Animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano dello zoo di nutrire tutti gli animali dello zoo. 
    #Ogni volta che un animale viene nutrito, la sua salute incrementa di 1% rispetto alla sua salute corrente, ma le dimensioni dell'animale (height e width) vengono incrementate del 2%. 
    #Perciò, l'animale si può nutrire soltanto se il recinto ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo.

#4. clean(fence: Fence) (Pulizia dei recinti): implementare un metodo che consenta al guardiano dello zoo di pulire tutti i recinti dello zoo. 
    #Questo metodo restituisce un valore di tipo float che indica il tempo che il guardiano impiega per pulire il recinto. 
    #Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. Se l'area residua è pari a 0, restituire l'area occupata.

#5. describe_zoo() (Visualizza informazioni sullo zoo): visualizza informazioni su tutti i guardani dello zoo, sui recinti dello zoo che contengono animali. 
    #Fra un recinto e l'altro mettete 30 volte il carattere #

class Zoo:

    def __init__(self, fences, zoo_keepers):
        self.fences = fences
        self.zoo_keepers = zoo_keepers

    def describe_zoo(self) -> str:
        print("Zookepers:")
        for zookeeper in self.zoo_keepers: 
            print(f"ZooKeeper(name={zookeeper.name}, surname={zookeeper.surname}, id={zookeeper.id})")
        print("Fences:")
        for fence in self.fences:
            print(f"Fence(area={fence.area}, temperature={fence.temperature}, habitat={fence.habitat})")
            print("with animals:")
            for animal in fence.animals:
                print(f"Animal(name={animal.name}, species={animal.species}, age={animal.age})")
            print("#" * 30)

    class ZooKeeper:

        def __init__(self, name: str, surname: str, id: int):
            self.name: str = name
            self.surname: str = surname
            self.id: str = str(id)

        def __str__(self) -> str:
            return f"name = {self.name}, surname = {self.surname}, id = {self.id}"

        class Fence:

            def __init__(self, area: int, temperature: float, habitat: str):
                self.area: int = area
                self.temperature: float = temperature
                self.habitat: str = habitat
                self.list_of_animals: list[str] = []
                self.residual_area: float = area

            def __str__(self) -> str:
                return f"area = {self.area}, temperature = {self.temperature}, habitat = {self.habitat}"

        class Animal:

            def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: str):
                self.name: str = name
                self.species: str = species 
                self.age: int = age
                self.height: float = height
                self.width: float = width
                self.habitat: str = preferred_habitat
                self.health: float = round(100 * (1/age), 3)
                self.area: float = self.height * self.width
                self.fence = None

            def __str__(self) -> str:
                return f"name = {self.name}, species = {self.species}, age = {self.age}"

        def add_animal(self, animal: Animal, fence: Fence):
            if animal.habitat == fence.habitat:
                if fence.residual_area >= animal.height * animal.width:
                    fence.list_of_animals.append(animal)
                    fence.residual_area -= (animal.width * animal.height)
                    animal.fence = fence

        def remove_animal(self, animal: Animal, fence: Fence):
            if animal in fence:
                fence.remove(animal)
                fence.residual_area += animal.width * animal.height

        def feed(self, animal: Animal): 
            increased_height: float = animal.height + ((2/100) * animal.height)
            increased_width: float = animal.width + ((2/100) * animal.width)
            animal_area_increase: int = animal.area - (increased_height * increased_width)
            if animal_area_increase <= animal.fence.residual_area:
                animal.height = increased_height
                animal.width = increased_width
                animal.fence.residual_area -= animal_area_increase

        def clean(self, fence: Fence):
            time: float = 0
            if fence.residual_area > 0:
                time = (fence.area - fence.residual_area) / fence.residual_area
            return time


prima = Zoo.ZooKeeper.Fence(100, 25, "Continent")
lorenzo = Zoo.ZooKeeper("Lorenzo", "Maggi", 1234)
scoiattolo = Zoo.ZooKeeper.Animal("Scoiattolo", "Blabla", 25, 15, 3, "Continent")

lorenzo.add_animal(animal = scoiattolo, fence = prima)
