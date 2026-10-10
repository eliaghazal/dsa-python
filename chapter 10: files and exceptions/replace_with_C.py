from pathlib import Path

path = Path('/path/')
content = path.read_text()
content = content.replace('Python', 'C')
print(content)
