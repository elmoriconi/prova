#Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi. 
#For example: 
#Test: print(list_statistics([1, 2, 3, 4, 5])) Result: (5, 1, 3.0)

def list_statistics(numbers: list[int]) -> ... :
    massimo: int = max(numbers)
    minimo: int = min(numbers)
    media_lista: float = sum(numbers)/len(numbers)
    return massimo, minimo, media_lista

print(list_statistics([1, 2, 3, 4, 5])) 


#Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione. L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere. La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.
#For example:
#Test: print(check_combination(True, False, True)) Result: Operazione permessa
#Test: print(check_combination(False, True, False)) Result: Operazione negata

def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA == True:
        return "Operazione permessa"
    elif conditionB == True and conditionC == True:
        return "Operazione permessa"
    else:
        return "Operazione negata"

print(check_combination(True, False, True))
print(check_combination(False, True, False))


#Scrivi una funzione che, dato un numero intero, determina se è un "numero magico". Un numero magico è definito come un numero che contiene il numero 7.
#For example:
#Test: print(is_magic_number(70)) Result: True
#Test: print(is_magic_number(123)) Result: False

def is_magic_number(num: int) -> bool:
    num: str = str(num)
    if "7" in num:
        return True
    else:
        return False

print(is_magic_number(70))
print(is_magic_number(123)) 


#Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.
#For example:
#Test: print(frequency_dict(['mela', 'banana', 'mela'])) Result: {'mela': 2, 'banana': 1}

def frequency_dict(elements: list) -> dict:
    dizionario: dict = {}
    for elem in elements:
        if elem in dizionario:
            dizionario[elem] += 1
        else:
            dizionario.update({elem: 1}) 
    return dizionario

print(frequency_dict(['mela', 'banana', 'mela']))


#La funzione dovrebbe calcolare la media dei numeri in una lista di interi. Un errore nell'implementazione porta a risultati inaspettati.
#For example:
#Test: print(calculate_average([1, 2, 3, 4, 5])) Result: 3.0
#Test: print(calculate_average([])) Result: 0

def calculate_average(numbers: list[int]) -> float:
    if len(numbers) == 0:
        return 0
    else:
        return sum(numbers) / len(numbers) 
    
print(calculate_average([1, 2, 3, 4, 5]))
print(calculate_average([])) 


#Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
#For example:
#Test: print(check_parentheses("()()"))	Result: True
#Test: print(check_parentheses("(()))(")) Result: False

def check_parentheses(expression: str) -> bool:
    count: int = 0
    for elem in expression:
        if elem == "(":
            count += 1
        elif elem == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0

print(check_parentheses("()()"))
print(check_parentheses("(()))("))


#Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi. Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.
#For example:
#Test: print(count_isolated([1, 2, 2, 3, 3, 3, 4])) Result: 2
#Test: print(count_isolated([1, 2, 3, 4, 5])) Result: 5

def count_isolated(lista: list) -> int:
    quanti: int = 0
    i: int = 0
    if len(lista) == 0:
        return quanti
    else:
        if lista[0] != lista[1]:
            quanti += 1
        if lista[-1] != lista[-2]:
            quanti += 1     
        for i in range(1, len(lista)-1):
            if lista[i] != lista[i-1] and lista[i] != lista[i+1]:
                quanti += 1
        return quanti


print(count_isolated([1, 1, 2, 2, 3, 4, 4]))


#Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, ritorni un nuovo insieme senza i numeri specificati nella lista.
#For example:
#Test: print(remove_elements({5, 6, 7}, [7, 8, 9])) Result: {5, 6}

def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set: 
    nuovo_set = original_set.copy()
    for i in elements_to_remove:
        nuovo_set.discard(i)
    return nuovo_set

print(remove_elements({5, 6, 7}, [7, 8, 9]))


#Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    dizionario: dict = {}
    for key in dict1:
        if key not in dict2:
            dizionario.update({key: dict1[key]})
        else:
            dizionario.update({key: dict2[key] + dict1[key]})
    for key in dict2:
        if key not in dizionario:
            dizionario.update({key: dict2[key]})
    return dizionario

print(merge_dictionaries({'x': 5}, {'x': -5}))



#Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni. La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione e l'elemento iniziale viene spostato alla fine della lista. Per la rotazione utilizzare lo slicing e gestire il caso in cui il numero specificato di posizioni sia maggiore della lunghezza della lista.
#For example:

def rotate_left(elements: list, k: int) -> list:
    lista: list = []
    if k == len(elements):
        return elements
    elif k > len(elements):
        k = k % len(elements)
    lista = elements[k:] + elements[:k]
    return lista