def make_album(artist_name, album_title, album_track=''):
    if album_track:
        album = 'Name of the artist: '+artist_name.title() +'\nTitle: '+album_title.title()+'\nTrack: '+album_track
    else:
        album = 'Name of the artist: '+artist_name.title()+'\nTitle: '+album_title.title()
    return album

a = make_album('linkin park','it is so hard','21')
print(a)

print()
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)