# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = name1 + name2
name = name.lower()
x = name.count("t") + name.count("r") + name.count("u") + name.count("e")
y = name.count("l") + name.count("o") + name.count("v") + name.count("e")
love_percentage = x*10+y

if love_percentage<=10 or love_percentage > 90:
    print(f"Your score is {love_percentage}, you go together like coke and mentos.")
elif love_percentage > 40 and love_percentage <= 50:
    print(f"Your score is {love_percentage}, you are alright together.")
else:
    print(f"Your score is {love_percentage}")
    