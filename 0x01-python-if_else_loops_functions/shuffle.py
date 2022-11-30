#!/usr/bin/python3

from random import random
import random

def shuffle(songs):
    while(len(songs) > 0):
        next_song = random.randint(0, len(songs) - 1)
        print(songs[next_song])
        songs.remove(songs[next_song])

songs=["dfa","fad","read","sad","gad"]
shuffle(songs)