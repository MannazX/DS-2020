# ex 4 lec 5
import math
import random
randomNumber = random.randint(0,9)

def guess():
    print("the random number is: ", randomNumber)
    numberGuess = eval(input("Guess a number between 0 - 9: "))
    print("your guess is: ", numberGuess)
    #return numberGuess
    if numberGuess == randomNumber:
        print("Well guessed!")
        exit()
    else:
        print("Guess again!")
        guess()

guess()

# written by Gergo Gyori
