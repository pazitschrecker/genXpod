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

Plug the button you plan to use for pause/play functionality into port 26. Plug the "power" button into port 35.
For each button, attach the button to the breadboard. On one side of the button, attach one end of a 10 ohm resistor in the same row as a button pin and the other end to 3.3 A power. Attach two wires, one to each row with a button pin to GROUND. Lastly, attach another 10 ohm resistor to the remaining row with a button pin and attach the other end of this resistor to the correct port (26 or 35, respectively).

The i2c LCD is plugged into the Raspberry Pi only. The 
Plug the switch into port 4.
Plug the Circular Pentiometer into port 2.
