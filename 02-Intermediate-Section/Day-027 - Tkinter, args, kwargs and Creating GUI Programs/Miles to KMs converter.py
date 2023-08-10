from tkinter import *

#Window

window = Tk()
window.title("Miles to KMs converter")
# window.minsize(width=200, height=150)
window.config(padx=20, pady=20)

#Label

label_1 = Label(text="is equal to")
label_1.grid(column=0, row=1)

label_2 = Label(text="Miles")
label_2.grid(column=2, row=0)

label_3 = Label(text="KMs")
label_3.grid(column=2, row=1)

label_output = Label(text="0")
label_output.grid(column=1, row=1)

#Button

def converter():
    miles = float(input.get())
    kms = round(1.609 * miles, 2)
    label_output.config(text=f"{kms}")

# def printer():
#     text.delete("0.0", END)
#     text.insert(END, converter())

button = Button(text="Calculate", command=converter)
button.grid(column=1, row=2)

#Input

input = Entry(width=10)
input.insert(END, string=0)
input.grid(column=1, row=0)

#Text

# text = Text(height=1, width=8)
# text.insert(END, 0)
# text.grid(column=1, row=1)

window.mainloop()
