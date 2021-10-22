from tkinter import *


def button_clicked():
    mile = float(input1.get())
    kilometer = (mile * 1.609)
    kilometers["text"] = kilometer


window = Tk()
window.title("Mile to Km converter")
window.config(padx=20, pady=20)

input1 = Entry(width=10)
input1.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

kilometers = Label(text="0")
kilometers.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

calculate = Button(text="Calculate", command=button_clicked)
calculate.grid(column=1, row=2)


window.mainloop()
