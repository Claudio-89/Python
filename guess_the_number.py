#!/usr/bin/env python3


# with if/else

import random

print("Try to guess a number between 1 and 100")
random_num = random.randint(1, 100)

def game():
  guess = int(input("Guess: "))

  if guess == random_num:
      print("You win!")
  else:
      print("Guess...{}".format("higher" if guess < random_num else "lower" ))
      game()

game()

# with while loop

import random

print("Let's Play!, guess a number between 1 and 100")
random_num = random.randint(1, 100)

def game():
  while True:
    guess = int(input("Guess: "))

    if guess == random_num:
      print("You guessed right!")
      break
 
    else:
      print("Guess....{}".format("Higher!" if guess < random_num else "Lower!"))
      continue
game()
