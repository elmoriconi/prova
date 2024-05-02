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