from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Roboto Slab"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(6, 8)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

def random_password():
    # list comprehension: new_list = [new_item for item in list]
    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    #for char in range(nr_letters):
        #password_list.append(random.choice(letters))

    #for char in range(nr_symbols):
        #password_list += random.choice(symbols)

    #for char in range(nr_numbers):
        #password_list += random.choice(numbers)

    random.shuffle(password_list)

    # .join() is a way to put together all the elements in password_list
    password = "".join(password_list)

    #for char in password_list:
        #password += char

    return password_entry.insert(END, string = password)

# ---------------------------- SEARCH BUTTON ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open(file="passwords.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title = "Error", message = f"You have not saved an account for {website} yet")
    # if the try succeeds, you can continue with this else
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]['password']
            return messagebox.showinfo(title = website, message= f"email: {email} \npassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"You have not saved an account for {website} yet")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password" : password,
    }}

    # what happens if the user doesn't enter anything either in the password or website
    if len(website) == 0 or len(password) == 0:
       messagebox.showerror(title= "Error", message= "You cannot leave either the website or email in blank.")

    else:
        double_check = f"These are the details entered: \nWebsite: {website} \nEmail: {email} \nPassword: {password} \nIs it okay to save?"
        is_ok = messagebox.askokcancel(title= website, message= double_check)

        if is_ok == True:
            try:
                # Write into the passwords.json file
                with open(file = "passwords.json", mode = "r") as file:
                    # this is how you write into a json file
                    #json.dump(new_data, file, indent = 4)
                    # this is how you raed from a json file
                    #data = json.load(file)
                    #print(data)
                    # this is how you update data in a json file without overwrite it
                    # Step 1: Reading Old Data
                    data = json.load(file)
                    # Step 2: Updating old data
                    data.update(new_data)
                # With open the data in write mode
                with open(file="passwords.json", mode="w") as file:
                    # Saving updated data
                    json.dump(data, file, indent = 4)
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)
            except FileNotFoundError:
                with open(file="passwords.json", mode="w") as file:
                    json.dump(new_data, file, indent = 4)

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
website_entry = Entry(width = 20)
# put cursor right in website from the begninning
website_entry.focus()
website_entry.grid(column = 1, row = 1)

# Search Button
search_button = Button(text = "Search", command = find_password, width = 15)
search_button.grid(column = 2, row =1)

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
password_entry = Entry(width = 18)
password_entry.grid(column = 1, row = 3)

# Generate Password Button
password_button = Button(text = "Generate Password", command = random_password)
password_button.grid(column = 2, row =3)

# Add Button
add_button = Button(text = "add", command= save_password, width= 30)
add_button.grid(column = 1, row =4, columnspan=2)

window.mainloop()