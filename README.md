# raspi_sound
utilities for raspberry pi sound

Requires Google's text to voice
'''
    pip install gTTS
'''

requires VLC:
'''
    pip install python-vlc
'''

Requires mutagen:
'''
    pip install mutagen
'''

I got this error on the first run:
```
vlcpulse audio output error: PulseAudio server connection failure: Connection refused
```
The following command fixed it:
```
sudo apt-get --purge --reinstall install pulseaudio
```