#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total=""

 # <><><><><><><><><><><><><><><><><><><><><><><><><>   APPROACH 01  <><><><><><><><><><><><><><><><><><><><><><><><><>
  
# for l_select in range(0,nr_letters):
#   index= random.randint(0, len(letters)-1)
#   l_select= letters[index]
#   total+=l_select
# # print(total)

# for s_select in range(0,nr_symbols):
#   index=random.randint(0,len(symbols)-1)
#   s_select=symbols[index]
#   total+=s_select
# # print(total)

# for n_select in range(0,nr_numbers):
#   index=random.randint(0,len(numbers)-1)
#   n_select=numbers[index]
#   total+=n_select
# print(f"Your password is  {total}")
    
 # <><><><><><><><><><><><><><><><><><><><><><><><><>   APPROACH 02  <><><><><><><><><><><><><><><><><><><><><><><><><>

for s_select in range(0,nr_letters):
  s_select=random.choice(letters)
  total+=s_select

for n_select in range(0,nr_numbers):
  n_select=random.choice(numbers)
  total+=n_select

for l_select in range(0,nr_symbols):
  l_select=random.choice(symbols)
  total+=l_select

print(f"Your password is   {total}")



  
