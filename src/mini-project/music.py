import webbrowser

class Music():
    """
    This class provides a way to store music information 
    """
    VALID_RATINGS = ["A", "B", "C"]

    def __init__(self, music_name, music_url):
        self.music_name = music_name
        self.music_url = music_url

    def play_music(self):
        webbrowser.open(self.music_url)

def main():
    better_together = Music("better together", "https://www.youtube.com/watch?v=u57d4_b_YgI")
    better_together.play_music()
    print (Music.VALID_RATINGS)
    print (Music.__doc__)

if __name__ == '__main__':
    main()