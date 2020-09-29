#!/usr/bin/python
from time import sleep
from pyautogui import click

# If you're resolution is lower than the position coordinates,
# adjust them accordingly
position = (x=1127, y=638)

def autoplay_netflix(episode_length):
    global position
    while True:               # infinite loop for infinite Netflix time
        sleep(episode_length) # wait until at least one episode has passed
        click(position)       # pause the show
        sleep(1)              # wait one second so we don't exit fullscreen
        click(position)       # resume the show

# Netflix has to be fullscreen and playing a TV show in order for this script
# to work as intended. I wouldn't use this on a movie because that would be
# redundant dude.
if __name__ == "__main__":
    # enter the length of one episode in seconds
    episode_length = 1320 # 22 minutes
    autoplay_netflix(episode_length)
