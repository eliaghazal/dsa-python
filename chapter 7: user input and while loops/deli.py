sandwich_orders = ['ham and cheese', 'ham', 'cheese', 'labneh']
finished_sandwiches = []
while sandwich_orders:

    current_sandwich = sandwich_orders.pop()
    print(f"I have made your {current_sandwich} sandwich!")
    finished_sandwiches.append(current_sandwich)
print(f"All the sandwiches made:")
for s in finished_sandwiches:
  print(s)
