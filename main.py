from tkinter import *


def calculate():
    miles_calc = int(miles.get())
    km_calc = miles_calc * 1.609
    calculated_label.config(text=km_calc)


window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

# User input for miles
miles = Entry(width=10)
miles.grid(column=1, row=0)

# Miles label
miles_label = Label(text="Miles", font=("Courier", 12, "bold"))
miles_label.grid(column=2, row=0)

# Is equal to
equal_label = Label(text="is equal to ", font=("Courier", 12, "bold"))
equal_label.grid(column=0, row=1)

# Calculated label
calculated_label = Label(text=0, font=("Courier", 12, "bold"))
calculated_label.grid(column=1, row=1)

# Km label
km_label = Label(text="Km", font=("Courier", 12, "bold"))
km_label.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
