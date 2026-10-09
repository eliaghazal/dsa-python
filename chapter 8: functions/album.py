#Album: Write a function called make_album() that builds a dictionary
#describing a music album. The function should take in an artist name and an
#album title, and it should return a dictionary containing these two pieces of
#information. Use the function to make three dictionaries representing
#different albums. Print each return value to show that the dictionaries are
#storing the album information correctly.
#Use None to add an optional parameter to make_album() that allows you to
#store the number of songs on an album. If the calling line includes a value
#for the number of songs, add that value to the album’s dictionary. Make at
#least one new function call that includes the number of songs on an album

#8-8. User Albums: Start with your program from Exercise 8-7. Write a whileloop that allows users to enter an album’s artist and title. Once you have
#that information, call make_album() with the user’s input and print the
#dictionary that’s created. Be sure to include a quit value in the while loop.

def make_album(artist, title, song_number = None):
  album = {"artist": artist.title(), "title": title.title()}
  if song_number:
    album["song_number"] = song_number
  return album
print(make_album("taylor swift", "midnights", "13"))
print(make_album("taylor swift", "folklore"))
print(make_album("taylor swift", "reputation"))
print(make_album("taylor swift", "red"))

while True:
    print("\nEnter 'quit' at any time to stop.")
    artist = input("Enter the artist's name: ")
    if artist == 'quit':
        break
    title = input("Enter the album's title: ")
    if title == 'quit':
        break
    song_number = input("Enter the number of songs (optional): ")
    if song_number == 'quit':
        break
    if song_number:
        album = make_album(artist, title, song_number)
    else:
        album = make_album(artist, title)
    print(album)




    
  
