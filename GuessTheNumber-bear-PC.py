#Guess the Number Game
import random

guessesTaken = 0

print('Hello! Welcome to The Guess the Number Game. What is your name?')
myName = input()

number = random.randint(1, 100)
print ('Well, ' + myName + ', I am thinking of a number between 1 and 100.')

while guessesTaken < 6:
      print('Take a guess.')
      guess = input()
      guess = int(guess)

      gussesTaken = gussesTaken + 1
      
      

