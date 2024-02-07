#have game logic seperate to reduce repeated code
import random, sys, time
print('ROCK, PAPER, SCISSORS')
choicesAndPlays = {'r':'ROCK','p':'PAPER','s':'SCISSORS'}
computerMove = random.choice('rps')
wins = 0
ties = 0
losses = 0
while True:
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')

    while True:
        userMove = input('Enter your move: (r)ock (p)aper (s)cissors or (q)uit\n')

        if userMove == 'q':
            if wins > losses:
                print('Overall, YOU WON!')
            print ('Overall, YOU LOST!')
            sys.exit()
 #   elif playermove == '': throw error is not rps
        else:
            break


    if userMove in choicesAndPlays:
        print(f"{choicesAndPlays[userMove]} versus...")

    time.sleep(1)
    if computerMove in choicesAndPlays:
        print(f"{choicesAndPlays[computerMove]}")

#use tuple to make code simpler - https://www.reddit.com/r/learnpython/comments/10m15gd/review_my_rock_paper_scissors_and_help_me_improve/
    time.sleep(1)
    if computerMove != userMove:
        if userMove == 'r' and computerMove == 'p' \
        or userMove == 'p' and computerMove == 's' \
        or userMove == 's' and computerMove == 'r':
            print('You lose!')
            losses += 1
        else:
            print('You win!')
            wins += 1
    elif userMove == computerMove:
        print('It is a tie!')
        ties += 1
#use functions to break down code. Can sit here and make it better butwill coninue wth ATBS> May come back after capter 5
