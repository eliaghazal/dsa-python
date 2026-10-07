sandwich_orders = ['ham and cheese', 'pastrami', 'ham', 'pastrami', 'cheese', 'labneh', 'pastrami']
finished_sandwiches = []
print("We have run out of pastrami sandwiches.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:

    current_sandwich = sandwich_orders.pop()
    print(f"I have made your {current_sandwich} sandwich!")
    finished_sandwiches.append(current_sandwich)
print(f"All the sandwiches made:")
for s in finished_sandwiches:
  print(s)
