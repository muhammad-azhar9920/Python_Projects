import random

# Generate random number
randomNum = random.randint(1,100)
attempCount = 0
while True:
    attempCount += 1
    userNum = int(input("Guess the Number from 1 to 100: "))
    if(randomNum == userNum):
        print("Congratulations ! You have successfully guessed the number ", userNum)
        break
    elif(userNum > randomNum):
        print("Your number is too big !! try small number")
    elif(userNum < randomNum):
        print("Your number is too small !! try big number")
    else:
        print("Please write valid number 1 to 100")
print(f"You attempted this game {attempCount} times")
    