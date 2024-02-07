#message = input('Enter the English message to translate into Pig Latin:')
message = 'My name is AL SWEIGART and I am 4,000 years old.'
message = message.replace('.','') #add fullstop back later
vowels = {'a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
consonants_and_clusters = {
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',
    'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z',
    'bl', 'br', 'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gh', 'gl', 'gr', 'kn', 'ph', 'pl', 'pr', 'qu', 'sc', 'sh', 'sk',
    'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th', 'tr', 'tw', 'wh', 'wr',
    'BL', 'BR', 'CH', 'CL', 'CR', 'DR', 'FL', 'FR', 'GH', 'GL', 'GR', 'PL', 'PR', 'QU', 'SC', 'SH', 'SK', 'SL', 'SM',
    'SN', 'SP', 'ST', 'SW', 'TH', 'TR', 'TW', 'WH', 'WR'
}
messageList = message.split()
for i, message in enumerate(messageList):
    if message.startswith(tuple(vowels)):
        if message.islower() or message.istitle():
            messageList[i] = f'{message}yay'
        else:
            messageList[i] = f'{message}YAY'
    elif message.startswith(tuple(consonantsAndClusters)):
        char = message[0]
        if message.islower() or message.istitle():
            newMessage = message[1:] + char.lower() + 'ay'
        else:
            newMessage = message[1:] + char + 'AY'
        messageList[i] = newMessage
        
messageList[0] = messageList[0].title()
pigLatin = ' '.join(messageList) + '.'

print(pigLatin)