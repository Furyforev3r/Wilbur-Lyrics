import random
from random import choice
from time import sleep
from plyer import notification
from lyrics import songs

while True:
    song = choice(list(songs.keys()))
    Lyrics = choice(songs[song]["lyrics"])
    notification.notify(
        title=f'♡ | {songs[song]["title"]} - {songs[song]["author"]}!',
        message=Lyrics,
        app_icon=songs[song]["icon"],
        timeout=60,
    )
    print(Lyrics)
    sleep(120)
