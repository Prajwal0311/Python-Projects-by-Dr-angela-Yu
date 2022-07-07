import random
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
print(logo)

guess=random.randint(1,100)

choice=input("Choose your Difficulty.Easy or Hard--->")
if choice=="Easy" or choice=="easy":
  chance=10
  print("You have 10 Attempts to Guess the number")

  for i in range(1,11):
    number=int(input("Guess the number between 1 and 100.--->"))
    if number==guess:
      print("You won the game.!!")
      exit
    else:
      print(f"You have {chance-i} Attempts left.")      
      if number < guess: 
        
        print("Your Guess is lesser than the number.")
      else:
        print("Your Guess is greater than the number.")
      if (chance-i)==0:
        print("You ran out of Guesses! You lose.")
        print(f"The number was {guess}")

elif choice=="Hard" or choice=="hard" :
  chance=5
  print("You have 5 Attempts to Guess the number")

  for i in range(1,6):
    number=int(input("Guess the number between 1 and 100.--->"))
    if number==guess:
      print("You won the game.!!")
      exit
    else:
      print(f"You have {chance-i} Attempts left.")      
      if number < guess: 
        
        print("Your Guess is lesser than the number.")
      else:
        print("Your Guess is greater than the number.")
      if (chance-i)==0:
        print("You ran out of Guesses! You lose.")
        print(f"The number was {guess}")
  
