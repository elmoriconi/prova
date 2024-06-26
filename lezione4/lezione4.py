#8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.

def display_message() -> str:
    message: str = "In this chapter, I'm learning about functions: how to write them and use them."
    return message

print(display_message())

#8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as "One of my favorite books is Alice in Wonderland". Call the function, making sure to include a book title as an argument in the function call.

def favourite_book(title: str) -> str:
    print(f"One of my favourite books is '{title}'")

title: str = "Pride and Prejudice"
favourite_book(title)

#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

def make_tshirt(size: str, text: str) -> str:
    print(f"The tshirt should be a size {size} and should read '{text}'.")

size: str = "M"
text: str = "Forza Roma"
make_tshirt(size, text)

def make_tshirt2(size: str, text: str) -> str:
    print(f"The tshirt should be a size {size} and should read '{text}'.")

make_tshirt2(size = "M", text = "Forza Roma")

#8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_tshirt3(size: str = "L", text: str = "I love Python") -> str:
    print(f"The tshirt should be a size {size} and should read '{text}'.")
    print(f"The tshirt should be a size M and should read '{text}'.")
    print(f"The tshirt should be a size S and should read 'I hate Python'.")

make_tshirt3()

#8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.

def describe_city(name: str, country: str = "Sweden") -> str:
    print(f"{name} is in {country}.")

describe_city(name = "Stockholm")
describe_city(name = "Malmo")
describe_city(name = "Oslo")

#8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this: "Santiago, Chile". Call your function with at least three city-country pairs, and print the values that are returned.

def city_country(name: str, country: str) -> str:
    print(f"{name}, {country}")

city_country(name = "Madrid", country = "Spain")
city_country(name = "Rome", country = "Italy")
city_country(name = "Paris", country = "France")

#8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly. Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.

def make_album(artist: str, title: str, songs: int) -> dict:
    album: dict = {
        "artist": artist,
        "title": title,
        "songs": songs
    }
    print(album)

make_album(artist = "Hozier", title = "Wasteland, Baby!", songs = None)
make_album(artist = "Harry Styles", title = "Harry's House", songs = None)
make_album(artist = "Conan Gray", title = "Superache", songs = None)
make_album(artist = "Taylor Swift", title = "The Tortured Poets Department", songs = 31)

#8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.

def make_album2(album: dict) -> dict:
    print(album)

album: dict = {
        "artist": "",
        "title": "",
    }
for keyword in album:
    album[keyword] = input(f"{keyword}:")
make_album2(album)

#8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.

def show_messages(messages: list[str]) -> str:
    for elem in messages:
        print(elem)    

messages: list[str] = ["Hello, how are you?",
                       "Have you finished you homework?",
                       "I am studying right now"]
show_messages(messages)

#8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.

def send_messages(messages: list[str]) -> str:
    sent_messages: list[str] = []
    i: int = 0
    while i in range(len(messages)):
        print(messages[i])
        sent_messages.append(messages[i])
        messages.remove(messages[i])
    print(messages)
    print(sent_messages)

messages2: list[str] = ["Hello, how are you?",
                       "Have you finished you homework?",
                       "I am studying right now"]
send_messages(messages2)

#8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.

#I'm not quite sure I understand what I'm supposed to do

def send_messages(messages: list[str]) -> str:
    for elem in messages:
        print(elem)
    sent_messages: list[str] = messages.copy()
    print(messages)
    print(sent_messages)

messages2: list[str] = ["Hello, how are you?",
                       "Have you finished you homework?",
                       "I am studying right now"]
send_messages(messages2)

#8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.

def sandwiches(*args) -> list[str]:
    print(args)

sandwiches("tomato", "mayo", "tuna")
sandwiches("ham", "lettuce", "cheese", "bacon")
sandwiches("chicken", "tomato")

#8-13. User Profile: Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you. All the values must be passed to the function as parameters. The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"

def build_profile(first_name: str, last_name: str, age: int, hair_colour: str, eye_colour: str) -> str:
    print(f"{first_name} {last_name}, age {age}, hair {hair_colour}, eyes {eye_colour}")

first_name: str = "Elena"
last_name: str = "Moriconi"
age: int = 21
hair_colour: str = "brown"
eye_colour: str = "brown"
build_profile(first_name, last_name, age, hair_colour, eye_colour)

#8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) Print the dictionary that’s returned to make sure all the information was stored correctly. 

def car_info(manufacturer: str, model: str, **kwargs) -> dict:
    dictionary: dict = {"manufacturer": manufacturer,
                        "model": model,
                        }
    if len(kwargs) > 0:
        for keyword in kwargs:
            dictionary.update({keyword: kwargs[keyword]})
    print(dictionary)

manufacturer: str = "subaru"
model: str = "outback"
car_info(manufacturer, model, colour = "blue", two_package = True)

#8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.



#8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:
    #import module_name
    #from module_name import function_name
    #from module_name import function_name as fn
    #import module_name as mn
    #from module_name import *



#8-17. Styling Functions: Choose any three programs you wrote for this chapter, and make sure they follow the styling guidelines described in this section.