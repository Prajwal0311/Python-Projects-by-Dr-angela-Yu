from art import logo,vs
from game_data import data
from replit import clear
import random

def format_data(account):
  """format the account data into printable format """
  account_name=account["name"]
  account_desc=account["description"]
  account_country=account["country"]

  return f"{account_name} , a {account_desc} , from {account_country} "
  

def check_answer(guess, a_followers , b_followers):
  """Takes the user's guess and returns  if they got it right ."""
  if a_followers> b_followers:
    return guess=="a"       #guess=="a" ->  if a is the guess , then answer is true
  else:
    return guess=="b"       #guess=="b" ->  if b is the guess , then answer is true


print(logo)
score = 0
game_shuld_contin=True
account_b=random.choice(data)


# make the game repeatable 

while  game_shuld_contin:
  """To generate random choices from given set of data."""
  # Making account at positon B the new account at position A for the next loop
  account_a=account_b
  account_b= random.choice(data)
 
  if account_a==account_b:
    account_b=random.choice(data)
  
  print(f"Compare A : {format_data(account_a)}")
  print(vs)
  print(f"Against B : {format_data(account_b)}")
  
  guess= input("Who has more followers ? Type A or B :").lower()
  
  a_followers=account_a["follower_count"]
  b_followers=account_b["follower_count"]
  
  is_correct=check_answer(guess,a_followers,b_followers)
  clear()
  print(logo)
  
  if is_correct:
    score+=1
    print("Your score is ", score)
    print("You're right!")
  else:
    game_shuld_contin=False
    print("Sorry, you're wrong!")
    print("Your final score is ", score)
    
