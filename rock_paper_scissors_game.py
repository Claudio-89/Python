#!/usr/bin/env python3

import random

moves = ['rock', 'paper', 'scissors']
player_wins = ['paperrock', 'scissorspaper', 'rockscissors']

print("Rock Paper Scissors Game, try to beat the computer!")
print("")
print("Type 'rock', 'paper' or 'scissors' and if you want to quit the game, type 'quit'")
print("")

while True:
  player_move = input("Your move: ")
  if player_move == 'quit':
    break
  elif player_move not in moves:
    print("I think you made a typo...try again")
    continue

  computer_move = random.choice(moves)

  print("You: ", player_move)
  print("Computer: ", computer_move)

  if player_move == computer_move:
    print("Tie")
  elif player_move + computer_move in player_wins:
    print("You win!")
  else:
    print("You lose!")
