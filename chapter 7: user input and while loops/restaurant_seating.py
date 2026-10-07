prompt = "Welcome to Elia's restautant! How many people are dining?"
number = int(input(prompt))

if number >= 8:
  print("You will have to wait for a table.")
else:
  print("Your table is ready.")
