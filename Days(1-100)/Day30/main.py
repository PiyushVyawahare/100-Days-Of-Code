# try:
#     file = open("data.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("data.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("file closed.")

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise TypeError("Height can't be greater than 3 meters.")

bmi = weight / height ** 2

print(bmi)