from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password manager')
window.config(padx=250, pady=250)

canvas = Canvas(width=200, height=189, highlightthickness=0)
lock = PhotoImage(file='logo.png')
canvas.create_image(100, 95, image=lock)
#timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

window.mainloop()