# pizza.py file
def make_pizza(size, *toppings):
  print(f"\nMaking a {size}-inch pizza with the following toppings:")
  for topping in toppings:
    print(f"- {topping}")

# make_pizza.py file
import pizza

pizza.make_pizza(16, 'pepperoni')

# or if you want a specific function from another module
from pizza import make_pizza

make_pizza(16, 'pepperoni')

# or if you want all the functions in another module
from pizza import *

make_pizza(16, 'pepperoni')

# you can give the functions an alias too
from pizza import make_pizza as mp

mp(16, 'pepperoni')
