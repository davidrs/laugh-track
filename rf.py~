import time
import pygame
pygame.mixer.init()

# Plays a laugh track.     
def play_laugh():
    print "HAHAHAHHA"
    if not pygame.mixer.music.get_busy():
    	pygame.mixer.music.load("laugh.mp3")
    	pygame.mixer.music.play()
    else:
    	pygame.mixer.music.unpause()

    time.sleep(6)
    pygame.mixer.music.pause()
