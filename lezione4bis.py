def subtract_all(x: list[float], y: float) -> list[float]:
    result: list[float] = []
    for elem in x:
        z: float = elem - y
        result.append(z)
    return result

x: list[float] = [1,2,3,4,5]
y: float = 5
result: list[float] = subtract_all(x, y)
print(result)

def suBtract_all2(x: list[float], y: list[float]) -> list[float]:
    result: list[float] = []
    for i in range(len(x)):
        z: float = x[i] - y[i]
        result.append(z)
    return result

a: list[float] = [1,2,3,4,5]
b: list[float] = [2,3,4,5,6]
result2: list[float] = suBtract_all2(a, b)
print(result2)

def suBtract_all3(x: list[float], y: list[float]) -> list[float]:
    result: list[float] = []
    if len(x) >= len(y):
        for i in range(len(y)):
            z: float = x[i] - y[i]
        result.append(z)
    else:
        for i in range(len(x)):
            z: float = x[i] - y[i]
            result.append(z)
    return result

c: list[float] = [1,2,3,4,5]
d: list[float] = [2,3,4,5,6,7]
result3: list[float] = suBtract_all3(c, d)
print(result3)

#Set: 

def counter(s: str) -> list[int]:
    result: list[int] = []
    caratteri: int = len(s)
    result.append(caratteri)
    parole: int = len(s.split(" "))
    result.append(parole) 
    parole_distinte: set[str] = set(s.split())
    numero_parole_distinte: int = len(parole_distinte)
    result.append(numero_parole_distinte)
    frasi: int = len(s.split("."))-1
    result.append(frasi)
    return(result)
    """
    Questa funzione prende una stringa in input e restituisce una lista costruita nel modo seguente:
        - il primo elemento della lista contiene il numero di caratteri nela stringa
        - il secondo elemento della lista contiene il numero di parole nella stringa
        - il secondo elemento della lista contiene il numero di parole distinte nella stringa
        - il quarto elemento della lista contiene il numero di frasi nella stringa
    """


prova: str = "Oggi mi sono svegliata alle sette. Oggi andrò a lezione. Oggi ti sei svegliata alle sette."
s: str = "La meccanica quantistica è la teoria fisica che descrive il comportamento della materia, della radiazione e le reciproche interazioni, con particolare riguardo ai fenomeni caratteristici della scala di lunghezza o di energia atomica e subatomica, dove le precedenti teorie classiche risultano inadeguate. Come caratteristica fondamentale, la meccanica quantistica descrive la radiazione e la materia sia come fenomeni ondulatori che come entità particellari, al contrario della meccanica classica, che descrive la luce solamente come un'onda e, ad esempio, l'elettrone solo come una particella. Questa inaspettata e controintuitiva proprietà della realtà fisica, chiamata dualismo onda-particella, è la principale ragione del fallimento delle teorie sviluppate fino al XIX secolo nella descrizione degli atomi e delle molecole. La relazione tra natura ondulatoria e corpuscolare è enunciata nel principio di complementarità e formalizzata nel principio di indeterminazione di Heisenberg. Esistono numerosi formalismi matematici equivalenti della teoria, come la meccanica ondulatoria e la meccanica delle matrici; al contrario, ne esistono numerose e discordanti interpretazioni riguardo all'essenza ultima del cosmo e della natura, che hanno dato vita a un dibattito tuttora aperto nell'ambito della filosofia della scienza. La meccanica quantistica rappresenta, assieme alla teoria della relatività, uno spartiacque rispetto alla fisica classica, portando alla nascita della fisica moderna. Attraverso la teoria quantistica dei campi, generalizzazione della formulazione originale che include il principio di relatività ristretta, essa è a fondamento di molte altre branche della fisica, come la fisica atomica, la fisica della materia condensata, la fisica nucleare, la fisica delle particelle, la chimica quantistica."
result: list[int] = counter(s)
print(result)

#Dizionari: 

def word_count(s: str) -> dict[str, int]:
    dictionary: dict[str, int] = {}
    parole: list[str] = list(s.split())
    for i in parole:
        if i not in dictionary:
            dictionary.update({i: 1})
        else:
            dictionary[i] += 1
    maggiore_di_uno: dict[str, int] = {}
    for key in dictionary:
        if dictionary[key] > 1:
            maggiore_di_uno.update({key: dictionary[key]})
    return dictionary, maggiore_di_uno

"""
    Questa funzione conta quante volte occorrono le parole dentro una stringa
"""

prova2: str = "Oggi mi sono svegliata alle sette. Oggi andrò a lezione. Oggi ti sei svegliata alle sette."
s2: str = "La meccanica quantistica è la teoria fisica che descrive il comportamento della materia, della radiazione e le reciproche interazioni, con particolare riguardo ai fenomeni caratteristici della scala di lunghezza o di energia atomica e subatomica, dove le precedenti teorie classiche risultano inadeguate. Come caratteristica fondamentale, la meccanica quantistica descrive la radiazione e la materia sia come fenomeni ondulatori che come entità particellari, al contrario della meccanica classica, che descrive la luce solamente come un'onda e, ad esempio, l'elettrone solo come una particella. Questa inaspettata e controintuitiva proprietà della realtà fisica, chiamata dualismo onda-particella, è la principale ragione del fallimento delle teorie sviluppate fino al XIX secolo nella descrizione degli atomi e delle molecole. La relazione tra natura ondulatoria e corpuscolare è enunciata nel principio di complementarità e formalizzata nel principio di indeterminazione di Heisenberg. Esistono numerosi formalismi matematici equivalenti della teoria, come la meccanica ondulatoria e la meccanica delle matrici; al contrario, ne esistono numerose e discordanti interpretazioni riguardo all'essenza ultima del cosmo e della natura, che hanno dato vita a un dibattito tuttora aperto nell'ambito della filosofia della scienza. La meccanica quantistica rappresenta, assieme alla teoria della relatività, uno spartiacque rispetto alla fisica classica, portando alla nascita della fisica moderna. Attraverso la teoria quantistica dei campi, generalizzazione della formulazione originale che include il principio di relatività ristretta, essa è a fondamento di molte altre branche della fisica, come la fisica atomica, la fisica della materia condensata, la fisica nucleare, la fisica delle particelle, la chimica quantistica."
s2 = s2.replace(",", " ").replace(".", " ").replace(";", " ").replace(":", " ").replace("!", " ")
result: dict[str, int] = word_count(s2)
print(result)

#Verificare se una stringa è palindroma

"""
Restituisce True se è palindroma, altrimenti False
"""

def funz_palindromo(s: str) -> bool:
    i = 0
    y = -1
    flag = 0
    while i <= len(s)/2:
        if s[i] == s[y]:
            flag = 0
            i += 1
            y -= 1
        else:
            return False   
    return True

frase: str = "Amo Roma"
frase: str = frase.lower().replace(" ", "")
palindromo: bool = funz_palindromo(frase)
if palindromo == True:
    print("True")
else:
    print("False")