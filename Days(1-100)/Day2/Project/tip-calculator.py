print("***Welcome to the Tip Calculator***")

bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12 or 15?"))

bill+=(bill*tip/100)

people = float(input("How many people to split the bill?"))
ans = round(bill/people, 2)

print(f"Each person should pay: ${ans}.")
