class Person:

    def __init__(self, cf: str, name: str, surname: str, age: int):
        self.cf: str = cf
        self.name: str = name
        self.surname: str = surname
        self.age: int = age

class Student(Person):

    def __init__(self, id: str, cf: str, name: str, surname: str, age: int):
        super().__init__(cf, name, surname, age)
        self.id: str = id
        self.group = None

    def withdraw(self):
        if self.group:
            self.group.students.remove(self)
            self.group.limit_students += 1
            return True
        return False