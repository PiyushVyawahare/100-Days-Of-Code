#######Before Debugging#######

# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])


####After Debugging######

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0: #here it should be and as both condition must be true to execute next line.
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number) #here we have to just print a number instead of list.
# here I have changed 'if' to 'elif' for second and third 'if statement' as when it was 'if' it was checking all the three conditions except last.