from art import logo
from replit import clear
from random import randint
def chooseTheNumber():
	clear()
	print(logo)
	print("***Welcome to choose The Number game.***")
	print("I'm thinking of a number between 1 and 100.")
	number = randint(1,100)
	if input("Choose a difficulty level. Type 'Easy' or 'Hard' : ").lower() == "easy":
		numberOfAttempts = 10
	else:
		numberOfAttempts = 5
	print(f"You have {numberOfAttempts} attempts to guess the number.")
	while numberOfAttempts:
		numberOfAttempts -= 1
		guess = int(input("Make a Guess: "))
		if numberOfAttempts == 0:
			print(f"You have left with {numberOfAttempts} attempts to guess the number.")
			print(f"You Lose and the number was {number}.")
			break
		elif guess == number:
			print("You guessed it correct.")
			break
		elif guess < number:
			print("Too low")
			print(f"You have left with {numberOfAttempts} attempts to guess the number.")
			print("Guess Again")
		elif guess > number:
			print("Too High")
			print(f"You have left with {numberOfAttempts} attempts to guess the number.")
			print("Guess Again")
chooseTheNumber()
flag = input("Do you want to play again?. Type 'y' or 'n' : ").lower()
if flag == "y":
	chooseTheNumber()
else:
	print("Byeeee. To play again next time, re-run the program.")