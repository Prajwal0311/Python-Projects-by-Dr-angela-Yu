from tkinter import *

FONT = ("Ink Free", 15, "bold")


# Funtion
def miles_kilometer():
    Miles = float(miles_input.get())
    Km =round( Miles * 1.609, 3)
    km_result.config(text=Km,)


# Window
window = Tk()
window.title("Miles to Kilometer Convertor.")
window.config(padx=15, pady=15)

# Label
is_equal = Label(font=FONT)
is_equal["text"] = "is equal to"
is_equal.grid(column=0, row=1)

# Label 2
miles = Label(font=FONT)
miles.grid(row=0, column=2)
miles["text"] = "Miles"

# Label 3
km = Label(font=FONT)
km.grid(row=1, column=2)
km["text"] = "Km"

# Label 4
km_result = Label(text=0, font=FONT)
km_result.grid(row=1, column=1)


# Entry
miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)


# miles_input.configure(bg='green')


# Button
def button_clicked():
    print("button Clicked!")


button = Button(text="Calculate", command=miles_kilometer)
button.grid(column=1, row=2)
# button.config(bg='green')

window.mainloop()
