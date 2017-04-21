def make_album(name_artist, name_album, num_track=''):
    album = {'artist': name_artist, 'album': name_album}
    prompt = album['artist'] + " - " + album['album']
    if num_track:
        album['track'] = num_track
        prompt += ", " + album['track'] + ' tracks'
    print(prompt)


make_album('girugamesh', '13')
make_album('queen', 'jazz', '13')
make_album('joe satriani', 'time machine')
while True:
    print("\nMake album: ")
    print("(enter 'q' at any time to quit) ")
    n_artist = input("Name artist: ")
    if n_artist == 'q':
        break
    n_album = input("Name album: ")
    if n_album == 'q':
        break
    n_track = input("Number of tracks: ")
    if n_track == 'q':
        break
    make_album(n_artist, n_album, n_track)
