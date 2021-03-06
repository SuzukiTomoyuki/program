#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

def main():
	SCREEN_SIZE = (640, 480)
	 
	pygame.init()
	screen = pygame.display.set_mode(SCREEN_SIZE)
	pygame.display.set_caption(u"draw image")
	 
	pythonImg = pygame.image.load("Funa01.png").convert_alpha()
	 
	while True:
	    screen.blit(pythonImg, (0,0))
	    pygame.display.update()
	    
	    for event in pygame.event.get():
	        if event.type == QUIT:
	            sys.exit()

if __name__ == '__main__':
	main()