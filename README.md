# laugh-track
Plays laugh track from raspi when button pushed or site visited.

Set volume on raspi:
amixer cset numid=1 -- -100

## Design doc
 - audio.py  # Plays the audio file
 - button.py # listens for the button press
 - server.py # Runs a small server, visits to the page trigger audio file


## Material
 - Raspi B+
 - Speaker
 - Button
