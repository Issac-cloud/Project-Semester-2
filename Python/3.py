import random
num = random.randint(10,20)
while True:
    guess = int(input("Please guess a number between 10 and 20: "))
    if guess == num:
        print("Congratulations!")
        break
    else:
        print("Please try again!")
