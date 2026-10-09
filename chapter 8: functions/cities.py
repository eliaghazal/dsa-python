def describe_city(city, country="France"):
  print(f"{city.title()} is in {country.title()}.")
describe_city("paris")
describe_city("beirut") #wrong country
describe_city("beirut", "lebanon")
