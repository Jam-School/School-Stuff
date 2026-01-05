# Jordan AM
# 7
# Logical Operators Practice
# Time Spent: 10 minutes


day = str(input("Is to day wensday? Y for yes and N for no ")) #getting player input 7-11

hung = str(input("Are you hungry? Y for yes and N for no "))

com = str(input("Are you on a computer? Y for yes and N for no "))

if day == "Y": #converting to make logic easy 13-26
    dayB = True
else:
    dayB = False
    
if hung == "Y":
    hungB = True
else:
    hungB = False
    
if com == "Y":
    comB = True
else:
    comB = False
 
if not dayB: #checking day
    print("Aw man")
else:
    print("It's wensday my dudes")
    
if dayB == True and hungB == True: #checking day and hunger
    print("To bad it's not taco tuesday")
    
if hungB == True and comB == True or dayB == True: #yelling at the player
    print("It's wensday, but you still gotta eat!")
    
elif hungB == True and comB == True or dayB == False:
    print("It's taco tuesday, go eat a taco!")

elif hungB == True and comB == False or dayB == True:
    print("You got nothing better to do, go eat!")
    
else:
    print("It's taco time!!")