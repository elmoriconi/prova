#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

guestlist: list = ["Jane Austen", "Hozier", "Kabi Nagata"]
invitations: list = ["I am a big fan of your works, and I'd be honoured to invite you to a dinner party", "I'd love to discuss your latest album over dinner if you're available next week", "I love your mangas and think we are very much alike. How would you like to meet up for dinner?"]
for i in range(len(invitations)):
    print(f"Dear {guestlist[i]}, {invitations[i]}. Best regards.")


#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
#• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
#• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#• Print a second set of invitation messages, one for each person who is still in your list.

print(f"{guestlist[0]} can't make it.")
guestlist[0] = "William Shakespeare"
for i in range(len(invitations)):
    print(f"Dear {guestlist[i]}, {invitations[i]}. Best regards.")


#3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
#• Use insert() to add one new guest to the beginning of your list.
#• Use insert() to add one new guest to the middle of your list.
#• Use append() to add one new guest to the end of your list.
#• Print a new set of invitation messages, one for each person in your list.

print("Dear guests, since a bigger table is available, the party will host a few more guests.")
guestlist.insert(2, "Marsha P. Johnson")
guestlist.insert(1, "Dante Alighieri")
guestlist.append("David Tennant")
invitations.insert(2, "I deeply admire you for your activism and would like to invite you to my dinner party")
invitations.insert(1, "upon reading your works, there are quite a few things I'd like to ask you; hence you are invited to my place for dinner")
invitations.append("as a fan of your movies and tv series, I'd like to meet you and invite you over for dinner")
for i in range(len(invitations)):
    print(f"Dear {guestlist[i]}, {invitations[i]}. Best regards.")


#3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
#• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
#• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#• Print a message to each of the two people still on your list, letting them know they’re still invited.
#• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

print("Dear guests, unfortunately, due to an unexpected problem, I will only be able to recieve two of you for dinner.")
for i in range(4):
    print(f"Dear {guestlist[i]}, I'm sorry to inform you that we will have to postpone our dinner together.")
guestlist.pop(0)
guestlist.pop(0)
guestlist.pop(0)
guestlist.pop(0)
for i in range(len(guestlist)):
    print(f"Dear {guestlist[i]}, I'm happy to confirm you are still invited to dinner next week.")
del guestlist[0:2]
print(guestlist)


#3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
#• Store the locations in a list. Make sure the list is not in alphabetical order.
#• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
#• Use sorted() to print your list in alphabetical order without modifying the actual list.
#• Show that your list is still in its original order by printing it.
#• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
#• Show that your list is still in its original order by printing it again.
#• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
#• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#• Use sort() to change your list so it’s stored in reverse-alphabetical order.
#Print the list to show that its order has changed.

locations: list = ["Iceland", "Egypt", "Spain", "Scotland", "Japan"]
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)


#3-9. Dinner Guests: Working with one of the programs from Exercises 3, use len() to print a message indicating the number of people you’re inviting to dinner.
guestlist: list = ["William Shakespeare", "Dante Alighieri", "Hozier", "Marsha P. Johnson", "Kabi Nagata", "David Tennant"] #I created the list again otherwise its length would be 0 (we emptied it earlier)
print(f"I am inviting {len(guestlist)} to my dinner party.")


#3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

languages: list = ["Italian", "Portuguese", "Japanese", "Chinese"]
print(languages)
languages.append("Korean")
print(languages)
languages.pop(2)
print(languages)
languages.remove("Chinese")
print(languages)
print(sorted(languages))
print(languages)
languages.sort(reverse=True)
print(languages)
languages.insert(1, "English")
print(languages)

#6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

person: dict = {"first_name": "Alice",
                "last_name": "Bocci",
                "age": 20,
                "city": "Rome"}
for key in person:
    print(person[key])


#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

favourite_numbers: dict = {"Alessandra": 17,
                           "Elena": 7,
                           "Marco": 3,
                           "Andrea": 9,
                           "Giada": 15}
for key in favourite_numbers:
    print(f"Person: {key}, favourite number: {favourite_numbers[key]}")


#6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.

favourite_numbers.update({"Alessandra": [17, 4]})
favourite_numbers.update({"Elena": [7, 3]})
favourite_numbers.update({"Marco": [3, 18]})
favourite_numbers.update({"Andrea": [9, 27]})
favourite_numbers.update({"Giada": [15, 8]})
for key in favourite_numbers:
    print(f"Person: {key}, favourite number: {favourite_numbers[key]}")


#6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#• Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
#• Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.



#6-7. People: Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.

second_person: dict = {"first_name": "Giada",
                "last_name": "Giammarco",
                "age": 20,
                "city": "Rome"}
third_person: dict = {"first_name": "Giulia",
                "last_name": "Marini",
                "age": 20,
                "city": "Rome"}
people: list = [person, second_person, third_person]
for i in people:
    print(i)


#6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet. 
first_pet: dict = {"animal": "dog",
                   "name": "Nina",
                   "owner": "Alice"}
second_pet: dict = {"animal": "dog",
                   "name": "Maya",
                   "owner": "Giulia"}
third_pet: dict = {"animal": "cat",
                   "name": "Seki",
                   "owner": "Lavinia"}
fourth_pet: dict = {"animal": "dog",
                   "name": "Teo",
                   "owner": "Marta"}
pets: list = [first_pet, second_pet, third_pet, fourth_pet]
for i in pets:
    print(i)


#6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.

favourite_places: dict = {"Giada": "Rome, Florence",
                          "Alessandra": "Naples",
                          "Elena":"Rome, London, Budapest"}
for key in favourite_places:
    print(f"{key}: {favourite_places[key]}")


#6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.
rome: dict = {"country": "Italy",
              "population": "2.873 million people",
              "fact": "its birthday is on April 21st"}
madrid: dict = {"country": "Spain",
              "population": "3.223 million people",
              "fact": "its official symbol is a bear"}
amsterdam: dict = {"country": "Netherlands",
              "population": "821.752 people",
              "fact": "it has more bicycles than people"}
cities: dict = {"Rome": rome,
                "Madrid": madrid,
                "Amsterdam": amsterdam}
for key in cities:
    print(f"{key}: {cities[key]}")

#6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output.