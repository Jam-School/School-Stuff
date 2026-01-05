# Jordan AM
# 7
# if-elif-else HW
# Time Spent: 2 minutes

import random #importing random for random number

numb = random.randint(1,100) #random number

guess = int(input("Guess the number ")) #Input to get the players guess

if guess == numb: #checks if guess is right
    print("You got it right!")
    
elif guess > numb: #checks if guess is too high
    print(f"Too high! the number was {numb}")
    
else: #checks if guess is too low
    print(f"Too low! the number was {numb}")
