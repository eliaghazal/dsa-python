favorite_places = {'elia': ['usa', 'switzerland'], 'george':['switzerland', 'germany'], 'khoder':['japan', 'china'], 'nelly':['paris', 'london']}
for name, place in favorite_places.items():
  print(f"{name.title()}'s favorite places are:")
  for p in place:
    print(f"{p.title()}")
