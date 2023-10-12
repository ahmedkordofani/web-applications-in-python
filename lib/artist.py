class Artist:
    def __init__(self):
        self.artists = []

    def add_artist(self, name, genre):
        self.artists.append({'name': name, 'genre': genre})

    def get_artists(self):
        return self.artists
