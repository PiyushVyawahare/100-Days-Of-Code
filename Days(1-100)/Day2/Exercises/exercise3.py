age = input("Enter your age ")
years = 90-int(age)
months = years * 12
weeks = years * 52
days = 365 * years
s = f'You have {days} days, {weeks} weeks, {months} months left.'
print(s)