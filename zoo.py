#1. Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti e dei guardiani dello zoo.

    #3. Recinto: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. I recinti possono contenere uno o più animali. 
        #I recinti hanno gli attributi dimensioni, temperatura e tipo di habitat.

        #2. Animale: questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi: nome, specie, età.

    #4. ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo. I guardiani dello zoo possono nutrire gli animali, 
        #pulire i recinti e svolgere altri compiti.

#Funzionalità:

#1. add_animal(animal) (Aggiungi nuovo animale): consente al guardiano dello zoo di aggiungere un nuovo animale allo zoo. 
    #L'animale deve essere collocato in un recinto adeguato in base alle esigenze della sua specie e del suo habitat.

#2. remove_animal(animal) (Rimuovi animale): consente al guardiano dello zoo di rimuovere un animale dallo zoo. L'animale deve essere allontanato dal suo recinto.

#3. feed(animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano dello zoo di nutrire tutti gli animali dello zoo. 
    #Ogni animale può avere esigenze dietetiche diverse.
    #Esclusivo dello zookeeper

#4. clean(recinto) (Pulizia dei recinti): implementare un metodo che consenta al guardiano dello zoo di pulire tutti i recinti dello zoo. 
    #Il processo di pulizia può variare a seconda del tipo di recinto e degli animali che contiene.
    #Esclusivo dello zookeper

#5. describe_zoo() (Visualizza informazioni sullo zoo): visualizza informazioni su tutti gli animali e i recinti dello zoo, incluso il loro stato attuale e tutti i dettagli rilevanti.

class Zoo:

    class Zookeper:

        def __init__(self) -> None:
            pass

        def feed_animal(self):
            pass

        def clean(self):
            pass

    class Recinto:

        def __init__(self, dimensioni: str, temperatura: float, habitat: str) -> None:
            self.dimensioni = dimensioni
            self.temperatura = temperatura
            self.habitat = habitat

        class Animale:

            def __init__(self, nome: str, specie: str, età: int) -> None:
                self.nome = nome
                self.specie = specie 
                self.età = età

            def addAnimal(self, animal: str):
                pass

            def removeAnimal(self, animal: int):
                pass

    @classmethod
    def describe_zoo(cls):
        pass