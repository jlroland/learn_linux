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

def select_answer(level):
    '''Function is called by event handler when player selects the answer on screen.  Player position on screen is translated into indices corresponding to the answer matrix.  Selected answer is evaluated for correctness and appropriate action is taken to track progress.'''
    
    # need to manipulate globally to trigger events
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
    chosen_answer = answers[i,j]

    # determine whether or not selected answer is correct
    # adjust variables to track game progress
    if chosen_answer in qs.levels[level]["correct_answers"]:
        answers[i,j] = ''  # remove correct answer from matrix
    elif chosen_answer in qs.levels[level]["wrong_answers"]:
        penalty_switch = 1   # flip switch to trigger game over
    elif chosen_answer == 'End':
        #check for overlap between "correct answers" & answers remaining in matrix
        check_answers = set(answers.flatten()).intersection(set(qs.levels[level]["correct_answers"]))
        if check_answers:
            penalty_switch = 1  # some correct answers were not "chomped"
        else:
            win_switch = 1  # all correct answers were "chomped"

def main(level):
    run = 1    # way to break current loop & move to next level
    dist = width/grid_size  # distance player moves between boxes
    while run:
        screen.fill(black)
        # draw grid and display answers
        for i in range(grid_size):
            for j in range(grid_size):
                grid_box = pg.Rect(i*width/grid_size, j*height/grid_size, width/grid_size, height/grid_size)
                pg.draw.rect(screen, white, grid_box, 1)
                font = pg.font.Font(None, 28)
                text = font.render(answers[j,i], True, white)
                screen.blit(text, ((grid_box.centerx - 20), grid_box.centery))
        
        # display question at top of screen
        length = int(len(qs.levels[level]['question']))
        mid = qs.levels[level]['question'].find(' ', int(length/2))
        line1 = qs.levels[level]['question'][0:mid]
        line2 = qs.levels[level]['question'][(mid+1): length]
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
        # arrows move player, spacebar "chomps" answer
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
                    select_answer(level)

        # display message if player loses
        if penalty_switch:
            end_font = pg.font.Font(None, 72)
            end_text = end_font.render("GAME OVER", True, red)
            end_textpos = end_text.get_rect(centerx=screen.get_width()/2, centery=screen.get_height()/2)
            # tell player which keys to press to restart or exit
            end_font2 = pg.font.Font(None, 40)
            end_text2 = end_font2.render("Press r to restart or q to quit", True, red)
            end_textpos2 = end_text2.get_rect(centerx=screen.get_width()/2, centery=screen.get_height()*0.75)
            screen.blit(end_text, end_textpos)
            screen.blit(end_text2, end_textpos2)

        # display message if player wins
        if win_switch:
            end_font = pg.font.Font(None, 72)
            end_text = end_font.render("YOU'RE A WINNER!", True, green)
            end_textpos = end_text.get_rect(centerx=screen.get_width()/2, centery=screen.get_height()/2)
            # tell player which keys to press to proceed or exit
            end_font2 = pg.font.Font(None, 40)
            end_text2 = end_font2.render("Press ENTER for next level or q to quit", True, green)
            end_textpos2 = end_text2.get_rect(centerx=screen.get_width()/2, centery=screen.get_height()*0.75)
            screen.blit(end_text, end_textpos)
            screen.blit(end_text2, end_textpos2)

        screen.blit(player, player_pos)
        pg.display.flip()

        # end game when player loses
        if penalty_switch:
            dist = 0  # stop player movement
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    raise SystemExit
                if event.type == pg.KEYDOWN:
                    # restart game if player presses 'r'
                    if event.key == pg.K_r: 
                        os.execv(sys.argv[0], sys.argv)
                    # quit game & close window if player presses 'q'
                    if event.key == pg.K_q:
                        pg.quit()
                        sys.exit()
        # end level when player wins
        if win_switch:
            dist = 0    # stop player movement
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    raise SystemExit
                if event.type == pg.KEYDOWN:
                    # go to next level if player presses ENTER
                    if event.key == pg.K_RETURN:
                        run = 0
                    if event.key == pg.K_q:
                        # quit game & close window if player presses 'q'
                        pg.quit()
                        sys.exit()
                        
# need to run the main function within a while loop
# this controls the flow of the game, rendering only one level at a time
if __name__ == '__main__':
    level_index = 0
    while level_index < len(qs.levels):
        score = 0
        penalty_switch = 0
        win_switch = 0

        # create randomized answer matrix to display on grid
        answers = qs.answer_shuffle(qs.levels[level_index], grid_size)

        main(level_index)
        level_index += 1
