from pathlib import Path

files = ['cats.txt', 'dogs.txt']
for file in files:
  try:
    path = Path(file)
    content = path.read_text()
    print(content)
  except FileNotFoundError:
    print(f"File does not exist, or wrong path.")

''' except FileNotFoundError:
      pass
    This fails silently if either file is missing. '''
    
