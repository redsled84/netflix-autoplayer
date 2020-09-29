#!/usr/bin/python
from time import sleep
from pyautogui import click

# If you're resolution is lower than the position coordinates,
# adjust them accordingly
position_x = 1127
position_y = 638

def netflix_autoplayer(episode_length):
    global position_x, position_y
    while True:               # infinite loop for infinite Netflix time
        sleep(episode_length) # wait until at least one episode has passed

        click(x=position_x, y=position_y)   # bring up the netflix playbar
        sleep(.5)                           # wait half a second so we don't exit fullscreen
        click(x=position_x, y=position_y)   # pause the show   
        sleep(.5)                           # wait half a second so we don't exit fullscreen
        click(x=position_x, y=position_y)   # resume the show

# Netflix has to be fullscreen and playing a TV show in order for this script
# to work as intended. I wouldn't use this on a movie because that would be
# redundant dude.
if __name__ == "__main__":
    # enter the length of one episode in seconds
    episode_length = 1320 # 22 minutes
    netflix_autoplayer(episode_length)
