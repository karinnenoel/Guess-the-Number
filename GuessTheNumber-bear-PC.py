#Guess the Number Game
import random

guessesTaken = 0

print('Hello! Welcome to The Guess the Number Game. What is your name?')
myName = input()

print(myName +', please choose the maximum number in your range.')
maxNumber = int(input())

print(myName +', please choose the minimum number in your range.') 
minNumber = int(input())

number = random.randint(minNumber, maxNumber)
print ('Well, ' + myName + ', I am thinking of a number between' + minNumber + 'and' + maxNumber +'.')

while guessesTaken < 6:
      print('Take a guess.')
      guess = input()
      guess = int(guess)

      guessesTaken = guessesTaken + 1

      if guessesTaken == 6:
           break

      if guess < number:
            print('Your guess is too low.')

      if guess > number:
            print('Your guess is too high.')

      if guess == number:
             break

if guess == number:
      guessesTaken =str(guessesTaken)
      print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses! ')

if guess != number:
      number = str(number)
      print('Awwe you got it wrong. The number I was thinking of was ' + number + ' Try agian next time! ')
      
      
      

