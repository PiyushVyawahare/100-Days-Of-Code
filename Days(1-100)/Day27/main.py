# Playing with Tkinter widgets

from tkinter import *


# Window
window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I'm a label", font=("Arial", 24, "bold"))
my_label.pack()


# Button
def button_clicked():
    input2 = input1.get()
    my_label["text"] = input2
    # or
    # my_label.config(text=input2)


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input1 = Entry(width=25)
input1.insert(END, "Enter some text.")
input1.pack()

# Text
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Enter lines of text.")
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=31, width=5, command=spinbox_used)
spinbox.pack()


# Scale
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# checkbutton
def checkbutton_used():
    print(check_state.get())


check_state = IntVar()
check_button = Checkbutton(text="Is on?", variable=check_state, command=checkbutton_used)
check_button.pack()


# Radio Buttons
def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# ListBox
def listbox_used():
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for items in fruits:
    listbox.insert(fruits.index(items), items)
listbox.bind("<<ListBoxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
