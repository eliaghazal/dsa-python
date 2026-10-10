number1 = input("Enter a number: ")
number2 = input("Enter another number: ")

try:
  print(int(number1) + int(number2))
except ValueError:
  print(f"You entered strings. Please enter numbers.")
