from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = ''.join(password_list)

    input_pass.delete(0, END)
    input_pass.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input_web.get()
    email = input_email.get()
    password = input_pass.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    if len(website) < 1 or len(password) < 1:
        messagebox.showerror(title='Fields empty', message="Please don't leave any empty fields")
        return

    is_yes = messagebox.askyesno(title=website, message=f'Are you sure this information is correct?\n'
                                                    f'Email: {email}\nPassword: {password}')
    if is_yes:
        try:
            with open("data.json", 'r') as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", 'w') as data_file:
                # saving new data
                json.dump(new_data, data_file, indent=4)
        else:
            # updating data
            data.update(new_data)
            with open("data.json", 'w') as data_file:
                # saving new data
                json.dump(data, data_file, indent=4)
        finally:
            input_web.delete(0, END)
            input_pass.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password manager')
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=0, )

webs_lbl = Label(text='Website:')
webs_lbl.grid(column=0, row=1)
email_lbl = Label(text='Email/Username:')
email_lbl.grid(column=0, row=2)
pass_lbl = Label(text='Password:')
pass_lbl.grid(column=0, row=3)

input_web = Entry(width=40)
input_web.grid(column=1, row=1, columnspan=2)
input_web.focus()
input_email = Entry(width=40)
input_email.grid(column=1, row=2, columnspan=2)
input_email.insert(0, 'xander@gmail.com')
input_pass = Entry(width=22)
input_pass.grid(column=1, row=3)

generate_button = Button(text='Generate Password', command=generate)
generate_button.grid(column=2, row=3)
add_button = Button(text='Add', width=34, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
