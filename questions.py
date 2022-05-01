#!/usr/bin/env python3
import random
import numpy as np

level1 = {
    'question' : 'You see a file named devices.txt. Which commands are valid for this file type?',
    'correct_answers' : ['mv', 'cp', 'rm', 'chmod', 'touch'],
    'wrong_answers' : ['rmdir', 'cd', 'pwd']
}

#print(level1['question'].count(' '))
def answer_shuffle(level, dim):
    all_answers = np.array(level['correct_answers'] + level['wrong_answers'])
    random.shuffle(all_answers)
    all_answers = np.insert(all_answers, 4, 'Start')
    all_answers = np.reshape(all_answers, (dim,dim))
    return all_answers
