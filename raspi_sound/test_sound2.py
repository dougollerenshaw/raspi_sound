from pygame import mixer
import time
mixer.init()
mixer.music.load('./temp.mp3')

for i in range(1):
    mixer.music.play()

    time.sleep(2)