import tkinter
from tkinter import messagebox
import string
import random
import pyperclip
import json

window = tkinter.Tk()
window.title("Password Manager Python")
window.config(padx=15, pady=15, bg="alice blue")

# Introduction
canvas_intro = tkinter.Canvas(height=210, width=210, bg="alice blue")
canvas_img = tkinter.PhotoImage(file="lock.png")
canvas_intro.create_image(105, 105, image=canvas_img)
canvas_intro.grid(column=1, row=0, columnspan=3)

label_intro = tkinter.Label(
    text="\nWelcome! You can store your passwords, generate passwords, and retrieve stored data!\nWhen you generate a password it will be automatically copied to your clipboard.\n",bg="alice blue")
label_intro.grid(column=1, row=1, columnspan=3)

# Website
label_website = tkinter.Label(text="Website: ", bg="alice blue")
label_website.grid(column=1, row=2)

input_website = tkinter.Entry(width=30)
input_website.grid(column=2, row=2)
input_website.focus()

def search_btn():
    account_searched = input_website.get()
    if len(account_searched) == 0:
        warn_user = messagebox.showinfo(
            title="Empty field", message="Type the name of the account in order for information be retrieved.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)  # reading old data
        except FileNotFoundError:
            messagebox.showwarning(title="Error", message="No data file on record.")
        else:
            if account_searched in data:
                the_email = data[account_searched]["email"]
                the_password = data[account_searched]["password"]
                messagebox.showinfo(
                    title=f"Account information for {account_searched}", message=f"Email: {the_email}\nPassword: {the_password}")
            else:
                messagebox.showinfo(
                    title="Information not found", message=f"No record for {account_searched} was found.")

btn_search = tkinter.Button(text="Search", fg="black", bg="light slate gray", command=search_btn, width=18)
btn_search.grid(column=3, row=2)

# Email/username

label_email = tkinter.Label(text="Email or username: ", bg="alice blue")
label_email.grid(column=1, row=3)

input_email = tkinter.Entry(width=55)
input_email.grid(column=2, row=3, columnspan=3)

# Password
label_password = tkinter.Label(text="Password: ", bg="alice blue")
label_password.grid(column=1, row=4)

input_password = tkinter.Entry(width=30)
input_password.grid(column=2, row=4)

def generate_btn():
    # generating a random password:
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = ["!", "*", "$", "%", "+"]
    ranNumb = random.randint(1,2) #symbols might be included or not
    the_letters = [random.choice(letters) for _ in range(random.randint(5, 10))]
    the_numbers = [random.choice(numbers) for _ in range(random.randint(2,6))]
    password_list = the_letters + the_numbers
    nr_symbols = random.randint(1, 2)
    if ranNumb == 2:
        for symbol in range(nr_symbols):
            password_list.append(random.choice(symbols))
    random.shuffle(password_list)
    the_password = ''.join(password_list)
    input_password.delete(0, tkinter.END)
    input_password.insert(0, the_password)
    pyperclip.copy(the_password)

btn_password = tkinter.Button(
    text="Generate password", fg="black", bg="light slate gray", width=18, command=generate_btn)
btn_password.grid(column=3, row=4)

# Add new password

def add_btn():
    the_site = input_website.get()
    the_mail = input_email.get()
    the_pwd = input_password.get()
    new_data = {
        the_site: {
            "email": the_mail,
            "password": the_pwd
        }
    }
    
    if len(the_site) == 0 or len(the_mail) == 0 or len(the_mail) == 0:
        user_warning = messagebox.showinfo(title="Empty fields", message="Make sure not to leave any field empty.")
    else:
        user_confirmation = messagebox.askokcancel(
            title="Check information before saving", message=f"Website: {the_site}\nEmail/username: {the_mail}\nPassword: {the_pwd}\n\nClick 'ok' to save.")
        if user_confirmation:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file) # reading old data
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)  # if no file, create a new json file and add new_data
            else:
                data.update(new_data) # updating old data with new data
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4) # saving updated file
            finally:
                input_website.delete(0, tkinter.END)
                input_email.delete(0, tkinter.END)
                input_password.delete(0, tkinter.END)

btn_password = tkinter.Button(
    text="Add password", fg="black", bg="DarkGoldenrod1", width=25, command=add_btn)
btn_password.grid(column=2, row=5)

window.mainloop()
