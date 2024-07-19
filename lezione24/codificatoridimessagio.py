"""# Codificatori Messaggio
Si crei una classe astratta chiamata CodificatoreMessaggio che ha un solo metodo astratto codifica(testoInChiaro), dove testoInChiaro sarà il messaggio da codificare. Il metodo restituirà il messaggio codificato.

Si crei una classe astratta chiamata DecodificatoreMessaggio che abbia un solo metodo decodifica(testoCodificato), dove testoCodificato sarà il messaggio da decodificare. 
Il metodo ritornerà il messaggio decodificato.

Si crei una classe CifratoreAScorrimento che implementa le classi astratte CodificatoreMessaggio e DecodificatoreMessaggio. Il costruttore dovrebbe ricevere un numero intero chiamato chiave. 
Si definisca il metodo codifica(testoInChiaro) così che ogni lettera del testo sia spostata dal valore contenuto in chiave.
Per esempio, se chiave è uguale a 3, la lettera 'a' sarà sostituita da 'd', la lettera 'b' sarà sostituita da 'e', la lettera 'c' sarà sostituita da 'f' e così via.

     Suggerimento: si potrebbe definire un metodo privato sposta_carattere(c) che restituisca la codifica di un singolo carattere c da concatenare agli altri per costruire il messaggio codificato 
     nel metodo codifica(testoInChiaro).

Si crei una classe CifratoreACombinazione che implementa le classi astratte CodificatoreMessaggio e DecodificatoreMessaggio. Il costruttore dovrebbe ricevere un numero intero chiamato n. 
Si definisca il metodo codifica(testoInChiaro) così che il messaggio sia combinato n volte. Per eseguire una singola combinazione, si divide il messaggio a metà e poi si prendono i caratteri 
da ognuna delle metà in modo alternato. Per esempio, se il messaggio è 'abcdefghi', le metà sono 'abcde' e 'fghi' (nel caso in cui la lunghezza del testo da decifrare sia un numero dispari, 
la prima metà deve essere più lunga della seconda metà). Il messaggio combinato è 'afbgchdie'.

    Suggerimento: si potrebbe definire un metodo privato combinazione(testo) che esegue la combinazione del testo e ritorni il testo cifrato da usare nel metodo codifica(testoInChiaro).

Si scriva il metodo decodifica(testoCodificato) per ognuna delle classi CifrarioAScorrimento e CifrarioACombinazione.

    Suggerimento: definire il metodo privato decodifica_carattere() per la classe CifrarioAScorrimento che compie un'azione inversa al metodo sposta_carattere().

    Suggerimento: definire il metodo privato decodifica_combinazione() per la classe CifrarioACombinazione che compie un'azione inversa al metodo combinazione().


Infine, si implementi anche un metodo per leggere il testo da cifrare da un file e un metodo per scrivere il testo cifrato su un file per entrambe le classi CifratoreAScorrimento e CifratoreACombinazione."""

from abc import ABC, abstractmethod

class CodificatoreMessaggio(ABC):

    @abstractmethod
    def codifica(testoInChiaro: str) -> str:
        pass

class DecodificatoreMessaggio(ABC):

    @abstractmethod
    def decodifica(testoCodificato: str) -> str:
        pass

class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):

    def __init__(self, chiave: int) -> None:
        super().__init__()
        self.chiave: int = chiave

    def codifica(self, testoInChiaro: str) -> str:
        testoInChiaro = testoInChiaro.lower()
        alfabeto_numeri: dict[str, int] = {"a": 1, "b": 2, "c": 3,
                                    "d": 4, "e": 5, "f": 6,
                                    "g": 7, "h": 8, "i": 9,
                                    "j": 10, "k": 11, "l": 12,
                                    "m": 13, "n": 14, "o": 15,
                                    "p": 16, "q": 17, "r": 18,
                                    "s": 19, "t": 20, "u": 21,
                                    "v": 22, "w": 23, "x": 24,
                                    "y": 25, "z": 26}
        numeri_alfabeto: dict[str, int] = {1: "a", 2: "b", 3: "c",
                                    4: "d", 5: "e", 6: "f",
                                    7: "g", 8: "h", 9: "i",
                                    10: "j", 11: "k", 12: "l",
                                    13: "m", 14: "n", 15: "o",
                                    16: "p", 17: "q", 18: "r",
                                    19: "s", 20: "t", 21: "u",
                                    22: "v", 23: "w", 24: "x",
                                    25: "y", 26: "z"}
        mess_cifrato: str = ""
        for char in testoInChiaro:
            if char.isalpha():
                numero: int = alfabeto_numeri[char]
                nuova_posizione: int = numero + self.chiave
                mess_cifrato += numeri_alfabeto[nuova_posizione]
            else:
                mess_cifrato += char
        return mess_cifrato
    
    def decodifica(self, testoCodificato: str) -> str:
        mess_decifrato: str = ""
        alfabeto_numeri: dict[str, int] = {"a": 1, "b": 2, "c": 3,
                                    "d": 4, "e": 5, "f": 6,
                                    "g": 7, "h": 8, "i": 9,
                                    "j": 10, "k": 11, "l": 12,
                                    "m": 13, "n": 14, "o": 15,
                                    "p": 16, "q": 17, "r": 18,
                                    "s": 19, "t": 20, "u": 21,
                                    "v": 22, "w": 23, "x": 24,
                                    "y": 25, "z": 26}
        numeri_alfabeto: dict[str, int] = {1: "a", 2: "b", 3: "c",
                                    4: "d", 5: "e", 6: "f",
                                    7: "g", 8: "h", 9: "i",
                                    10: "j", 11: "k", 12: "l",
                                    13: "m", 14: "n", 15: "o",
                                    16: "p", 17: "q", 18: "r",
                                    19: "s", 20: "t", 21: "u",
                                    22: "v", 23: "w", 24: "x",
                                    25: "y", 26: "z"}
        for char in testoCodificato:
            if char.isalpha():
                numero: int = alfabeto_numeri[char]
                nuova_posizione: int = numero - self.chiave
                mess_decifrato += numeri_alfabeto[nuova_posizione]
            else:
                mess_decifrato += char
        return mess_decifrato        

class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):

    def __init__(self, n: int) -> None:
        super().__init__()
        self.n = n

    def codifica(self, testoInChiaro: str) -> str:
        sinistra: str = testoInChiaro[0:len(testoInChiaro)//2]
        destra: str = testoInChiaro[len(testoInChiaro)//2:]
        mess_cifrato: str = ""
        i: int = 0
        j: int = 0
        while i < len(sinistra) and j < len(destra):
            mess_cifrato += sinistra[i]
            mess_cifrato += destra[j]
            i += 1
            j += 1
        return mess_cifrato
            
    def decodifica(self, testoCodificato: str) -> str:
        i: int = 0
        sinistra: str = ""
        destra: str = ""
        while i < len(testoCodificato):
            if i % 2 == 0:
                destra += testoCodificato[i]
                i += 1
            else:
                sinistra += testoCodificato[i]
                i += 1
        mess_decifrato: str = destra + sinistra
        return mess_decifrato



filippino: CifratoreAScorrimento = CifratoreAScorrimento(3)
print(filippino.codifica("Ciao, come stai?")) 
print(filippino.decodifica("fldr, frph vwdl?"))
filippino2: CifratoreACombinazione = CifratoreACombinazione(5)
print(filippino2.codifica("Ciao, come stai?")) 
print(filippino2.decodifica("Cmiea os,t acio?"))


"""### Test tramite codice driver:
Test del Cifratore a Scorrimento:
- Inizializzazione: Viene creato un oggetto CifratoreAScorrimento con una chiave di scorrimento di 3.
- Lettura del testo: Il testo in chiaro viene letto da un file.
- Codifica: Il testo in chiaro viene codificato utilizzando il cifratore a scorrimento.
- Scrittura del testo codificato: Il testo codificato viene scritto su un file.
- Stampa del testo codificato: Il testo codificato viene stampato.
- Decodifica: Il testo codificato viene decodificato.
- Stampa del testo decodificato: Il testo decodificato viene stampato."""

"""###Test del Cifratore a Combinazione:
- Inizializzazione: Viene creato un oggetto CifratoreACombinazione con 3 combinazioni.
- Lettura del testo: Il testo in chiaro viene letto da un file.
- Codifica: Il testo in chiaro viene codificato utilizzando il cifratore a combinazione.
- Scrittura del testo codificato: Il testo codificato viene scritto su un file.
- Stampa del testo codificato: Il testo codificato viene stampato.
- Decodifica: Il testo codificato viene decodificato.
- Stampa del testo decodificato: Il testo decodificato viene stampato."""