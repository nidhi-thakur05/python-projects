import random

target=random.randint(1,100)

while True:
    userchoice = input("guess the target or Quit(Q): ")

    if (userchoice=="Q"):
        break
    userchoice=int(userchoice)

    if (userchoice==target):
        print("Hurray its a success: correct guess!!")
        break

    elif (userchoice < target):
        print("your number was too small..Take a bigger guess...")

    else:
        print("your number was too big..Take a smaller guess...")

    
        
print("----Game Over----")
