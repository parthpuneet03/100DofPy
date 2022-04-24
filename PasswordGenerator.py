#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nl= int(input("How many letters would you like in your password?\n")) 
ns = int(input(f"How many symbols would you like?\n"))
nn= int(input(f"How many numbers would you like?\n"))
password=[]
for i in range(0, nl):
  randChar=random.choice(letters)
  password.append(randChar)
for j in range(0,ns):
  randSym=random.choice(symbols)
  password.append(randSym)
for k in range(0, nn):
  randNum=random.choice(numbers)
  password.append(randNum)
random.shuffle(password)
str=""
for j in password:
  str+=j
print(str)
