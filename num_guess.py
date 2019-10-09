# Author: Mahtab Zilaie
# Date: 10/9/19
# Description: prompts the user for an integer, user will try to guess
# higher or lower than the target number, program will output that it is
# too high or low. Then program will print how many guesses it took

num_guesses = 0
number = int(input('Enter the number for the player to guess.'))
print(number)
guess = int()

while guess != number:
    guess = input('Enter your guess.')
    print(guess)
    guess = int(guess)
    num_guesses = num_guesses +1

    if guess < number:
        print('Too low - try again:')
    if guess > number:
        print('Too high - try again:')
    if guess == number:
        print('You guessed it in', num_guesses,'tries.')