#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 480))
font = pygame.font.Font(None, 48)
clock = pygame.time.Clock()

start = None
done = False
while not done:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or
            getattr(event, 'key', None) == pygame.K_ESCAPE):
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if start:
                time = pygame.time.get_ticks() - start
                color = (random.randint(0, 255),
                         random.randint(0, 255),
                         random.randint(0, 255))
                screen.fill(color)
                screen.blit(font.render(str(time), True, (255-color[0],
                                                          255-color[1],
                                                          255-color[2])), (0, 0))
                print time
                start = None
            else:
                start = pygame.time.get_ticks()

        if start and pygame.time.get_ticks() - start > 900:
            start = None

    pygame.display.update()
    clock.tick(60)
