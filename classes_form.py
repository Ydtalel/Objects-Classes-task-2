class Track:
    def __init__(self, track_name, track_duration):
        self.track_name = track_name
        self.track_duration = track_duration

    def __gt__(self, other):
        return self.track_duration > other.track_duration

    def __lt__(self, other):
        return self.track_duration < other.track_duration

    def __str__(self):
        return f"{self.track_name} - {self.track_duration} min."


class Album(Track):
    def __init__(self, album_name, band_name):
        self.album_name = album_name
        self.band_name = band_name
        self.track_list = []

    def __str__(self):
        print(f" Name group: {self.band_name}\n Name album: {self.album_name} \n Tracks:")
        album = ''
        for track in self.track_list:
            album += f"\t{track.track_name} - {track.track_duration} min.\n"
        return album

    def add_track(self, track):
        self.track_list.append(track)

    def get_album_duration(self):
        time = 0
        for duration in self.track_list:
            time += duration.track_duration
        return f"{self.album_name}'s duration is: {time} min.\n"
