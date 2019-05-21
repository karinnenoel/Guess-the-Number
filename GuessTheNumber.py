#Guess the Number Game

import random

guesses = 6
number = random.randint(1, 100)
win = False

while guesses > 0;
      guess = int(input("Guess: "))

      guesses -= 1
      
       if guess > number:
          print("Your guess was too high, you have", guesses, "remaining")
      elif guess < number:
         print ("Your guess was too low, you have", guesses, "remaining")
     else:
         print ("YAY! You Won!! Your guess was correct.")
         win = True
         guesses = 0


if win == False:
    print("sorry, you didn't guess the number. :( The number was", number)
