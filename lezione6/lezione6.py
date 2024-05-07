class Person:


    def __init__(self, name, age):
        self.name = name
        self.age = age


alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

print(f"Bob's age: {bob.age}")

if alice.age > bob.age:
    print(alice.name)
else:
    print(bob.name)

elena = Person("Elena M.", 21)
giada = Person("Giada G.", 20)
gabriele = Person("Gabriele C.", 19)

people: list[Person] = [alice, bob, elena, giada, gabriele]

min_age: int = float('inf')
index_min_age: int = 0
for i in range(len(people)):
    if people[i].age < min_age:
        min_age = people[i].age
        index_min_age = i
print(f"La persona più giovane è {people[index_min_age].name} che ha {people[index_min_age].age} anni")