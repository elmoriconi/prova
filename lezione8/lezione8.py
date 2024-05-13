class animal:

    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age

    def get_name(self) -> str:
        return self.name
    
    def get_age(self) -> int:
        return self.age
    
    def set_name(self, new_name:str):
        self.name = new_name
        
    def set_age(self, new_age: int):
        self.age = new_age

class Zoo:

    def __init__(self, fences = [], zoo_keepers = []): #questi oggetti di default sono condivisibili, quindi in due istanze zoo diverse condividono comunque le stesse liste
        self.fences = fences
        self.zoo_keepers = zoo_keepers

    def add_fence(self, fence):
        self.fences.append(fence)

    def get_fences(self):
        return self.fences
    