import numpy as np
from play_sound import play_sound
import time

def compliment_machine(name,N):
    
    adjectives = [
        'cute',
        'strong',
        'funny',
        'fg',
        'schmooga',
        'lovely',
        'five years old',
        'mnbvcxzertyui',
        'a really good piano player',
    ]

    time.sleep(0.1)
    for i in range(int(N)):
        text = '{} is {}!'.format(name,np.random.choice(adjectives))
        
        # time.sleep(0.25)
        print(text)
        # time.sleep(0.1)
        play_sound(text)
        play_sound("I'm going to compliment {} {} more times".format(name,int(N)-i-1))
        # time.sleep(0.25)

if __name__ == '__main__':
    print('')
    name = 'Elliott'
    N = input('how many times do you want to say {}? '.format(name))
    print('\n')
    compliment_machine(name,N)