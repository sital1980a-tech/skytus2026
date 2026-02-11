class MusicPlayer:
    def __init__(self, song):
        self.song = song

    def play(self):
        print(f"Playing song: {self.song} in default Music Player")


# Subclass
class Spotify(MusicPlayer):
    def __init__(self, song, playlist):

        super().__init__(song)
        self.playlist = playlist


    def play(self):
        print(f"Streaming '{self.song}' from Spotify playlist '{self.playlist}'")


# -------- Testing --------

player = MusicPlayer("Shape of You")
player.play()

print()

spotify_player = Spotify("Blinding Lights", "Top Hits 2025")
spotify_player.play()
