# import random

# secret number
secret = 5

# ask the user to guess
guess = input('Guess a number 1-10: ')

# convert guess to integer for comparisons
guess = int(guess)

if guess < 1 or guess > 10:
    message = f'Invalid guess: {guess}.'

# if they guess correctly
elif guess == secret:
    message = f'You guessed the secret!'

# if they guess too high
elif guess > secret:
    message = f'Your guess of {guess} was too high!!'

# if they guess too low
elif guess < secret:
    message = f'Your guess of {guess} was too low!!'

# display result with after a new line
print('\n' + message)
print(f'The secret was: {secret}')

