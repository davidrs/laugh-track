import pygame
import time

allowMusic = 0

pygame.mixer.init()

def playMusic():
	if not pygame.mixer.music.get_busy():
	        pygame.mixer.music.load("laugh.mp3")
        	pygame.mixer.music.play()
	else:
		pygame.mixer.music.unpause()
        #pygame.mixer.music.load("rizzle.mp3")


while True:
	allowMusic = allowMusic - 1
	playMusic()
	time.sleep(15)
	pygame.mixer.music.pause()
	time.sleep(5)

