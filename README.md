# laugh-track
Plays laugh track from raspi when button pushed or site visited.

Set volume on raspi:
amixer cset numid=1 -- -100

## Setup

Pin 7, (Bottom right non nick's pi) is for the manual tinfoil switch.
Pin 17 for the Data on the transmitter.

Original Raspi Wireless article:
https://www.samkear.com/hardware/control-power-outlets-wirelessly-raspberry-pi

## Design doc
 - audio.py  # Plays the audio file
 - button.py # listens for the button press
 - server.py # Runs a small server, visits to the page trigger audio file


## Material
 - Raspi B+
 - Speaker
 - Button
