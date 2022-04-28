#!/usr/bin/env python3

import sys
import pygame as pg
#import numpy as np
import questions as quest
pg.init()

width, height = 600, 600
grid_size = 3
black = 0, 0, 0
white = 255, 255, 255

screen = pg.display.set_mode((width, height))

player = pg.image.load("./weird_donkey.png")
player_rect = player.get_rect()
player_pos = [width/2, height/2]
dist = width/grid_size

answers = quest.answer_shuffle(quest.level1, grid_size)

def select_answer():
    i, j = 0, 0
    if player_pos[0] == 300:
        j = 1
    elif player_pos[0] == 500:
        j = 2
    if player_pos[1] == 300:
        i = 1
    elif player_pos[1] == 500:
        i = 2
    
    chosen_answer = answers[j,i]   # text loop went wonky?
    if chosen_answer in quest.level1["correct_answers"]:
        print("Correct!")
    elif chosen_answer == 'Start':
        print("What are you doing?")
    else:
        print("Wrong!")

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                player_pos[1] -= dist
            if event.key == pg.K_DOWN:
                player_pos[1] += dist
            if event.key == pg.K_LEFT:
                player_pos[0] -= dist
            if event.key == pg.K_RIGHT:
                player_pos[0] += dist
            if event.key == pg.K_SPACE:
                select_answer()

    screen.fill(black)
    font = pg.font.Font(None, 22)
    text = font.render(quest.level1['question'], True, white)
    textpos = text.get_rect(centerx=screen.get_width() / 2, y=10)
    screen.blit(text, textpos)

    for i in range(grid_size):
        for j in range(grid_size):
            grid_box = pg.Rect(i*width/grid_size, j*height/grid_size, width/grid_size, height/grid_size)
            pg.draw.rect(screen, white, grid_box, 1)
            font = pg.font.Font(None, 28)
            text = font.render(answers[i,j], True, white)
            screen.blit(text, grid_box.center)

    screen.blit(player, player_pos)
    pg.display.flip()

