# class Song:
#     count = 0
#     artists = []
#     genres = []
#     artist_count = {}
#     genre_count = {}

#     def __init__(self, name, artist, genre):
#         self.name = name
#         self.artist = artist
#         self.genre = genre

#         Song.count += 1
#         Song.artists.append(artist)
#         Song.genres.append(genre)

#         # Update genre count
#         if genre in Song.genre_count:
#             Song.genre_count[genre] += 1
#         else:
#             Song.genre_count[genre] = 1

#         # Update artist count
#         if artist in Song.artist_count:
#             Song.artist_count[artist] += 1
#         else:
#             Song.artist_count[artist] = 1


# Mop = Song('Mop', "Young Thug", "Rap")
# print(Mop.artist)


# print(Song.artists)

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

        # Update tracking stats
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
