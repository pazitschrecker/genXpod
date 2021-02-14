# https://linuxconfig.org/how-to-play-audio-with-vlc-in-python
# https://gist.github.com/santolucito/dd0b68edd6f8c64aaf89e59f2d8c3f00
# https://www.instructables.com/Ribbon-Sensor-and-Arduino/

from pygame import mixer
import random
import serial
import sys
import time

#select the correct port and baud rate 
s = serial.Serial(port='/dev/tty.usbserial-1420', baudrate=9600)
order = ['songs/cindi_gjwhf.mp3', 'songs/bonnie_teoth.mp3', 'songs/tiffany_itwan.mp3']
playlist = ['songs/cindi_gjwhf.mp3', 'songs/bonnie_teoth.mp3', 'songs/tiffany_itwan.mp3']
val = "0"

paused = 0
currSong = 0

mixer.init() 

def playSong(i):
    if i >= len(playlist) or i < 0:
        currSong = 0
        i = 0
    mixer.music.load(playlist[i]) 
    mixer.music.set_volume(0.7) 
    mixer.music.play()
    print("playing: ", playlist[i])

def shuffleSongs():
    random.shuffle(playlist)

def orderSongs():
    for i in range(0, len(playlist)):
        playlist[i] = order[i]

def playSongs():
    while True:
        playSong(currSong)
        while (mixer.music.get_busy() == 1 or paused == 1):
            continue
        currSong = currSong+1

while True:
    try:
        playSong(currSong)

        if ((mixer.music.get_busy() == 1 and val != "b" and val != "n") or paused == 1):
            ser_bytes = s.readline()
            print("ser_bytes: ", ser_bytes)
            val = str(ser_bytes)[5:6] # state
            print("val: ", val)

            if(paused == 1 and (val == "0" or val == "1")):
                paused = 0
                mixer.music.unpause() 
                print("unpausing: ",val)
                
            
            elif (val == "0"):
                orderSongs()
                currSong = 0
                playSong(currSong)
            
            elif (val == "1"):
                shuffleSongs()
                currSong = 0
                playSong(currSong)

            elif(val == "2" or val == "3"):
                paused = 1
                if (mixer.music.get_busy() == 1): 
                    mixer.music.pause() 

        if val == "4":
            currSong = currSong-1
            playSong(currSong)
        elif val == "5":
            currSong = currSong+1
            playSong(currSong)
            
    except:
        print("gave up")
        print(sys.exc_info()[0])
        break