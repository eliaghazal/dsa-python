from pathlib import Path

path = Path('twilight.txt')
contents = path.read_text()

lines = contents.splitlines()

the = 0
for line in lines:
  the += line.lower().count('the ')
print(the)
