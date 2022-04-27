#!/usr/bin/env python3

import sys, pygame
pygame.init()

width, height = 600, 600
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode((width, height))


player = pygame.image.load("./learn_linux/weird_donkey.png")
player_rect = player.get_rect()
player_pos = [250, 250]
dist = 50

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_pos[1] -= dist
            if event.key == pygame.K_DOWN:
                player_pos[1] += dist
            if event.key == pygame.K_LEFT:
                player_pos[0] -= dist
            if event.key == pygame.K_RIGHT:
                player_pos[0] += dist


    screen.fill(black)
    for i in range(5):
        for j in range(5):
            pygame.draw.line(screen, white, (0, i*width/5), (width, i*width/5))
            pygame.draw.line(screen, white, (j*height/5, 0), (j*height/5, height))
    screen.blit(player, player_pos)
    pygame.display.flip()

