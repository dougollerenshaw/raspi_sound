from gtts import gTTS
import time
import os 
import vlc
from mutagen.mp3 import MP3

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
    # # time.sleep(0.25)
    # os.system("vlc temp.mp3")
    # os.system("quit")

    audio = MP3("temp.mp3")
    player = vlc.MediaPlayer("temp.mp3")
    player.play()
    print('playing...should be {} seconds'.format(audio.info.length))
    time.sleep(audio.info.length)
    print('done.')
    player.stop()



if __name__ == '__main__':
    print('')
    play_sound(raw_input('what do you want to say? '))
    print('')
