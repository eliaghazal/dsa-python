#3-6. More Guests: You just found a bigger dinner table, so now more space
#is available. Think of three more guests to invite to dinner.
#Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
#end of your program, informing people that you found a bigger table.
#Use insert() to add one new guest to the beginning of your list.
#Use insert() to add one new guest to the middle of your list.
#Use append() to add one new guest to the end of your list.
#Print a new set of invitation messages, one for each person in your list.

guests = ['taylor swift', 'ariana grande', 'ed sheeran', 'bruno mars', 'adele']
print("Good news! I found a bigger dinner table, so now more space is available.")
guests.insert(0, 'justin bieber')
guests.insert(3, 'rihanna')
guests.append('shawn mendes')
print(f"You are invited to the dinner of {guests[0].title()}!")
print(f"You are invited to the dinner of {guests[1].title()}!")
print(f"You are invited to the dinner of {guests[2].title()}!")
print(f"You are invited to the dinner of {guests[3].title()}!")
print(f"You are invited to the dinner of {guests[4].title()}!")
print(f"You are invited to the dinner of {guests[5].title()}!")
