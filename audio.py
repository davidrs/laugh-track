import time
import pygame
pygame.mixer.init()

# Plays a laugh track.     
def play_laugh():
#    if not pygame.mixer.music.get_busy():
    pygame.mixer.music.load("laugh.mp3")
    pygame.mixer.music.play()
 #   else:
 #   	pygame.mixer.music.unpause()

    time.sleep(4)
    pygame.mixer.music.pause()


def play_applause():
#    if not pygame.mixer.music.get_busy():
    pygame.mixer.music.load("applause.mp3")
    pygame.mixer.music.play()
 #   else:
  #  	pygame.mixer.music.unpause()
    time.sleep(4)
    pygame.mixer.music.pause()
