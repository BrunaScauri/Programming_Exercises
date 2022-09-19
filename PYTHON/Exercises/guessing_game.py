#  GUESSING GAME
secret_number = 34
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    user_guess = int(input('Guess the secret number: '))
    guess_count += 1
    if user_guess == secret_number:
        print('You win!')
        break
else: #this else belongs to the while loop.
    print('Sorry, you failed!')
