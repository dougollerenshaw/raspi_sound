from gtts import gTTS
from pygame import mixer
from mutagen.mp3 import MP3
import time
import os 

def play_sound(mytext):
    # The text that you want to convert to audio 
    mytext = mytext
    
    # Language in which you want to convert 
    language = 'en'
    
    # Passing the text and language to the engine,  
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  ls

    # have a high speed 
    myobj = gTTS(text=mytext, lang=language, slow=False) 

    # Saving the converted audio in a mp3 file named 
    # welcome  
    myobj.save("temp.mp3") 

    mixer.init()
    mixer.music.load('./temp.mp3')

    audio = MP3('./temp.mp3')
    print(audio.info.length)

    mixer.music.play()
    time.sleep(audio.info.length)

if __name__ == '__main__':
    play_sound(input('what do you want to say? '))