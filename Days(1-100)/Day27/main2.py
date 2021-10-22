# Using Grid to manage layout

from tkinter import *


def button_clicked():
    input2 = text.get()
    label["text"] = input2
    # or
    # my_label.config(text=input2)


window = Tk()
window.title("Playing with Grid")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

label = Label(text="A Label")
label.grid(column=0, row=0)
label.config(padx=10, pady=10)

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Click me again", command=button_clicked)
new_button.grid(column=2, row=0)

text = Entry(width=10)
text.grid(column=3, row=2)

window.mainloop()
