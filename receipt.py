# Jordan AM
# 7
# F-string Receipt maker
# Time Spent: 2 hours
import time
money = 100

print("welcome to the super market, you have $100 to get everything you need!")
time.sleep(3)
print("Shopping time!")
apple = int(input("How many apples do you want? (theres only 5 and cost $3 each)"))
time.sleep(1)

if apple > 5:
    print("There are only 5 apples so you took them all")
    apple = 5
    time.sleep(2)

bread = int(input("How many loafs of bread do you want? (theres only 2 and cost $5 each)"))
time.sleep(1)

if bread > 2:
    print("There are only 2 loafs so you took them all")
    bread = 2
    time.sleep(2)
    
dogfood = int(input("How dog food do you want? (theres only 50 bags and cost $10 each)"))
time.sleep(1)

if dogfood > 50:
    print("There are only 50 bags so you took them all")
    dogfood = 50
    time.sleep(2)

water = int(input("How many bottles of water do you want? (theres only 5 and cost $1 each)"))
time.sleep(1)

if water > 5:
    print("There are only 5 bottles so you took them all")
    bottles = 5
    time.sleep(2)
    
doll = int(input("There is a cool looking action figure, do you want it? (It cost $PRICE HAS HAD AN ERROR: FLOAT OVERFLOW)"))
time.sleep(1)

if doll == 1:
    print("Something tells you this was a bad idea.")
    time.sleep(3)
    
grand = int(input("There is a grandma who is walking slow infront of you. 1 to walk pass her. 2 to beat her up."))
time.sleep(1)

if grand == 1:
    print("You walked pass her.")
    time.sleep(2)
elif grand == 2:
    print("You beat up the grandma and got $120 from her!")
    money = money + 120
    time.sleep(2)
    print("You also got the horrible person achievement!")
    time.sleep(2)
else:
    print("You didn't pick anything so you beat up the grandma and got $120 from her!")
    money = money + 120
    time.sleep(2)
    print("You also got the horrible person achievement!")
    time.sleep(2)
    
apmon = apple * 3
brmon = bread * 5
dogmon = dogfood * 10
sum = apmon + brmon + dogmon
    
print("Your total is:")
print(f"{apple} apples: ${apmon}")
print(f"{bread} loafs: ${brmon}")
print(f"{dogfood} bags: ${dogmon}")
print(f"{water} apples: ${water}")
time.sleep(3)
if sum > money:
    print("You are too broke!")
else:
    Print("You left with everything!")


