languages = {'elia': 'python', 'george': 'c++', 'william':'rust', 'bassam':'c#'}
names = ['elia', 'rami', 'khoder', 'miled', 'george']
for name in names:
  if name not in languages.keys():
    print(f"{name.title()}, is invited to take the poll.")
  else:
    print(f"Thank you for taking the poll, {name.title()}!")
