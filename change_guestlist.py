name = ['elia', 'john', 'mary', 'jane', 'michael']
print(name)
cannot_attend = name.pop(0)
print(name)
print(f"{cannot_attend.title()} cannot attend the concert.")
name.insert(0, 'taylor swift')
print(f"You are invited to the concert of {name[0].title()}!")
print(f"You are invited to the concert of {name[1].title()}!")
print(f"You are invited to the concert of {name[2].title()}!")
