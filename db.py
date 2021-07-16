import touchphat
from pygame import mixer


@touchphat.on_touch("1")
def start():
    mixer.init()
    mixer.music.load('/home/pi/baby_goes_what_home/server/public/files/dream.mp3')
    mixer.music.play()
