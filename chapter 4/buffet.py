buffet=('burger', 'jello', 'nutella', 'strawberry', 'spaghetti')
for food in buffet:
  print(food)
# buffet.append('banana') , it rejects it because it is a tuple.
# to change:
buffet = ('burger', 'banana', 'nutella', 'strawberry', 'spaghetti')
for food in buffet:
  print(food)
