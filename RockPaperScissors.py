rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random as r
rand=r.randint(0,2)
rps=[rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(f"You Chose:{rps[user_choice]}")
print(f"Computer Chose:{rps[rand]}")
if(user_choice == rand):
  print("Its a Draw!")
elif(user_choice ==0 and rand==1):
  print("You Lose!")
elif(user_choice ==0 and rand==2):
  print("You Win!")
elif(user_choice ==1 and rand==0):
  print("You Win!")
elif(user_choice ==1 and rand==2):
  print("You Lose!")
elif(user_choice ==2 and rand ==0):
  print("You Lose!")
else:
  print("You Win!")
