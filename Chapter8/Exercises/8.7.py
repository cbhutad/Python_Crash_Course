def make_album(artist_name, title, number_of_songs=None):

    album = {
        "artist" : artist_name.title(),
        "title" : title.title()
    }
    if number_of_songs != None:
        album["number_of_songs"] = number_of_songs

    return album

print(make_album(title="illmatic", artist_name="nas"))
print(make_album(title="capital_punishment", artist_name="big pun", number_of_songs= 7))