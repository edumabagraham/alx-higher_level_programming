#!/usr/bin/python3
import random

def shuffle_music(arr):
    while True:
        if len(arr) == 1:
            print(arr[0])
            break
        else:
            random_num = random.randrange(0, len(arr))
            song = arr[random_num]
            arr.pop(random_num)
            print(song,arr)

songs = ["blessed", "yes", "nazarene","jireh"]
shuffle_music(songs)
# print(shuffle_music(songs))