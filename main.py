from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Roboto Slab"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager 🔐")
window.config(padx = 50, pady = 50)

# canvas
canvas = Canvas(width=200, height=200)

# Lock image
lock_img = PhotoImage(file = "logo.png")
canvas.create_image(100,100, image = lock_img)
canvas.grid(column = 1, row = 0)

# Website Label
website_label = Label(text = "Website:", font = (FONT_NAME, 15, "bold"))
website_label.grid(column= 0, row = 1)

# Website entry
website_entry = Entry(width = 35)
# put cursor right in website from the begninning
website_entry.focus()
website_entry.grid(column = 1, row = 1, columnspan=2)

# Email/Username Label
email_label = Label(text = "Email/Username:", font = (FONT_NAME, 15, "bold"))
email_label.grid(column= 0, row = 2)

# Email/Username Entry
email_entry = Entry(width = 35)
# put the most used email as the predetermined email
email_entry.insert(END, "example@gmail.com")
email_entry.grid(column = 1, row = 2, columnspan=2)

# Password label
password_label = Label(text = "Password:", font = (FONT_NAME, 15, "bold"))
password_label.grid(column= 0, row = 3)

# Password entry
password_entry = Entry(width = 17)
password_entry.grid(column = 1, row = 3)

# Generate Password Button
password_button = Button(text = "Generate Password")
password_button.grid(column = 2, row =3)

# Add Button
add_button = Button(text = "add", width= 30)
add_button.grid(column = 1, row =4, columnspan=2)

window.mainloop()