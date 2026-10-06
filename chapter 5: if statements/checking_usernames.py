current_users = ['elia', 'maya', 'george', 'william', 'nelly']
new_users = ['elia', 'GEORGE', 'robin', 'bradley', 'hailey']

for user in new_users:
  if user in current_users or user.lower() in current_users or user.upper() in current_users or user.title() in current_users:
    print("Enter a new username")
  else:
    print("The username is available")
  
