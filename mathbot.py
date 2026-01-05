# Jordan AM
# 7
# Input Practice HW
# Time Spent: 2 hours


import time
import random
import sys

good = 0

name = input("What is your name? ")
time.sleep(1)
print(f'Hello {name}, welcome to math bot 1.0!')
time.sleep(1)
print("Lets start!")

time.sleep(3)

while True:

    x = random.randint(1, 10)

    y = random.randint(1, 10)

    s = x + y
        
    i_str = input(f'What is {x} + {y}? ')
    
    if ("cor" in i_str):
        if (good >= 5):
            print("5")
        else:
            print(good)
            
    if ("quit" in i_str):
        if (good >= 10):
            print("lol get trolled nerd")
            time.sleep(3)
            sys.exit()
        else:
            print("Not a valid command or input!!!")        
    
        
    else:
    
        try:
            i = int(i_str)
        except ValueError:
            print("Not a valid command or input!!!")

        if (i == s):
            
            if(good >= 10):
                print("Try and easier math, type quit to go to easy math!")
                time.sleep(3)
            else:
                if(good >= 5):
                    print("Close but wrong, try again!")
                    good = good + 1
                    time.sleep(3)
                else:
                    print("You did it!")
                    good = good + 1
                    time.sleep(3)
        
        
    
        else:
            print("Close but wrong, try again!")
            time.sleep(3)

