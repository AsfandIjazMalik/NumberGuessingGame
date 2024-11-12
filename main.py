import random  # Used to generate random numbers

def NumberGuessingGame():
    random_number = random.randint(1, 100)  # Generate random number within the function
    chances = 3  # Set the number of chances
    print('********************************\nWELCOME TO NUMBER GUESSING GAME\n********************************\n')

    while chances > 0:
        try:
            player_guessing_number = int(input(f'You have {chances} chances left. Enter a number between 1 and 100: '))

            # Check if the player's guess is correct
            if player_guessing_number == random_number:
                print('Congratulations!!!\nYOU WON')
                break
            elif player_guessing_number > random_number:
                if chances > 1:  # Only print the message if there are more than 1 chance left
                    print('Please enter a lower number')
            elif player_guessing_number < random_number:
                if chances > 1:  # Only print the message if there are more than 1 chance left
                    print('Please enter a greater number')
            
            chances -= 1  # Deduct a chance after each guess

            # Check if the player has run out of chances
            if chances == 0:
                print(f'Sorry, you\'ve run out of chances. The correct number was {random_number}.')
                break

        except ValueError:
            print('Please enter a valid positive number.')

# Game loop to replay or exit
while True:
    NumberGuessingGame()

    player_again = input('Enter Yes to Play Again or No to Exit: ').lower()
    if player_again == 'no':
        print('YOU ARE EXITING THE GAME. SEE YOU NEXT TIME!\nTHANK YOU!!!!')
        break