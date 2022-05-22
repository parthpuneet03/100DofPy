from art import logo 
import random
num=random.randint(1,100)

def checkNum(n):
    if n>num:
        return 0
    elif n<num:
        return 1
    else:
        return 2

print(logo)
print("Welcome to the number guessing game! \nI am thinking of a Number between 1 and hundred")
print(num, "is the number")
dif=input("Choose difficulty. Type 'easy' or 'hard' ")
if dif=='easy':
    attempts=10
else:
    attempts=5
while(attempts>0):
    print(f"You have {attempts} attempts to guess")
    n=int(input("Make a guess: "))
    attempts-=1
    ans=checkNum(n)
    if ans==0:
        print("Too High")
    elif ans==1:
        print("Too Low")
    elif ans==2:
        print(f"Your guess is right, number is: {num}")
        break
