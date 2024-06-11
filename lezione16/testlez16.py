"""class Contatore:
    
    def __init__(self):
        self.conteggio: int = 0
        
    def setZero(self):
        self.conteggio = 0

    def add1(self):
        self.conteggio += 1
        
    def sub1(self):
        if self.conteggio >= 1:
            self.conteggio -= 1
        else:
            print("Non è possibile eseguire la sottrazione")
            
    def get(self):
        return self.conteggio
        
    def mostra(self):
        print(f"Conteggio attuale: {self.conteggio}")

c = Contatore()  
c.add1()
c.mostra()"""

class RecipeManager:
    
    def __init__(self):
        self.ricette: dict[str, list[str]] = {}
        
    def create_recipe(self, name: str, ingredients: list[str]):
        for key, value in self.ricette.items():
            if name not in self.ricette.items():
                self.ricette.key = name
                self.ricette.value = ingredients
            else:
                print("Ricetta già esistente")
        return self.ricette
    
    def add_ingredient(self, recipe_name: str, ingredient: str):
        for key, value in self.ricette.items():
            if recipe_name in self.ricette.items():
                if ingredient not in self.ricette[recipe_name]:
                    lista_ingredienti = self.ricette[recipe_name]
                    self.ricette[recipe_name].append(ingredient)
                    self.ricette.update({"recipe_name: lista_ingredienti"})
                    return self.ricette[recipe_name]
                else:
                    print("Ingrediente già presente")
            else:
                print("Ricetta non esistente")
    
    def remove_ingredient(self, recipe_name: str, ingredient: str):
        for key, value in self.ricette.items():
            if recipe_name in self.ricette.items():
                if ingredient in self.ricette[recipe_name]:
                    lista_ingredienti = self.ricette[recipe_name]
                    self.ricette[recipe_name].remove(ingredient)
                    self.ricette.update({"recipe_name: lista_ingredienti"})
                    return self.ricette[recipe_name]
                else:
                    print("Ingrediente non presente")
            else:
                print("Ricetta non esistente")
            
    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str):
        for key, value in self.ricette.items():
            if recipe_name in self.ricette.items():
                if old_ingredient in self.ricette[recipe_name]:
                    lista_ingredienti = self.ricette[recipe_name]
                    #.replace(old_ingredient, new_ingredient)
                    self.ricette.update({"recipe_name: lista_ingredienti"})
                    return self.ricette[recipe_name]
                else:
                    print("Ingrediente non presente")
            else:
                print("Ricetta non esistente")
                
    def list_recipes(self):
        lista_chiavi: list[str] = []
        for key, value in self.ricette.items():
            lista_chiavi.append(key)
        return lista_chiavi
        
    def list_ingredients(self, recipe_name: str):
        for key, value in self.ricette.items():
            if recipe_name in self.ricette.items():
                lista_ingredienti = self.ricette[recipe_name]
                return self.ricette[recipe_name]
            else:
                print("Ricetta non esistente")
    
    def search_recipe_by_ingredient(self, ingredient: str):
        for key, value in self.ricette.items():
            if ingredient in self.ricette[key]:
                return self.ricette[key]

manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
#print(manager.add_ingredient("Pizza Margherita", "Basilico"))
#print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
#print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
#print(manager.list_ingredients("Pizza Margherita"))