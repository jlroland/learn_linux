#!/usr/bin/env python3

import sys
import pygame as pg
import questions as quest
pg.init()


width, height = 600, 600
grid_size = 3
black = 0, 0, 0
white = 255, 255, 255

screen = pg.display.set_mode((width, height))


player = pg.image.load("./weird_donkey.png")
player_rect = player.get_rect()
player_pos = [250, 250]
dist = 50

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            sys.exit()
        if event.type == pg.KEYDOWN or event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                player_pos[1] -= dist
            if event.key == pg.K_DOWN:
                player_pos[1] += dist
            if event.key == pg.K_LEFT:
                player_pos[0] -= dist
            if event.key == pg.K_RIGHT:
                player_pos[0] += dist


    screen.fill(black)
    font = pg.font.Font(None, 28)
    text = font.render("Question here", True, white)
    textpos = text.get_rect(centerx=screen.get_width() / 2, y=10)
    screen.blit(text, textpos)
    for i in range(grid_size):
        for j in range(grid_size):
            grid_box = pg.Rect(i*width/grid_size, j*width/grid_size, width/grid_size, height/grid_size)
            pg.draw.rect(screen, white, grid_box, 1)
            font = pg.font.Font(None, 28)
            text = font.render("answer here", True, white)
            #text_box = pg.Rect(i*width*0.5/grid_size, j*width*0.5/grid_size, width/grid_size, height/grid_size)
            #textpos = text.get_rect(centerx=grid_box.get_width() / 2, y=10)
            screen.blit(text, grid_box)
   
    # font = pg.font.Font(None, 64)
    # text = font.render("Pummel The Chimp, And Win $$$", True, white)
    # textpos = text.get_rect(centerx=screen.get_width() / 2, y=10)
    # screen.blit(text, textpos)
    screen.blit(player, player_pos)
    pg.display.flip()



 # for i in range(grid_size):  
    #     pg.draw.line(screen, white, (0, i*width/grid_size), (width, i*width/grid_size))       
    # for j in range(grid_size):
    #     pg.draw.line(screen, white, (j*height/grid_size, 0), (j*height/grid_size, height))