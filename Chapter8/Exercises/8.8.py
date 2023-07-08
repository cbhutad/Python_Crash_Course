def make_album(artist_name, title, number_of_songs=None):

    album = {
        "artist" : artist_name.title(),
        "title" : title.title()
    }
    if number_of_songs != None:
        album["number_of_songs"] = number_of_songs

    return album

while True:

    artist = input("Enter artist name : ")
    title = input("Enter album title : ")
    number_of_songs = int(input("Enter number of songs : (0 is allowed)"))

    if number_of_songs != 0:
        print(make_album(title=title, number_of_songs=number_of_songs, artist_name=artist))
    else:
        print(make_album(title=title, artist_name=artist))

    choice = input("Do you want to continue : (enter yes or no)\n")
    if choice.lower() == "no":
        break

