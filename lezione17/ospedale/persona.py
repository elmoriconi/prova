"""### CLASSE: Persona

Creare un file chiamato "persona.py". In tale file, definire una classe chiamata Persona. Tale classe deve avere due attributi privati di tipo String, uno per il nome ed uno per il cognome, 
ed un attributo privato di tipo int per l'età.

- La classe Persona deve avere i seguenti metodi:

        -init(first_name, last_name). Tale metodo, deve verificare che first_name, last_name siano stringhe; in caso negativo, impostare a None l'attributo che non risulta essere una stringa, 
    stampando un messaggio di errore, ad esempio, "Il nome inserito non è una stringa!". Se first_name e last_name sono due stringhe, assegnare 0 all'attributo relativo all'età di una persona; 
    se first_name e last_name non sono due stringhe, allora assegnare None all'età.
        -setName(first_name): consente di impostare il nome di una persona, modificando il valore del relativo attributo. Il valore viene modificato se e solo se viene passata al metodo una stringa. 
    In caso contrario, stampare un messaggio di errore, ad esempio "Il nome inserito non è una stringa!".
        -setLastName(last_name): consente di impostare il cognome di una persona, modificando il valore del relativo attributo. 
    Il valore viene modificato se e solo se viene passata al metodo una stringa. In caso contrario, stampare un messaggio di errore, ad esempio "Il cognome inserito non è una stringa!".
        -setAge(age): consente di impostare l'età di una persona, modificando il valore del relativo attributo. Il valore viene modificato se e solo se viene passato al metodo un numero intero. 
    In caso contrario, stampare un messaggio di errore, ad esempio "L'età deve essere un numero intero!".
        -getName(): consente di ritornare il nome di una persona.
        -getLastname(): consente di ritornare il cognome di una persona.
        -getAge(): consente di ritornare l'età di una persona.
        -greet(): stampa il seguente saluto "Ciao, sono {nome} {cognome}! Ho {età} anni!"
"""

class Persona:

    def __init__(self, nome: str, cognome: str):
        if type(nome) == str:
            self.__nome = nome
        else:
            self.__nome = None
            raise ValueError("Il nome inserito non è una stringa!")
        if type(cognome) == str:
            self.__cognome = cognome
        else:
            self.__cognome = None
            raise ValueError("Il cognome inserito non è una stringa!")
        if type(self.__nome) and type(self.__cognome) == str:
            self.__età = 0
        else:
            self.__età = None

    def setName(self, nome: str):
        if type(nome) == str:
            self.__nome = nome
        else:
            raise ValueError("Il nome inserito non è una stringa!")
        return self.__nome
    
    def setLastName(self, cognome: str):
        if type(cognome) == str:
            self.__cognome = cognome
        else:
            raise ValueError("Il cognome inserito non è una stringa!")
        return self.__cognome
    
    def setAge(self, età: int):
        if type(età) == int:
            self.__età = età
        else:
            raise ValueError("L'età deve essere un numero intero!")
        return self.__età
    
    def getName(self):
        return self.__nome
    
    def getLastName(self):
        return self.__cognome
    
    def getAge(self):
        return self.__età
    
    def greet(self):
        return f"Ciao, sono {self.getName()} {self.getLastName()}! Ho {self.getAge()} anni!"