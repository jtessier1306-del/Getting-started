#.RandomNumberGenerator.py
import random 

number =random.randint(1, 100)
guess = int(input("Guesss a number between 1 and 100: "))

if guess == number:
    print("You guessed it right!")
else:
    print ("Sorry, the corrrect number was ", number)
