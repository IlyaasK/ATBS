import sys
def collatz(number):
    while True:
        if number % 2 == 0:
            return number // 2

        elif number % 2 == 1:
            return 3 * number + 1

secondNumber = collatz(int(input('Enter number:')))

while secondNumber != 1:
    print(secondNumber)
    secondNumber = collatz(secondNumber)
    if secondNumber == 1:
        print(secondNumber)
        break
