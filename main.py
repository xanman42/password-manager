from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = input_web.get()
    email = input_email.get()
    password = input_pass.get()

    if len(web) < 1 or len(password) < 1:
        messagebox.showerror(title='Fields empty', message="Please don't leave any empty fields")
        return

    is_yes = messagebox.askyesno(title=web, message=f'Are you sure this information is correct?\n'
                                                    f'Email: {email}\nPassword: {password}')
    if is_yes:
        with open("data.txt", 'a') as data:
            data.write(f"{web} | {email} | {password} \n")

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

generate_button = Button(text='Generate Password')
generate_button.grid(column=2, row=3)
add_button = Button(text='Add', width=34, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
