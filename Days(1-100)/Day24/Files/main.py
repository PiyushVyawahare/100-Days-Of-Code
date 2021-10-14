with open("new_file.txt", mode="w") as file:
    file.write("Hello everyone.")

with open("my_file.txt", mode="a") as file:
    file.write("\nHello everyone")

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
