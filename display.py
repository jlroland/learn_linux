#!/usr/bin/env python3

import sys
import pygame as pg
import numpy as np
import questions as qs
pg.init()

width, height = 600, 600
grid_size = 3
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0

screen = pg.display.set_mode((width, height))

player = pg.image.load("./cute-pink-toy-pxhere.jpg")
player_rect = player.get_rect()
player_pos = [width/2, height/2]
dist = width/grid_size

answers = qs.answer_shuffle(qs.level1, grid_size)
score = 0
penalty = 0
penalty_switch = 0
win_switch = 0

def select_answer():
    global score
    global penalty
    global penalty_switch
    global win_switch

    i, j = 0, 0
    if player_pos[0] == 300:
        j = 1
    elif player_pos[0] == 500:
        j = 2
    if player_pos[1] == 300:
        i = 1
    elif player_pos[1] == 500:
        i = 2
    answers[1,1] = 'End'
    
    chosen_answer = answers[j,i]   # text loop went wonky?
    if chosen_answer in qs.level1["correct_answers"]:
        score += 10
        answers[j,i] = ''
    elif chosen_answer in qs.level1["wrong_answers"]:
        answers[j,i] = ''
        penalty += 1
    elif chosen_answer == 'End':
        check_answers = set(answers.flatten()).intersection(set(qs.level1["correct_answers"]))
        if check_answers:
            penalty_switch =1
        else:
            win_switch =1

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and player_pos[1] > 200:
                player_pos[1] -= dist
            if event.key == pg.K_DOWN and player_pos[1] < 500:
                player_pos[1] += dist
            if event.key == pg.K_LEFT and player_pos[0] > 200:
                player_pos[0] -= dist
            if event.key == pg.K_RIGHT and player_pos[0] < 500:
                player_pos[0] += dist
            if event.key == pg.K_SPACE:
                select_answer()

    screen.fill(black)
    font = pg.font.Font(None, 24)
    text = font.render(qs.level1['question'], True, white)
    textpos = text.get_rect(centerx=screen.get_width() / 2, y=10)
    screen.blit(text, textpos)

    for i in range(grid_size):
        for j in range(grid_size):
            grid_box = pg.Rect(i*width/grid_size, j*height/grid_size, width/grid_size, height/grid_size)
            pg.draw.rect(screen, white, grid_box, 1)
            font = pg.font.Font(None, 28)
            text = font.render(answers[i,j], True, white)
            screen.blit(text, grid_box.center)

    if penalty > 1 or penalty_switch == 1:
        end_font = pg.font.Font(None, 72)
        end_text = end_font.render("GAME OVER", True, red)
        end_textpos = end_text.get_rect(centerx=screen.get_width()/2, centery=screen.get_height()/2)
        screen.blit(end_text, end_textpos)
    
    if win_switch == 1:
        end_font = pg.font.Font(None, 72)
        end_text = end_font.render("YOU'RE A WINNER!", True, green)
        end_textpos = end_text.get_rect(centerx=screen.get_width()/2, centery=screen.get_height()/2)
        screen.blit(end_text, end_textpos)


    screen.blit(player, player_pos)
    pg.display.flip()

    if penalty > 1 or penalty_switch == 1 or win_switch:
        pg.event.clear(eventtype=pg.KEYDOWN)  

