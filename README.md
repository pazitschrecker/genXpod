# Creative Embedded Systems: Module 2 (Interactive Devices)

This project contains a python script and an ESP32 Arduino script. The Arduino script should be run by an ESP32 plugged into a Raspberry Pi. There are also a number of other components to attach (push buttons, switch, etc.). These are detailed in the "Physical Setup" section of this ReadMe. The project is also contained in an interactive cardboard enclosure that resembles a large iPod and plays music. A video of the full project can be viewed on YouTube: https://www.youtube.com/watch?v=bYVhDSd7Jqo&feature=youtu.be

# Dependencies
This project requires the Arduino IDE to run. I recommend following this tutorial https://www.raspberrypi-spy.co.uk/2020/12/install-arduino-ide-on-raspberry-pi/ for Raspberry pi 4.

Download the Linux ARM 32-bit version of the Arduino IDE from the official website: https://www.arduino.cc/en/software

# Physical Setup
This project uses a large number of physical components. First, set up the ESP32 by plugging it into the GPIO Extender and then into a breadboard. 

Plug the button you plan to use for pause/play functionality into port 26. Plug the "power" button into port 35.
For each button, attach the button to the breadboard. On one side of the button, attach one end of a 10 ohm resistor in the same row as a button pin and the other end to 3.3 A power. Attach two wires, one to each row with a button pin to GROUND. Lastly, attach another 10 ohm resistor to the remaining row with a button pin and attach the other end of this resistor to the correct port (26 or 35, respectively).

Plug the switch into port 4.
Plug the Circular Pentiometer into port 2.
