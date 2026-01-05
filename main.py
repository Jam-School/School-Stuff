# Jordan AM
# 7
# Functions & Control Keyword Practice
# Time Spent: 20 minutes

def main():
    numd = int(input("What command do you want? 1 for start, 2 for set message and start ")) #Gets command from user

    while True: #Loop

        if numd == 1: #all the if stuff
            com1()

        elif numd == 2:
            com2()

        else:
            els3()
            break
        
def com1(): #Functions so I could meet the requierments
    print("Kaboom!")
    
def com2():
    mess = str(input("What message do you want? "))
    print(mess)
    
def els3():
    print("Give a command!")


main() #Thing that calls main
