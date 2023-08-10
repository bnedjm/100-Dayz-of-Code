from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_l = [choice(letters) for _ in range(randint(8, 10))]
    password_s = [choice(symbols) for _ in range(randint(2, 4))]
    password_n = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_l + password_s + password_n

    shuffle(password_list)
    password = "".join(password_list)

    input_pw.delete(0, END)
    input_pw.insert(0, string=password)

    pyperclip.copy(password)


# ---------------------------- PASSWORD FINDER ------------------------------- #

def search_pw():
    website = input_website.get().title()

    if len(website) == 0:
        messagebox.showwarning(title="Oops", message="Please do not leave the website field empty!")

    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No Data File Found!")

        else:
            if website in data:
                email = data[website]['email']
                pw = data[website]['password']
                messagebox.showinfo(title=f"{website.title()} Details", message=f"Email : {email}\nPassword: {pw}")

            else:
                messagebox.showerror(title="Error", message="No Details for the website exist.")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = input_website.get().title()
    email = input_email.get()
    pw = input_pw.get()

    new_data = {
        website: {
            "email": email,
            "password": pw
        }
    }
    if len(website) == 0 or len(email) == 0 or len(pw) == 0:
        messagebox.showwarning(title="Oops", message="Please do not leave the fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=f"{website} Password!",
                                       message=f"You entered:\nEmail: {email}\nPassword: {pw}\nIs "
                                               f"it okay to save these details?")

        if is_ok:
            try:
                with open("data.json", "r") as file:
                    # read old data
                    data = json.load(file)

            except FileNotFoundError:
                with open("data.json", "w") as file:
                    # save new data to file
                    json.dump(new_data, file, indent=4)

            else:
                # update data
                data.update(new_data)

                with open("data.json", "w") as file:
                    # save data back to file
                    json.dump(data, file, indent=4)

            finally:
                input_website.delete(0, END)
                input_website.focus()
                # input_email.delete(0, END)
                input_pw.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Window

window = Tk()
window.title("Password Generator")
window.config(padx=40, pady=40)

# Canvas

img_png = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=img_png)
canvas.grid(column=1, row=0)

# Label

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)
label_website.focus()

label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)

label_pw = Label(text="Password:")
label_pw.grid(column=0, row=3)

# Input

input_website = Entry(width=34)
input_website.grid(column=1, row=1)

input_email = Entry(width=59)
input_email.grid(column=1, row=2, columnspan=2)
input_email.insert(0, string="sample.sample@email.com")

input_pw = Entry(width=34)
input_pw.grid(column=1, row=3)

# Button

button_generate = Button(text="Generate Password", width=20, highlightthickness=0, command=generate_pw)
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", width=50, highlightthickness=0, command=save_data)
button_add.grid(column=1, row=4, columnspan=2)

button_generate = Button(text="Search", width=20, highlightthickness=0, command=search_pw)
button_generate.grid(column=2, row=1)

window.mainloop()