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
ans_key = key
for key in dictionary:
    if dictionary[key]>dictionary[ans_key]:
        ans_key = key

print(f"The winner is {ans_key} with a bid of ${dictionary[ans_key]}.")