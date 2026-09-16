import random

secret_number = random.randint(1, 100)

guess = int(input('This is a guessing game\nYou have ten tries to guess the number\nEnter a random number from 1 - 100: '))

guess_number = 10

while guess_number > 0 and guess != secret_number:
    guess_number -= 1
    if guess_number == 0:
        print(f'Out of guesses you lose, the secret number was {secret_number}')
        break
    if secret_number > guess:
        guess = int(input('Guess higher: '))
    elif secret_number < guess:
        guess = int(input('Guess lower: '))

if guess == secret_number:
    print(f'You win, the secret number was {secret_number}')
    print(f'You guessed the number with {guess_number} tries left')