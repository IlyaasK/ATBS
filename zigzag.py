# Write your code here :-)
import time, sys
space = ' '
design= '********'
try:
    while True:
        for i in range(0,5):
            print(i*space + design)
            time.sleep(0.1)

        for i in range(5,0,-1):
            print(i*space + design)
            time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()
