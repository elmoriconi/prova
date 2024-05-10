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


#Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. 
#Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.
#For example:
#Test: print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2})) Result: [1, 3, 4]
#Test: print(rimuovi_elementi([], {2: 1})) Result: []

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    pass

print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
print(rimuovi_elementi([], {2: 1})) 


#Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.
#For example:
#Test: print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}])) Result: {'Alice': [90, 85], 'Bob': [75]}
#Test: print(aggrega_voti([])) Result: {}

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    new_dict: dict = {}
    for elem in voti:
        student_name: str = elem["nome"]
        student_grade: int = elem["voto"]
        if student_name in new_dict:
            new_dict[student_name].append(student_grade)
        else:
            new_dict[student_name] = [student_grade]
    return new_dict

print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))
print(aggrega_voti([]))


#Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.
#For example:
#Test: print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0})) Result: {'Zaino': 45.0, 'Quaderno': 19.8}
#Test: print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0}))  Result: {}

def filtra_e_mappa(prodotti: dict[str:float]) -> list[str:float]:
    new_dict: dict = {}
    for key, value in prodotti.items():
        if value > 20:
            prezzo_scontato: float = value * 0.9
            new_dict.update({key: prezzo_scontato})
    return new_dict

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0})) 