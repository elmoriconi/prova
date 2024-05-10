#Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione. 
#L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere. 
#La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.
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

#Scrivi una funzione che accetti una lista di numeri e ritorni la somma dei numeri che sono divisibili sia per 2 che per 3.
#For example:
#Test: print(somma_condizionale([1, 2, 3, 6, 12])) Result: 18
#Test: print(somma_condizionale([5, 7, 11])) Result: 0

def somma_condizionale(numeri: list[int]) -> int:
    sum: int = 0
    for elem in numeri:
        if elem % 2 == 0 and elem % 3 == 0:
            sum += elem
    return sum

print(somma_condizionale([1, 2, 3, 6, 12]))
print(somma_condizionale([5, 7, 11]))