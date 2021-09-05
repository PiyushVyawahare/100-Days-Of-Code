
#****Debugged codes****


# # Describe Problem
# def my_function():
#   for i in range(1, 21): #here range should be from 1 to 21 so that it will encounter 20 
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"] #list start indexing from 0 by default
# dice_num = randint(0, 5) # here we have to choose random int from 0 to 5, it will give error for 6 as there is no image at index 6
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year <= 1994:  #It will produce error at 1994, so we have to make conditional operator as '<=' instead of '<'
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you?")) #here you have to make input integer type as we are comparing it later.
# if age > 18:
# 	print(f"You can drive at age {age}.") #here you have not indented print in a if statement and you have to make it fstring to print age value
# #And onee more here an else part is missinga as it will never print anything for age <= 18.
# elif age > 10:
# 	print(f"You are small to drive at age {age}")
# else:
# 	print(f"You are too small to drive at age {age}")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: ")) #here it should be "=" instead of "==".
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item) #to get supposed output we have to indent this line in for loop.
  print(b_list)

mutate([1,2,3,5,8,13])