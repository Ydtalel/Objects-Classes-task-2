class Track:

    def __init__(self, track_name, track_duration):
        self.track_name = track_name
        self.track_duration = track_duration

    def show(self, ):
        return f"-='{self.track_name}' - {self.track_duration} мин.=-"


class Album(Track):
    def __init__(self, album_name, band_name):
        self.album_name = album_name
        self.band_name = band_name
        self.track_list = []

    def get_tracks(self):
        print(f"_____{self.album_name}______")
        for track in self.track_list:
            print(track.show())
        print()

    def add_track(self, track):
        self.track_list.append(track)

    def get_album_duration(self):
        time = 0
        for duration in self.track_list:
            time += duration.track_duration
        return f"Длительность песен альбома '{self.album_name}' составляет: {time} мин.\n"
