# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

flag=0
if (year%4==0):
  if(year%100==0):
    if(year%400==0):
      flag=1
    else:
      flag=0
  else:
    flag=1
if(flag==1):
  print("it is a leap year")
else:
  print("not a leap year")
  
