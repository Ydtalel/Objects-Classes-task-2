from classes_form import *

track_1 = Track("Master of Puppets", 8.36)
track_2 = Track("Welcome Home (Sanitarium)", 6.28)
track_3 = Track("Battery", 5.13)

track_4 = Track("Disposable Heroes", 8.17)
track_5 = Track("The Thing That Should Not Be", 6.37)
track_6 = Track("Damage, Inc.", 5.30)

album_1 = Album("album_1", "Metallica")
album_2 = Album("album_2", "Metallica")

album_1.add_track(track_1)
album_1.add_track(track_2)
album_1.add_track(track_3)

album_2.add_track(track_4)
album_2.add_track(track_5)
album_2.add_track(track_6)

album_1.get_tracks()
album_2.get_tracks()
print(album_1.get_album_duration())
print(album_2.get_album_duration())
