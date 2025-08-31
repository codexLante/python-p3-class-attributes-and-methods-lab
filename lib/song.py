class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment total song count
        Song.count += 1

        # Track genres
        if genre not in Song.genres:
            Song.genres.append(genre)
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1

        # Track artists
        if artist not in Song.artists:
            Song.artists.append(artist)
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1

s1 = Song("99 Problems", "Jay Z", "Rap")
s2 = Song("Halo", "Beyonce", "Pop")

print(Song.count)          # 2
print(Song.genres)         # ['Rap', 'Pop']
print(Song.artists)        # ['Jay Z', 'Beyonce']
print(Song.genre_count)    # {'Rap': 1, 'Pop': 1}
print(Song.artist_count)   # {'Jay Z': 1, 'Beyonce': 1}