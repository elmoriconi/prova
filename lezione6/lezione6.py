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
min_age: int = float('inf')
index_min_age: int = 0
for i in range(len(people)):
    if people[i].age < min_age:
        min_age = people[i].age
        index_min_age = i
print(f"La persona più giovane è {people[index_min_age].name} che ha {people[index_min_age].age} anni. " \
      + f"Altezza {people[index_min_age].height} cm e peso {people[index_min_age].weight} kg")

#con __str__
print(people[0])

class Student:


    def __init__(self, name: str, studyProgram: str):
        self.name = name
        self.studyProgram = studyProgram
        self.age = None
        self.gender = None

    def printInfo(self) -> str:
        if self.age:
            return f"Name: {self.name}, study program: {self.studyProgram}, age: {self.age}"
        if self.gender:
            return f"Name: {self.name}, study program: {self.studyProgram}, gender: {self.gender}"
        if self.age and self.gender:
            return f"Name: {self.name}, study program: {self.studyProgram}, age: {self.age}, gender: {self.gender}"
        else:
            return f"Name: {self.name}, study program: {self.studyProgram}"
        
    def set_age(self, age: int):
        self.age: int = age
    
    def set_gender(self, gender: str):
        self.gender: str = gender

elena: Student = Student("Elena M.", "Cloud Dev.")
davide: Student = Student("Davide C.", "Cloud Dev.")
walter: Student = Student("Walter A.", "Cloud Dev.")
print(elena.printInfo())
print(davide.printInfo())
print(walter.printInfo())
elena.set_age(21)
walter.set_gender("male")
davide.set_age(19)
davide.set_gender("male")    #perché questo non lo aggiunge?
print(elena.printInfo())
print(davide.printInfo())
print(walter.printInfo())


#metodi per la classe

class studenti:

    student_grades: list[float] = []

    def __init__(self, name: str, grade: float):
        self.name = name
        self.student_grades.append(grade)
        self.my_grades: list[float] = []
    def add_grades(self, grade: float):
        self.my_grades.append(grade)
        self.student_grades.append(grade)

    def grades_average(self):
        return sum(self.my_grades)/len(self.my_grades)

    @classmethod
    def get_average_grades(cls) -> float:
        avg = sum(cls.student_grades)/len(cls.student_grades)
        return avg

francesca: studenti = studenti(grade = 8, name = "Francesca")
davide: studenti = studenti(grade = 9, name = "Davide")
francesca.add_grades(8)
avg = studenti.get_average_grades()
avgFrancesca = francesca.grades_average()
print(f"la media della classe è {avg}")
print(f"la media di Francesca è: {avgFrancesca}")


class Animal:

    def __init__(self, name:str):
        self.name = name
        self.legs = 0

    def __str__(self) -> str:
        return f"Name: {self.name}"

    def change_legs(self, new_legs: int) -> int:
        self.legs = new_legs

    def setLegs(self, legs: int) -> int:
        self.legs = legs
    
    def getLegs(self) -> int:
        return self.legs

    def printInfo2(self) -> str:
        return f"Animal's name: {self.name}, animal's legs: {self.legs}."

tiger: Animal = Animal("tiger")
flamingo: Animal = Animal("flamingo")
print(tiger)
print(flamingo)
tiger.change_legs(3)
print(tiger.legs)
elephant: Animal = Animal("elephant")
frog: Animal = Animal("frog")
snake: Animal = Animal("snake")
elephant.setLegs(4)
snake.setLegs(0)
frog.setLegs(4)
print(elephant.legs)
print(snake.legs)
print(frog.legs)
print(frog.getLegs())
print(frog.printInfo2())
