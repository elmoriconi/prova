#9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: 
      #a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, 
      #and a method called open_restaurant() that prints a message indicating that the restaurant is open. 
      #Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

class Restaurant:

    def __init__(self, restaurant_name:str, cuisine_type: str):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        return f"Il ristorante si chiama {self.name} e fa cucina {self.type}."
    
    def open_restaurant(self):
        return f"{self.name} è aperto."

restaurant: Restaurant = Restaurant("Oishi", "giapponese")  
print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())

#9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, 
      #and call describe_restaurant() for each instance.

restaurant2: Restaurant = Restaurant("Trapizzino", "romana")
restaurant3: Restaurant = Restaurant("Gandhi", "indiana")
restaurant4: Restaurant = Restaurant("Ami Poke", "hawaiana")
print(restaurant2.describe_restaurant())
print(restaurant3.describe_restaurant())
print(restaurant4.describe_restaurant())

#9-3. Users: Make a class called User. Create two attributes called first_name and last_name, 
      #and then create several other attributes that are typically stored in a user profile. 
      #Make a method called describe_user() that prints a summary of the user’s information. 
      #Make another method called greet_user() that prints a personalized greeting to the user. 
      #Create several instances representing different users, and call both methods for each user.
#9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. 
      #Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
      #Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
      #Make an instance of the User class and call increment_login_attempts() several times. 
      #Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
      #Print login_attempts again to make sure it was reset to 0.

class User:

    def __init__(self, first_name: str, last_name: str, age: int, date_of_birth: str, username: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.date_of_birth = date_of_birth
        self.username = username
        self.login_attempts = 0

    def describe_user(self):
        return f"First and last name: {self.first_name} {self.last_name}, username: {self.username}, "\
             + f"age: {self.age}, date of birth: {self.date_of_birth}"

    def greet_user(self):
        return f"Welcome back {self.username}"

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user: User = User("Elena", "Moriconi", 21, "07/01/2003", "elmoriconi")
print(user.describe_user())
print(user.greet_user())
user2: User = User("Giada", "Giammarco", 20, "15/07/2003", "g.gmm")
user3: User = User("Alice", "Bocci", 21, "03/05/2003", "allie")
user4: User = User("Vittoria", "Verdesca", 21, "16/04/2003", "vitto")
print(user2.describe_user())
print(user2.greet_user())
print(user3.describe_user())
print(user3.greet_user())
print(user4.describe_user())
print(user4.greet_user())
#9-5
for i in range(5):
    user.increment_login_attempts()
print(f"login attempts: {user.login_attempts}")
user.reset_login_attempts()
print(f"login attempts: {user.login_attempts}")

#9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. 
      #Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then 
      #change this value and print it again. Add a method called set_number_served() that lets you set the number of customers 
      #that have been served. Call this method with a new number and print the value again. 
      #Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
      #Call this method with any number you like that could represent how many customers were served in, say, a day of business. 

class Restaurant2:

    def __init__(self, restaurant_name:str, cuisine_type: str):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def set_number_served(self, number_served: int): 
        self.number_served = number_served

    def increment_number_served(self, increment: int): 
        self.number_served += increment

restaurant0: Restaurant2 = Restaurant2("Oishi", "giapponese")
restaurant0.set_number_served(3)
print(f"Clienti serviti: {restaurant0.number_served}")
restaurant0.set_number_served(9)
print(f"Clienti serviti: {restaurant0.number_served}")
restaurant0.increment_number_served(35)
print(f"Clienti serviti: {restaurant0.number_served}")

#9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.



#9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1  or Exercise 9-4. Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method. 

#9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 or Exercise 9-5. Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method. 

#9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.

#9-9. Battery Upgrade: Use the final version of electric_car.py from this section. Add a method to the Battery class called upgrade_battery(). This method should check the battery size and set the capacity to 65 if it isn’t already. Make an electric car with a default battery size, call get_range() once, and then call get_range() a second time after upgrading the battery. You should see an increase in the car’s range.

#9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.

#9-11. Imported Admin: Start with your work from Exercise 9-8. Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.

#9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.

#9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.

#9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. Randomly select 4 numbers or letters from the list and print a message saying that any ticket matching these 4 numbers or letters wins a prize.

#9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins. Print a message reporting how many times the loop had to run to give you a winning ticket.



#Fatto in classe

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

    def __init__(self, name:str, legs: int):
        self.name = name
        self.legs = legs

    def __str__(self) -> str:
        return f"Name: {self.name}"

    def setLegs(self, new_legs: int) -> int:
        self.legs = new_legs
    
    def getLegs(self) -> int:
        return self.legs

    def printInfo2(self) -> str:
        return f"Animal's name: {self.name}, animal's legs: {self.legs}."

tiger: Animal = Animal("tiger", 4)
flamingo: Animal = Animal("flamingo", 2)
print(tiger)
print(flamingo)
tiger.legs = 3
print(tiger.legs)
"""elephant: Animal = Animal("elephant")
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
"""
"""
class Food:

    def __init__(self, name: str, price: float, description: str = None):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return print(f"{self.name}: {self.description}. {self.price} euro.")    

first_food: Food = Food("pasta al pesto", 13, "pasta con pesto di basilico")
second_food: Food = Food("hamburger", 8.50, "panino con carne, insalata, pomodoro e salsa")
third_food: Food = Food("pasta con il tonno", 12.50, "pasta con passata di pomodoro e tonno")
first_food.__str__()
second_food.__str__()
third_food.__str__()

class Menu:

    def __init__(self, foods: list[Food] = [] ): #foods = [] si scrive così perché è opzionale
        self.foods: list[Food] = foods
    
    def __str__(self) -> str:
        repr: str = ""
        for food in self.foods:
            repr += food.__str__()
        return f"{self.foods}"

    def addFood(self, new_food: str):
        count: int = 0
        for food_menu in self.foods:
            if food.name == food_menu.name:
                count += 1  #non sarà mai > 1
        if count == 0:
            self.foods.append(new_food)

    def removeFood(self, old_food: str):
        self.foods.remove(old_food)

menu = Menu()
menu.addFood(first_food)
menu.addFood(second_food)
menu.addFood(third_food)
item4: Food = Food("pizza", 7)
item5: Food = Food("tramezzino", 3, "prosciutto e formaggio")
menu.removeFood(first_food)
print(menu)
"""

