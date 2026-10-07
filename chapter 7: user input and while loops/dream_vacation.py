prompt = "If you could visit one place in the world, where would you go?"
responses = {}
polling_Active = True

while polling_Active:
  name = input("What is your name? \n")
  place = input("If you could visit one place in the world, where would you go? \n")
  responses[name] = place
  poll = input("Is there another person to poll? y/n \n")
  if poll != "y":
    polling_Active = False
for n, v in responses.items():
  print(f"{n.title()} would like to go to {v.title()}!\n")
