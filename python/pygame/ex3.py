#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
 
SCR_RECT = Rect(0, 0, 640, 480)
 
def load_image(filename, colorkey=None):
    try:
        image = pygame.image.load(filename)
    except pygame.error, message:
        print "Cannot load image:", filename
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image
 
def split_image(image, y_im):
    imageList = []
    for i in range(0, 160, 40):
        surface = pygame.Surface((40,70))
        surface.blit(image, (0,0), (i, y_im, 40, 70))
        surface.set_colorkey(surface.get_at((0,0)), RLEACCEL)
        surface.convert()
        imageList.append(surface)
    return imageList
 
class Character(pygame.sprite.Sprite):
    animcycle = 12 
    frame = 0
    def __init__(self, filename, x, y, y_im):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images = split_image(load_image(filename), y_im)
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=(x,y))
    def update(self):
        self.frame += 1
        self.image = self.images[self.frame/self.animcycle%4]
 
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCR_RECT.size)
    pygame.display.set_caption(u"Walk")
 
    all = pygame.sprite.RenderUpdates()
    Character.containers = all
    
    player = Character("Funa01.png", 45, 140, 0)
    
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        screen.fill((0,0,255))
        all.update()
        all.draw(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT: sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: sys.exit()
                if event.key == K_DOWN:
                    player.move_ip(0, 10)
 
if __name__ == "__main__":
    main()