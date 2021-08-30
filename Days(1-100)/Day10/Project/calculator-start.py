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

while True:
	clear()
	print(logo)
	print("***Welcome to the Calculator***")
	
	first_num = int(input("Enter first Number : "))
	for operation in operations:
		print(f"{operation}")
	operation_symbol = input("Select an opeartor from above line and type it down: ")
	
	if operation_symbol not in operations:
		print("Enter valid operator.")
		break
	
	operator = operations[operation_symbol]
	second_num = int(input("Enter second number : "))

	answer = operator(first_num, second_num)

	print(f"\n{first_num} {operation_symbol} {second_num} = {answer}")

	user_input = input("Type 'yes' to continue else type 'no'.").lower()
	if user_input == "no":
		break
	clear()