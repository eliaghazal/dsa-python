def make_shirt(size, text):
  #The function should print a sentence summarizing the size of the shirt and the message printed on it.
  print(f"The size of the shirt is {size.upper()}.\nThe message printed on it is: {text}")
make_shirt("L", "I love food!")
make_shirt(text = "I love food!", size = "L")

# Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
def make_shirt(size = "L", text = "I love Python"):
    print(f"The size of the shirt is {size.upper()}.\nThe message printed on it is: {text}")

make_shirt()
make_shirt("M")
make_shirt("S", "I love programming!")
  
