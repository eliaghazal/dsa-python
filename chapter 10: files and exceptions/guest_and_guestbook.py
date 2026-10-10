""" Guest """

from pathlib import Path

name = input("Enter your name: ")

path = Path('/path')
contents = f"The user is called {name.title()}."
path.write_text(contents)

""" Guest book """

names = []
while True:
  name = input("Enter your name: Enter q to leave")
  if name == 'q':
    break
  else:
    names.append(name)

for name in names:
  contents += f"{name.title()}\n"

path.write_text(contents)
  
  
