class Song:

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
            return self.title
        
    name = property(get_title)

class Album:

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "various artists"
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)


class Artist():
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)

    def add_song(self, name, year, title):
        album_found = find_object(name, self.albums)
        if album_found is None:
            print(name + " Not found")
            album_found = Album(name, year, self.name)
            self.add_album(album_found)
        else:
            self.add_album(album_found)
            print("Found album: "+ name)
        
        album_found.add_song(title)


def find_object(field, object_list):
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    artist_list = []

    with open("OOP_IN_PYTHON/albums.txt",'r') as albums:
        for line in albums:
            artist_, album_, year_, song_ = tuple(line.strip('\n').split('\t'))
            year_ = int(year_)
            print(artist_, album_, year_, song_,sep=':')

            new_artist = find_object(artist_, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_)
                artist_list.append(new_artist)
            new_artist.add_song(album_, year_, song_)
    return artist_list


def create_checkfile(artist_list):
    with open("OOP_IN_PYTHON/checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{2.title}" .format(new_artist, new_album, new_song), file=checkfile)


if __name__ == "__main__":
    artists = load_data()
    print("There are {} artists " .format(len(artists)))
 
    create_checkfile(artists)


