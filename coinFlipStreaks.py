import random
htList = []
hList = [0,0,0,0,0,0]
lList = [1,1,1,1,1,1]

print('started')
for i in range(100):
    htList.append(random.randint(0,1))

print('made list')
count = 0
while hList or lList in htList:
    if hList in htList:
        htList.remove(hList)
        print('found 1hList')
        count += 1
    elif lList in htList:
        htList.remove(lList)
        count += 1
        print('found 1 lList')

print(count)
print('done')
