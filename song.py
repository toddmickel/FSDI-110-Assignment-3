class Song:

    def __init__(self, id, track_num, song_title, length_secs):
        self.id = id
        self.track_num = track_num
        self.song_title = song_title
        self.length_secs = length_secs

    def __str__(self):
        return f"ID {self.id}: {self.track_num} - {self.song_title} - {self.length_secs} sec"
