from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
dictionary = {}
while True:
    print(logo)
    print("\n*** Welcome to Secret Blind Auction ***\n\n")
    key = input("What is your name?\n").capitalize()
    value = int(input("\nWhat's your bid? $"))
    dictionary[key] = value
    user_input = input('\nAre there any other bidders? Type "yes" or "no" : ').lower()
    clear()
    if user_input == "no":
        break

print(logo)
print("\n*** Here is the Result of Secret Blind Auction ***\n\n")
ans_value = 0
for key in dictionary:
	value = dictionary[key]
	if value > ans_value :
		ans_key = key
		ans_value = value

print(f"The winner is {ans_key} with a bid of ${ans_value}.")