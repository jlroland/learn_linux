#!/usr/bin/env python3

import sys
import os
import pygame as pg
import questions as qs    # contains questions, answers, shuffle function
pg.init()


# basic display setup
width, height = 600, 600
grid_size = 3
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
screen = pg.display.set_mode((width, height))
pg.display.set_caption('Linux Chompers')


# set up player image and positioning
image = pg.image.load("./monster.png")
pg.display.set_icon(image)
player = pg.transform.scale(image, (width/(grid_size *2), height/grid_size))
player_pos = [width/2, height/3]
dist = width/grid_size

# create randomized answer matrix to display on grid
answers = qs.answer_shuffle(qs.level1, grid_size)

# to track game progress
score = 0
penalty_switch = 0
win_switch = 0

def select_answer():
    '''Function is called by event handler when player selects the answer on screen.  Player position on screen is translated into indices corresponding to the answer matrix.  Selected answer is evaluated for correctness and appropriate action is taken to track progress.'''
    
    # need to manipulate globally to trigger events
    global score
    global penalty_switch
    global win_switch

    answers[1,1] = 'End'  # once player makes first selection, Start becomes End

    # translate screen position into indices for answer matrix
    i, j = 0, 0
    if player_pos[0] == 300:
        j = 1
    elif player_pos[0] == 500:
        j = 2
    if player_pos[1] == 200:
        i = 1
    elif player_pos[1] == 400:
        i = 2
    chosen_answer = answers[j,i]

    # determine whether or not selected answer is correct
    # adjust variables to track game progress
    if chosen_answer in qs.level1["correct_answers"]:
        score += 10
        answers[j,i] = ''
    elif chosen_answer in qs.level1["wrong_answers"]:
        answers[j,i] = ''
        penalty_switch = 1
    elif chosen_answer == 'End':
        check_answers = set(answers.flatten()).intersection(set(qs.level1["correct_answers"]))
        if check_answers:
            penalty_switch = 1
        else:
            win_switch = 1
def main():
    while 1:
        screen.fill(black)
        # draw grid and display answers
        for i in range(grid_size):
            for j in range(grid_size):
                grid_box = pg.Rect(i*width/grid_size, j*height/grid_size, width/grid_size, height/grid_size)
                pg.draw.rect(screen, white, grid_box, 1)
                font = pg.font.Font(None, 28)
                text = font.render(answers[i,j], True, white)
                screen.blit(text, ((grid_box.centerx - 20), grid_box.centery))
        
        # display question at top of screen
        length = int(len(qs.level1['question']))
        mid = qs.level1['question'].find(' ', int(length/2))
        line1 = qs.level1['question'][0:mid]
        line2 = qs.level1['question'][(mid+1): length]
        font = pg.font.Font(None, 28)
        text1 = font.render(line1, True, black)
        text2 = font.render(line2, True, black)
        textpos1 = text1.get_rect(centerx=screen.get_width() / 2, y=10)
        textpos2 = text2.get_rect(centerx=screen.get_width() / 2, y=2 * font.get_height())
        screen.fill(white, textpos1)
        screen.fill(white, textpos2)
        screen.blit(text1, textpos1)
        screen.blit(text2, textpos2)

        # define actions to take with different keys
        for event in pg.event.get():
            if event.type == pg.QUIT:
                raise SystemExit
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP and player_pos[1] > 0:
                    player_pos[1] -= dist
                if event.key == pg.K_DOWN and player_pos[1] < 400:
                    player_pos[1] += dist
                if event.key == pg.K_LEFT and player_pos[0] > 200:
                    player_pos[0] -= dist
                if event.key == pg.K_RIGHT and player_pos[0] < 500:
                    player_pos[0] += dist
                if event.key == pg.K_SPACE:
                    select_answer()
                #print(player_pos)

        # display message if player loses
        if penalty_switch:
            end_font = pg.font.Font(None, 72)
            end_text = end_font.render("GAME OVER", True, red)
            end_textpos = end_text.get_rect(centerx=screen.get_width()/2, centery=screen.get_height()/2)
            # tell player which keys to press to restart or exit
            end_font2 = pg.font.Font(None, 40)
            end_text2 = end_font2.render("Press ENTER to restart or q to quit", True, red)
            end_textpos2 = end_text2.get_rect(centerx=screen.get_width()/2, centery=screen.get_height()*0.75)
            screen.blit(end_text, end_textpos)
            screen.blit(end_text2, end_textpos2)

        # display message if player wins
        if win_switch:
            end_font = pg.font.Font(None, 72)
            end_text = end_font.render("YOU'RE A WINNER!", True, green)
            end_textpos = end_text.get_rect(centerx=screen.get_width()/2, centery=screen.get_height()/2)
            # tell player which keys to press to restart or exit
            end_font2 = pg.font.Font(None, 40)
            end_text2 = end_font2.render("Press ENTER to restart or q to quit", True, green)
            end_textpos2 = end_text2.get_rect(centerx=screen.get_width()/2, centery=screen.get_height()*0.75)
            screen.blit(end_text, end_textpos)
            screen.blit(end_text2, end_textpos2)

        screen.blit(player, player_pos)
        pg.display.flip()

        #end game when player wins or loses
        if penalty_switch or win_switch:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    raise SystemExit
                if event.type == pg.KEYDOWN:
                    # restart game if player presses ENTER
                    if event.key == pg.K_RETURN:
                        os.execv(sys.argv[0], sys.argv)
                    # quit game & close window if player presses 'q'
                    if event.key == pg.K_q:
                        pg.quit()
                        sys.exit()
                        

if __name__ == '__main__':
    main()
