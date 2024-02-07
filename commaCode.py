spam = ['apples', 'bananas', 'tofu', 'cats']

def returnString(someVariable):
    for i in someVariable:
        if i == someVariable[-1]:
            print(str(i),sep='. ',end='. ')
        elif i != someVariable[-2]:
            print(str(i),sep=', ',end=', ')
        else:
            print(str(i),sep=', ',end=', and ')


returnString(spam)
