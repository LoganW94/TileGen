
import pygame
from handler import Handler
from app import App

pygame.init()

clock = pygame.time.Clock()
FPS = 60 # once up and running try owering to 30 for performance

h = Handler()
a = App(h)

def start():

	gameExit = False

	while not gameExit:

		h.update(a.get_current_state())
		
		h.draw()

		pygame.display.update()
		clock.tick(FPS)

start()	