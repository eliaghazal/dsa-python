from pathlib import Path

path = Path('dsa-python/chapter 10: files and exceptions/learning_python.txt')
contents = path.read_text()
print(contents)

lines = contents.splitlines()
for line in lines:
  print(line)
