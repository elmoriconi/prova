"""# Testi Digitali

Si definisca una classe Documento che contenga una variabile di tipo stringa chiamata testo e che memorizza qualsiasi contenuto testuale per il documento.
    Si crei un metodo getText() che restituisca il testo. 
    Si crei un metodo setText() per impostare il testo. 
    Scrivere un metodo isInText() che restituisce True se un documento contiene la parola chiave specificata.

Si definisca poi una classe Email che sia derivata da Documento e che includa le variabili per il mittente, il destinatario e il titolo del messaggio.
    Si implementino i metodi get() e set() appropriati per tali variabili. Il corpo del messaggio dell’e-mail dovrebbe essere memorizzato nella variabile ereditata testo.
    Si ridefinisca il metodo getText() per concatenare e ritornare tutti i campi di testo (mittente, destinatario, titolo del messaggio, e messaggio) come di seguito:
 
        Da: alice@example.com, A: bob@example.com
        Titolo: Incontro
        Messaggio: Ciao Bob, possiamo incontrarci domani?
 
    Inoltre, si implementi un metodo writeToFile() per scrivere il risultato del metodo getText() in un file di testo e in un percorso specificato.
 
Analogamente, si definisca una classe File che sia derivata da Documento e includa una variabile per il nomePercorso.
Crea un file document.txt con all'interno la stringa "Questo e' il contenuto del file." e salvalo in una directory a tua scelta e che sarà indicata in nomePercorso.
I contenuti testuali del file dovrebbero essere letti da questo file di testo al percorso specificato in nomePercorso e memorizzati nella variabile ereditata testo tramite un metodo leggiTestoDaFile().
Si ridefinisca il metodo getText() che concateni e ritorni il nome del percorso e il testo, come di seguito:
 
Percorso: nomePercorso/document.txt
Contenuto: Questo e' il contenuto del file.

### Test con UnitTest

Utilizzando il modulo unittest, definire i seguenti test per le classi Documento, Email e File.
 
I test devono includere:

    Verifica dei metodi getText() e setText() nella classe Documento.
    Verifica del metodo isInText() nella classe Documento.
    Verifica del metodo getText() nella classe Email.
    Verifica del metodo writeToFile() nella classe Email.
    Verifica del metodo isInText() nella classe Email.
    Verifica del metodo getText() nella classe File.
    Verifica del metodo isInText() nella classe File.
"""

import os

class Documento: 

    def __init__(self, testo: str) -> None:
        self.testo: str = testo

    def getText(self) -> str:
        return self.testo

    def setText(self, testo: str) -> None:
        self.testo = testo

    def isIntText(self, parola: str) -> bool:
        if parola in self.testo:
            return True
        else:
            return False
        

class Email(Documento):

    def __init__(self, testo: str, mittente: str, destinatario: str, titolo: str) -> None:
        self.testo: str = self.writeToFile(testo)
        self.mittente: str = mittente
        self.destinatario: str = destinatario
        self.titolo: str = titolo

    def getMittente(self) -> str:
        return self.mittente
    
    def getDestinatario(self) -> str:
        return self.destinatario
    
    def getTitolo(self) -> str:
        return self.titolo
    
    def setMittente(self, mittente: str) -> None:
        self.mittente = mittente

    def setDestinatario(self, destinatario: str) -> None:
        self.destinatario = destinatario

    def setTitolo(self, titolo: str) -> None:
        self.titolo = titolo

    def getText(self) -> str:
        return f"Da: {self.getMittente()}, A: {self.getDestinatario()} \nTitolo: {self.getTitolo()} \nMessaggio: {self.testo()}"
    
    def writeToFile(self, directory) -> None:
        with open(directory, "a") as reader: 
            testo = self.getText()
            reader.write(testo)

class File(Documento):

    def __init__(self, testo: str, nomePercorso: str) -> None:
        super().__init__(testo)
        self.nomePercorso = nomePercorso
        self.createDirectory(nomePercorso)

    def createDirectory(self, nomePercorso: str) -> None:
        if not os.path.isdir(nomePercorso):
            os.mkdir(nomePercorso)
            self.createFile(nomePercorso)
        else:
            print("Directory already exists")

    def createFile(self, nomePercorso: str) -> str:
        with open(f"{nomePercorso}/document.txt", "a") as reader:
            reader.write(self.testo)
        return "document.txt"
    
    def leggiTestoDaFile(self) -> None:
        with open(f"{self.nomePercorso}/document.txt", "r") as reader:
            self.testo = reader.read()

    def getText(self) -> str:
        f"Percorso: {self.nomePercorso}/document.txt \nContenuto: {self.testo}"

"""### Test tramite codice driver:
Creazione degli oggetti:

    Email: Viene creato un oggetto Email con mittente, destinatario, oggetto e corpo del messaggio.
    File: Viene creato un oggetto File specificando il percorso di un file esistente.

Prova dei metodi:

    Stampa del testo dell'email: Viene stampato il testo del messaggio dell'email utilizzando il metodo getText().
    Stampa del testo del file: Viene stampato il contenuto del file utilizzando il metodo getText().

Scrittura del contenuto dell'email su un file:

    Scrittura su file: Il contenuto dell'email viene scritto su un nuovo file chiamato email1.txt utilizzando il metodo writeToFile().

Verifica della presenza di parole chiave:

    Email: Utilizzo del metodo isInText() per verificare se la parola 'incontrarci' è presente nel testo dell'email. Il risultato atteso è True.
    File: Utilizzo del metodo isInText() per verificare se la parola 'percorso' è presente nel testo del file. Il risultato atteso è False.
"""

email: Email = Email("Ciao Bob, possiamo incontrarci domani?", "alice@example.com", "bob@example.com", "Incontro")
file: File = File("Questo è il contenuto del file: \n", "esempiomdycr4f")
print(email.getText())
print(file.getText())