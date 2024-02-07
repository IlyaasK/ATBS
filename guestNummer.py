# Write your code here :-)
name = ''
while not name:
    input ('Enter your name.\n')
    guestNummer = int(input('how many guests will you have?\n'))
    if guestNummer:
        print('ensure to have enough space.')
        break
    else:
        print ("done.")
