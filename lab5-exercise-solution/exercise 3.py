import random
number=random.randint(1,10)
rerun = 1
while rerun == 1:
    guess= int(input("please enter a number"))
    if number == guess:
        print ("you guessed correctly")
        rerun = 0
    elif number > guess:
        print ("increase your guess")
        rerun = 1
    elif guess > number:
        print ("decrease your guess")
        rerun = 1