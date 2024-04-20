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