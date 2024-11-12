# NumberGuessingGame
Python Programming 

## Number Guessing Game
### Overview
The Number Guessing Game is a simple and engaging Python-based game where players try to guess a randomly generated number within a limited number of attempts. The game provides feedback on whether the player's guess is too high or too low, and they have a total of 3 chances to guess the correct number. Once the game ends, the player is given the option to play again or exit.
### Features
•	Random Number Generation: The game generates a random number between 1 and 100 that the player must guess. <br>
•	Limited Chances: Players are given 3 chances to guess the correct number. <br>
•	Feedback on Guess: After each guess, players are informed whether their guess is too high or too low. <br>
•	Replay Option: After completing a game, the player can choose to play again or exit. <br>
### Game Instructions
1.	The game will generate a random number between 1 and 100. <br>
2.	You will have 3 chances to guess the number. <br>
3.	After each guess, the game will tell you if the number is too high or too low. <br>
4.	If you guess correctly, you will win the game. If you run out of chances, the correct number will be revealed. <br>
5.	After the game ends, you can choose to play again or exit. <br>
### Code Overview
The Number Guessing Game operates with the following flow: <br>
•	Random Number Generation: A number between 1 and 100 is generated using the random.randint method. <br>
•	Game Loop: The player has 3 chances to guess the number, with feedback after each guess on whether it is too high or too low. <br>
•	Replayability: After a round, the player is asked if they would like to play again. <br>
### Main Function: NumberGuessingGame()
This function handles: <br>
•	Generating the random number <br>
•	Managing player guesses and chances <br>
•	Providing feedback on guesses <br>
•	Ending the game or allowing for replay based on user input <br>

