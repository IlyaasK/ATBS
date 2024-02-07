# Write your code here :-)
import random
randomNumber = random.randint(1,20)
guessedNumber = 0
count = 0
print ('I am thinking of a number between 1 and 20.')
guessedNumber = int(input('Take a guess.\n'))
while guessedNumber != randomNumber:
    count += 1
    if randomNumber > guessedNumber:
        guessedNumber = int(input('Your guess is too low. Take another guess.\n'))
    elif randomNumber < guessedNumber:
        guessedNumber = int(input('Your guess is too high. Take another guess.\n'))
print (f"Good job. You guessed the number in {count} tries.")


