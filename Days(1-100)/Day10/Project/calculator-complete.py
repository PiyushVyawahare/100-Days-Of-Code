from art import logo
from replit import clear

def add(n1, n2):
	return n1+n2

def subtract(n1, n2):
	return n1-n2

def multiply(n1, n2):
	return n1*n2

def divide(n1, n2):
	return n1/n2

operations = {
	"+" : add,
	"-" : subtract,
	"*" : multiply,
	"/" : divide,
}

def calculator():
	clear()
	print(logo)
	print("***Welcome to the Calculator***")

	first_num = float(input("\nEnter first Number : "))

	while True:
		print("\n")
		for operation in operations:
			print(f"{operation}")
		operation_symbol = input("\nSelect an opeartor : ")
		
		if operation_symbol not in operations:
			print("\nEnter valid operator.")
			break
		
		operator = operations[operation_symbol]
		second_num = float(input("\nEnter next number : "))

		answer = operator(first_num, second_num)

		print(f"\n{first_num} {operation_symbol} {second_num} = {answer}")
		
		user_input = input(f"\nType 'yes' to continue with '{answer}' else type 'no' to start new calculation. : ").lower()
		if user_input == "no":
			clear()
			# if input("Type 'yes' to stop calculator.: ") == "yes":
			# 	clear()
			# 	print("Byee, to start again re-run program.")
			# 	break
			calculator()
		else:
			first_num = answer

calculator()