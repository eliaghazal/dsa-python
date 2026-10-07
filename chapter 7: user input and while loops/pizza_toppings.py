prompt = "Enter your toppings. Enter quit to stop."

while True:
  topping = input(prompt)
  if topping == "quit":
    break
  print(f"We will add {topping.title()} to your order.")
