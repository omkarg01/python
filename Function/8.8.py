def make_album(artist_name, album_title):
    #if album_track:
       # album = 'Name of the artist: '+artist_name.title()+'Title: '+album_title.title()
    #else:
    album = '\nName of the artist: '+artist_name.title()+'\nTitle: '+album_title.title()
    return album
while True:
    print('\nGive the following information: ')
    print("(enter 'q' at any time to quit)")

    art_name = input('Artist name: ')
    if art_name == 'q':
        break

    alb_title = input('Album title: ')
    if alb_title == 'q':
        break

    a = make_album(art_name, alb_title)
    print(a)

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
         break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")