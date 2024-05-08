#1. Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.

    #3. Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. I recinti possono contenere uno o più animali. 
        #I recinti possono hanno gli attributi area, temperature e habitat.

        #2. Animal: questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi: name, species, age, height, width, preferred_habitat, health che è uguale a 100 * (1 / age).

    #4. ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo. I guardiani dello zoo hanno un nome, un cognome, e una matricola. 
        #Essi possono nutrire gli animali, pulire i recinti e svolgere altri compiti nel nostro zoo virtuale.

#Funzionalità:

#1. add_animal(animals: list[Animal], fence: Fence) (Aggiungi nuovo animale): consente al guardiano dello zoo di aggiungere un nuovo animale allo zoo. L'animale deve essere collocato 
    #in un recinto adeguato in base alle esigenze del suo habitat e se c'è ancora spazio nel recinto, ovvero se l'area del recinto è ancora sufficiente per ospitare questo animale.

#2. remove_animal(animal: Animal) (Rimuovi animale): consente al guardiano dello zoo di rimuovere un animale dallo zoo. L'animale deve essere allontanato dal suo recinto. 
    #Nota bene: L'area del recinto deve essere ripristinata dello spazio che l'animale rimosso occupava.

#3. feed(animal: Animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano dello zoo di nutrire tutti gli animali dello zoo. 
    #Ogni volta che un animale viene nutrito, la sua salute incrementa di 1% rispetto alla sua salute corrente, ma le dimensioni dell'animale (height e width) vengono incrementate del 2%. 
    #Perciò, l'animale si può nutrire soltanto se il recinto ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo.

#4. clean(fence: Fence) (Pulizia dei recinti): implementare un metodo che consenta al guardiano dello zoo di pulire tutti i recinti dello zoo. 
    #Questo metodo restituisce un valore di tipo float che indica il tempo che il guardiano impiega per pulire il recinto. 
    #Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto.

#5. describe_zoo() (Visualizza informazioni sullo zoo): visualizza informazioni su tutti i guardani dello zoo, sui recinti dello zoo che contengono animali. 
    #Fra un recinto e l'altro mettete 30 volte il carattere #

#Metodi 3 e 4 sono esclusivi dello zookeper


class Zoo:

    class Zookeper:

        def __init__(self, name: str, surname: str, id: int) -> None:
            self.name = name
            self.surname = surname
            self.id = id

        def feed_animal(self):
            pass

        def clean(self):
            pass

    class Fence:

        def __init__(self, area: str, temperature: float, habitat: str) -> None:
            self.area = area
            self.temperature = temperature
            self.habitat = habitat

        class Animal:

            def __init__(self, name: str, species: str, age: int, height: int, width: int, habitat: str, health: int) -> None:
                self.name = name
                self.species = species 
                self.age = age
                self.height = height
                self.width = width
                self.habitat = habitat
                self.health = 100 * (1/age)

        @classmethod
        def addAnimal(cls, animal: Animal):
            pass

        def removeAnimal(cls, animal: Animal):
            pass

    @classmethod
    def describe_zoo(cls):
        pass

