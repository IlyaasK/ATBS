# Write your code here :-)
while True:
    name = input('what is your name?\n')
    if name != 'Joe':
        continue
    password = input('what is the password?\n')
    if password == 'swordfish':
        break
print ('access granted.')

