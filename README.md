# laugh-track
Plays laugh track from raspi when button pushed or site visited.

Set volume on raspi:
amixer cset numid=1 -- -100

## Setup

To scan for  RF numbers put the wire in Pin 22, just below Pin 17, 7th one down on the left of RaspiB)
Then run sudo ./RFScanner



Pin 7, (Bottom right on Raspi B) is for the manual tinfoil switch.

Pin 17 for the Data on the transmitter. (6th down on the left on Raspi B)

Original Raspi Wireless article:
https://www.samkear.com/hardware/control-power-outlets-wirelessly-raspberry-pi

Pin locations:
https://www.google.com/search?q=pin+17+raspi+b&espv=2&biw=1436&bih=702&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj68oTq47_NAhUC7GMKHcIMB5IQ_AUIBigB#imgrc=oSXvaM-s5hJm8M%3A

Visit:
<ip of raspi>:8000/client/index.html

## Design doc
 - audio.py  # Plays the audio file
 - button.py # listens for the button press
 - server.py # Runs a small server, visits to the page trigger audio file


## Material
 - Raspi B+
 - Speaker
 - Button
