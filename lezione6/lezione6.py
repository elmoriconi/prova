class Person:


    def __init__(self, name: str, age: int, height: float, weight:float):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


    def __str__(self) -> str:
        return(f"Nome: {self.name}, età: {self.age}, altezza: {self.height}, peso: {self.weight}")


alice: Person = Person("Alice W.", 45, 166, 60)
bob: Person = Person("Bob M.", 36, 178, 76)

print(f"Bob's age: {bob.age}")

if alice.age > bob.age:
    print(alice.name)
else:
    print(bob.name)

elena: Person = Person("Elena M.", 21, 158, 49)
giada: Person = Person("Giada G.", 20, 160, 55)
gabriele: Person = Person("Gabriele C.", 19, 180, 80)

people: list[Person] = [alice, bob, elena, giada, gabriele]
#senza __str__
"""
min_age: int = float('inf')
index_min_age: int = 0
for i in range(len(people)):
    if people[i].age < min_age:
        min_age = people[i].age
        index_min_age = i
print(f"La persona più giovane è {people[index_min_age].name} che ha {people[index_min_age].age} anni. " \
      + f"Altezza {people[index_min_age].height} cm e peso {people[index_min_age].weight} kg")
"""
#con __str__
print(people[0])

class Student:


    def __init__(self, name: str, studyProgram: str, age: int, gender: str):
        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender

    def printInfo(self) -> str:
        return print(f"Name: {self.name}, study program: {self.studyProgram}, age: {self.age}, gender: {self.gender}")

elena: Student = Student("Elena M.", "Cloud Dev.", 21, "female")
davide: Student = Student("Davide C.", "Cloud Dev.", 20, "male")
walter: Student = Student("Walter A.", "Cloud Dev.", 32, "male")
elena.printInfo()
davide.printInfo()
walter.printInfo()