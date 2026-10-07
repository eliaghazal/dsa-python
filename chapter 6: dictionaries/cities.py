cities = {'paris': {'country':'france', 'population': 2148327, 'fact': 'The Eiffel Tower is located in Paris.'},
          'tokyo': {'country':'japan', 'population': 13929286, 'fact': 'Tokyo is the most populous metropolitan area in the world.'},
          'new york': {'country':'usa', 'population': 8419600, 'fact': 'New York City is known as the "Big Apple."'},
          'sydney': {'country':'australia', 'population': 5312163, 'fact': 'Sydney is famous for its Opera House and Harbour Bridge.'},
          'cape town': {'country':'south africa', 'population': 433688, 'fact': 'Cape Town is known for its stunning Table Mountain and beautiful beaches.'}}

for city, info in cities.items():
  print(f"{city.title()} facts:")
  for k, v in info.items():
    print(f"{k.title()} : {v}")
