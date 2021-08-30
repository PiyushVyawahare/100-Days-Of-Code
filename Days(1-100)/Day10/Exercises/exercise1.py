def format(fname, lname):
	return fname.capitalize()+" "+lname.capitalize()

name = input("Enter your full name: ").split(" ")
print(format(name[0], name[1]))