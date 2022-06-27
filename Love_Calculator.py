# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_low= name1.lower()
name2_low= name2.lower()

t=0
name1_t=name1_low.count('t')
name2_t=name2_low.count('t')
t=name1_t+name2_t

r=0
name1_r=name1_low.count('r')
name2_r=name2_low.count('r')
r=name1_r+name2_r

u=0
name1_u=name1_low.count('u')
name2_u=name2_low.count('u')
u=name1_u+name2_u

e1=0
name1_e1=name1_low.count('e')
name2_e1=name2_low.count('e')
e1=name1_e1+name2_e1

l=0
name1_l=name1_low.count('l')
name2_l=name2_low.count('l')
l=name1_l+name2_l

o=0
name1_o=name1_low.count('o')
name2_o=name2_low.count('o')
o=name1_o+name2_o

v=0
name1_v=name1_low.count('v')
name2_v=name2_low.count('v')
v=name1_v+name2_v

e2=0
name1_e2=name1_low.count('e')
name2_e2=name2_low.count('e')
e2=name1_e2+name2_e2


str1=str(t+r+u+e1)
str2=str(l+o+v+e2)

total_score= str1+str2
total_score=int(total_score)

if total_score <10  or total_score>90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")

elif total_score >=40 and total_score<=50:
    print(f"Your score is {total_score},you are alright together.")

else:
    print(f"Your score is {total_score}")


