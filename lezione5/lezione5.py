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
