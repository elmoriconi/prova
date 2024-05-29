from abc import ABC, abstractmethod

class AbcAnimal(ABC):

    @abstractmethod
    def verso(self):
        pass

class Cane(AbcAnimal):

    def __init__(self, name: str) -> None:
        self.name: str = name

    def verso(self):
        print("Bau!")

class Gatto(AbcAnimal):

    def __init__(self, name: str) -> None:
        self.name: str = name

    def verso(self):
        print("Miao!")

class Coccodrillo(AbcAnimal):

    def __init__(self, name: str) -> None:
        self.name: str = name
    
    def verso(self):
        print("Roar!")

from typing import Any

a: dict[str, str|int] = {
    "key_1": "val_1",
    "key_2": "val_2",
    "key_3": 3
    }

b: dict[str, Any] = {               #meglio evitare Any
    "key_1": "val_1",
    "key_2": "val_2",
    "key_3": 3,
    "key_4": [4, 5, 6, 7]
    }

#se abbiamo dei tipi particolarmente complessi/annidati:
from typing import TypeAlias
tipo_composto: TypeAlias = dict[int, str]

c: dict[str,tipo_composto] = {
    "key_1": {1: ""},
    "key_2": {2: ""},
    "key_3": {3: ""}
    }

cane_1: Cane = Cane("Pluto")
cane_1.verso()
gatto_1: Gatto = Gatto("Silvestro")
gatto_1.verso()
coccodrillo_1: Coccodrillo = Coccodrillo("Giovanni")
coccodrillo_1.verso()

lista_animali: list[AbcAnimal] = [cane_1, gatto_1, coccodrillo_1]
for animale in lista_animali:
    animale.verso()