"""i: int = 0

assert i == 0, f"The value must be equal to 0, instead is {i}!"

def check_sqrt(func, input: int, result: int):
    n = func(input)
    assert n == result, f"The value must be equal to {result}, instead is {n}!"

#def constant(input: int) -> int:
#    return -1

from math import sqrt

#check_sqrt(constant, 4, 2) #ritorna -1 invece di 2 perché la funzione constant ritorna un valore costante -1
check_sqrt(sqrt, 4, 2)"""


class Calculations:

    def __init__(self, a: float, b: float) -> None:
        self.a: float = a
        self.b: float = b

    def get_sum(self) -> float:
        return self.a + self.b
    
    def get_difference(self) -> float:
        return self.a - self.b
    
    def get_product(self) -> float:
        return self.a * self.b
    
    def get_quotient(self) -> float:
        return self.a / self.b
    
