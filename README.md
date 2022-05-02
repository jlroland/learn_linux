# Linux Chompers  

## About the Game  

While trying to learn Linux commands, I thought a game would be helpful in the learning process.  I wanted the game to be uncomplicated and easy to use.  I remembered that one of my favorite computer games as a kid was Number Munchers, so I decided to create my own game in the same spirit.  

## How to Play  

Once the display module has been launched from the command line, the player will see a screen pop up.  The screen will contain a 3x3 grid with a monster in the "Start" box in the middle of the screen.  The surrounding boxes will contain possible answers to a question that is displayed at the top of the screen.  The objective of the game is to select all correct answers by using the monster to chomp them.  

![Screenshot of game at start](/game_start.png)  

The monster can be moved around the screen using arrow keys.  To make the monster chomp an answer, use the spacebar. The first time an answer is selected, the "Start" box turns into the "End" box.  After the player has selected all correct answers, they need to move to the "End" box and tap the spacebar to find out if they win or lose.  If the player selects an incorrect answer, they automatically lose and they are given the option to quit (press q) or restart the game (press ENTER).  

## For Future Development  

Some of the ideas I've had regarding game development have been set aside for now.  With more time, I would do the following:  

* Re-factor the code to make it scale to a variety of screen sizes
* Add several more levels    
* Incorporate sprite animation to show the monster chomping on the answers  
