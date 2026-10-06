#Every Function: Think of things you could store in a list. For
#example, you could make a list of mountains, rivers, countries, cities,
#languages, or anything else you’d like. Write a program that creates a list
#containing these items and then uses each function introduced in this
#chapter at least once.

places = ['mount everest', 'niagara falls', 'great wall of china', 'pyramids of giza', 'statue of liberty']
print(places)
print(sorted(places))
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
places.append('machu picchu')
print(places)
places.insert(2, 'grand canyon')
print(places)
removed_place = places.pop(3)
print(f"Removed place: {removed_place}")
print(places)
places.remove('statue of liberty')
print(places)
places[1] = 'sydney opera house'
print(places)
del places[0]
print(places)
print(f"Number of places in the list: {len(places)}")
