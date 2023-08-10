import tkinter
# from tkinter import *

#Window

window = tkinter.Tk()
window.title("Learning GUI")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label

MyLabel = tkinter.Label(text="This is a test label.", font=("Arial", 24, "bold"))
MyLabel.grid(column=0, row=0)

MyLabel['text'] = "New test label."
MyLabel.config(text="New test label 2.0.")

#Button

def button_clicked():
    # print("Clickkkkking!")
    MyLabel.config(text=f"Button got clicked!")

button = tkinter.Button(text="1 Click me!", command=button_clicked)
button.grid(column=1, row=1)

#Entry

def read_write_input():
    MyLabel.config(text=input.get())

button_2 = tkinter.Button(text="2 Click me!", command=read_write_input)
button_2.grid(column=2, row=0)

input = tkinter.Entry(width=30)
input.grid(column=3, row=2)

window.mainloop()
