class Restaurant:
  def __init__(self, restaurant_name, cuisine_type):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type

  def describe_restaurant(self):
    print(f"The restaurant is called {self.restaurant_name.title()}.\nIts cuisine is {self.cuisine_type}.")

  def open_restaurant(self):
    print(f"{self.restaurant_name.title()} is open!")

my_restaurant = Restaurant("Burger King", "American")

print(f"The restaurant is called {my_restaurant.restaurant_name.title()}.\nIts cuisine is {my_restaurant.cuisine_type}.")
print(f"{my_restaurant.restaurant_name.title()} is open!")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()


mcdonalds = Restaurant("McDonald's", "American")
taco_bell = Restaurant("Taco Bell", "Mexican")
chick_fil_a = Restaurant("Chick-Fil-A", "American")

mcdonalds.describe_restaurant()
mcdonalds.open_restaurant()

taco_bell.describe_restaurant()
taco_bell.open_restaurant()

chick_fil_a.describe_restaurant()
chick_fil_a.open_restaurant()
