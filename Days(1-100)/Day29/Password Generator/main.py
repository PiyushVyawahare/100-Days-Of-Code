from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(numbers) for _ in range(nr_numbers)]
    password_numbers = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password_string = "".join(password_list)

    password_entry.insert(0, password_string)
    pyperclip.copy(password_string)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered:\n"
                                                                          f"Email: {email_entry.get()}\n"
                                                                          f"Password: {password_entry.get()}\n"
                                                                          f"Is it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=30)

canvas = Canvas(width=200, height=200)
myPass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=myPass_image)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)

website_entry = Entry(width=50)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

email_entry = Entry(width=50)
email_entry.insert(0, "piyushvyawahare2001@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
