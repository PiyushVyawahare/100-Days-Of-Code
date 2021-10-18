with open("file1.txt") as file1:
    content = file1.read()
    lst1 = content.split("\n")

with open("file2.txt") as file2:
    content = file2.read()
    lst2 = content.split("\n")

result = [int(num) for num in lst1 if num in lst2]
# Write your code above 👆

print(result)
