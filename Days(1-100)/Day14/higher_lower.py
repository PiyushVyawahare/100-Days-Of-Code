import art
from game_data import data
from random import randint
from replit import clear
A = randint(0, len(data))
# B = randint(0, len(data))
lst = []
current_score = 0
while True:
	clear()
	print(art.logo)
	print("\n")
	if current_score != 0:
		print(f"You're right! Current score: {current_score}.")
	B = randint(0, len(data))
	while A == B:
		B = randint(0, len(data))
	A_name = data[A]["name"]
	A_follower_count = data[A]["follower_count"]
	A_description = data[A]["description"]
	A_country = data[A]["country"]
	print(f"Compare A: {A_name}, a {A_description}, from {A_country}.")

	print(art.vs)

	B_name = data[B]["name"]
	B_follower_count = data[B]["follower_count"]
	B_description = data[B]["description"]
	B_country = data[B]["country"]
	print(f"\nAgainst B: {B_name}, a {B_description}, from {B_country}.")

	if A_follower_count > B_follower_count:
		ans = "A"
	else:
		ans = "B"
	user_choice = input("\nWho has more followers? Type 'A' or 'B': ").upper()
	if user_choice == ans:
		current_score += 1
		if user_choice == "B":
			A = B
	else:
		clear()
		print(f"\nSorry, that's wrong. Final score: {current_score}.")
		break

