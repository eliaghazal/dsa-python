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
