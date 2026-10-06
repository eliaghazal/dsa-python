my_pizza = ['pepperoni', 'margherita', 'hawaiian']
my_friend_pizza = my_pizza[:]
my_pizza.append('veggie')
my_friend_pizza.append('bbq chicken')
print("My favorite pizzas are:")
for pizza in my_pizza:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in my_friend_pizza:
    print(pizza)
