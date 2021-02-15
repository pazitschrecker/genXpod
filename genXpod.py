# https://linuxconfig.org/how-to-play-audio-with-vlc-in-python
# https://gist.github.com/santolucito/dd0b68edd6f8c64aaf89e59f2d8c3f00
# https://www.instructables.com/Ribbon-Sensor-and-Arduino/

from pygame import mixer
import random
import serial
import sys
import time
import smbus

#select the correct port and baud rate 
s = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)
order = ['songs/cindi_gjwhf.wav', 'songs/bonnie_teoth.wav', 'songs/tiffany_itwan.wav']
playlist = ['songs/cindi_gjwhf.wav', 'songs/bonnie_teoth.wav', 'songs/tiffany_itwan.wav']
val = "0"
powerOn = 0
songTitles = {
    'songs/cindi_gjwhf.wav': ["Girls Just Want", "to Have Fun"],
    'songs/bonnie_teoth.wav': ["Total Eclipse", "of the Heart"],
    'songs/tiffany_itwan.wav': ["I Think We're", "Alone Now"]
}

'''* * * * * * * * * * * * * * * START BUS CODE * * * * * * * * * * * * * * *'''

# Define some device parameters
I2C_ADDR  = 0x27 # I2C device address
LCD_WIDTH = 16   # Maximum characters per line

# Define some device constants
LCD_CHR = 1 # Mode - Sending data
LCD_CMD = 0 # Mode - Sending command

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line

LCD_BACKLIGHT  = 0x08  # On
#LCD_BACKLIGHT = 0x00  # Off

ENABLE = 0b00000100 # Enable bit

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

#Open I2C interface
#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1
time.sleep(1)

def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off 
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  #time.sleep(E_DELAY)

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = the data
  # mode = 1 for data
  #        0 for command

  bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
  bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT

  # High bits
  
  bus.write_byte(I2C_ADDR, bits_high)
  lcd_toggle_enable(bits_high)
  
  # Low bits
  bus.write_byte(I2C_ADDR, bits_low)
  lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
  # Toggle enable
  time.sleep(E_DELAY)
  bus.write_byte(I2C_ADDR, (bits | ENABLE))
  time.sleep(E_PULSE)
  bus.write_byte(I2C_ADDR,(bits & ~ENABLE))
  time.sleep(E_DELAY)

def lcd_string(message,line):
  # Send string to display

  message = message.ljust(LCD_WIDTH," ")

  lcd_byte(line, LCD_CMD)

  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)


'''if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd_byte(0x01, LCD_CMD)
    '''

'''* * * * * * * * * * * * * * * END BUS CODE * * * * * * * * * * * * * * *'''

paused = 0
currSong = 0
display = ""

mixer.init()
lcd_init()

def playSong(i):
    if i >= len(playlist) or i < 0:
        currSong = 0
        i = 0
    mixer.music.load(playlist[i]) 
    mixer.music.set_volume(0.7) 
    mixer.music.play()
    print("playing: ", playlist[i])
    display = songTitles[playlist[i]]
    lcd_string(display[0],LCD_LINE_1)
    lcd_string(display[1],LCD_LINE_2)

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
        if (powerOn == 1 and val == "8"):
            powerOn = 0
            
        while (powerOn == 0):
            ser_bytes = s.readline()
            print("ser_bytes: ", ser_bytes)
            val = str(ser_bytes)[5:6]
            if val == "8":
                powerOn = 1
                playSong(currSong)
        

        if ((mixer.music.get_busy() == 1) or paused == 1):
            ser_bytes = s.readline()
            print("ser_bytes: ", ser_bytes)
            val = str(ser_bytes)[5:6] # state
            print("val: ", val)
            
            lcd_string(display,LCD_LINE_1)
            print(playlist)
            
            if(paused == 1 and (val == "0" or val == "1")):
                paused = 0
                mixer.music.unpause() 
                print("unpausing: ",val)
                
            
            elif (val == "0"):
                print("val was 0")
                orderSongs()
                currSong = 0
                playSong(currSong)
            
            elif (val == "1"):
                print("val was 1")
                shuffleSongs()
                currSong = 0
                playSong(currSong)

            elif(val == "2" or val == "3"):
                print("paused")
                paused = 1
                #if (mixer.music.get_busy() == 1):
                mixer.music.pause() 

            elif val == "4":
                print("PREV")
                currSong = currSong-1
                print(currSong)
                playSong(currSong)
                #lcd_string(display,LCD_LINE_1)
            elif val == "5":
                print("NEXT")
                currSong = currSong+1
                print(currSong)
                playSong(currSong)
                #lcd_string(display,LCD_LINE_1)
            else:
                break
            
    except:
        print("gave up")
        print(sys.exc_info()[0])
        break