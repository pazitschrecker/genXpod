# Creative Embedded Systems: Module 2 (Interactive Devices)

This project contains a python script and an ESP32 Arduino script. The Arduino script should be run by an ESP32 plugged into a Raspberry Pi. There are also a number of other components to attach (push buttons, switch, etc.). These are detailed in the "Physical Setup" section of this ReadMe. The project is also contained in an interactive cardboard enclosure that resembles a large iPod and plays music. A video of the full project can be viewed on YouTube: https://www.youtube.com/watch?v=bYVhDSd7Jqo&feature=youtu.be

# Dependencies
This project requires the Arduino IDE to run. I recommend following this tutorial https://www.raspberrypi-spy.co.uk/2020/12/install-arduino-ide-on-raspberry-pi/ for Raspberry pi 4.

Download the Linux ARM 32-bit version of the Arduino IDE from the official website: https://www.arduino.cc/en/software

This project also requires Pygame. This can be installed on the Raspberry pi by typing the following into the command line:

`sudo apt-get install python-pygame`

This project also requires Serial. This can be installed on the Raspberry pi by typing the following into the command line:

`sudo apt-get install python-serial`

Lastly, this project uses an i2c LCD display. This may also require some installations and onto the Raspberry pi, as well as some changes to existing settings. 

To enable the i2C interface on the Raspberry pi, follow this tutorial using raspi-config from the command line: https://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi/ (steps also detailed below)
In the command line, type: 
`sudo raspi-config`
Select: Interfacing Options --> I2C and select <Yes> when asked if you would like the ARM I2c interface to be enabled. 
  Then reboot the raspberry pi: `sudo reboot`

# Physical Setup
This project uses a large number of physical components. First, set up the ESP32 by plugging it into the GPIO Extender and then into a breadboard. 

Plug the button you plan to use for pause/play functionality into GPIO port 13. Connect the other side of the button to ground.
Plug the button you plan to use for "power" functionality into port 33. Connect the other side of the button to ground. 
Plug the middle and left pins of the switch into the breadboard using M-F wires. Now connect the middle wire to ground via another wire in series. Connect the left side to GPIO port 4. 

Lastly, use 3 M-F wires to connect the soft touch sensor to the bread board. Connect one side to ground via a 10K resistor in series. Connect the other side to 3.3V power via another 10K resistor in series. Lastly, connect the middle pin to GPIO port 2. 

The i2c LCD is plugged into the Raspberry Pi only. The GND port is plugged into the Raspberry pi's ground pin. The VCC is plugged into a 5V GPIO pin on the Raspberry Pi. SDA is plugged into GPIO 2 and SCL is plugged into GPIO 3.

A smaller speaker is also connected to the Raspberry pi's audio port.

Plug the ESP32 into the Raspberry pi via a cable that allows data transition (not just power).

# A note on songs
This project plays music and therefore requires downloaded .wav files. I have not included these in the repository because they are copyrighted materials. In order for your songs to work with the code, do the following:
Create a folder in the same location or directory as the python script and call this "songs". Within the songs directory, add the corresponding songs as 6 .wav files with the following names: 
- cindi_gjwhf.wav (corresponds to Cindi Lauper's "Girls Just Want to Have Fun")
- bonnie_teoth.wav (corresponds to Bonnie Tyler's "Total Eclipse of the Heart")
- tiffany_itwan.wav (corresponds to Tiffany's "Girls Just Want to Have Fun")
- abba_dq.wav (corresponds to Abba's "Dancing Queen")
- queen_watc.wav (corresponds to Queens's "We are the Champions")
- bowie_itlom.wav (corresponds to David Bowie's "Life on Mars?")

