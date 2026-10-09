#8-9. Messages: Make a list containing a series of short text messages. Pass
#the list to a function called show_messages(), which prints each text message.

#8-10. Sending Messages: Start with a copy of your program from Exercise
#8-9. Write a function called send_messages() that prints each text message and
#moves each message to a new list called sent_messages as it’s printed. After
#calling the function, print both of your lists to make sure the messages were
#moved correctly.

#8-11. Archived Messages: Start with your work from Exercise 8-10. Call
#the function send_messages() with a copy of the list of messages. After calling
#the function, print both of your lists to show that the original list has
#retained its messages.

messages = ["I love pizzas", "I am elia, what is your name?", "I love studying", "I love my brother"]
sent_messages = []

def show_messages(messages):
  for message in messages:
    print(message)
show_messages(messages)

def send_messages1(messages, sent_messages):
  while messages:
    sent_message = messages.pop()
    print(sent_message)
    sent_messages.append(sent_message)
send_messages1(messages, sent_messages)
print(messages)
print(sent_messages)

texts = ["I love pizzas", "I am elia, what is your name?", "I love studying", "I love my brother"]
sent_texts = []
send_messages1(texts[:], sent_texts)
print(texts)
print(sent_texts)
