import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Password Manager Python")
window.config(padx=15, pady=15, bg="alice blue")

# Introduction
canvas_intro = tkinter.Canvas(height=210, width=210, bg="alice blue")
canvas_img = tkinter.PhotoImage(file="lock.png")
canvas_intro.create_image(105, 105, image=canvas_img)
canvas_intro.grid(column=1, row=0, columnspan=3)

label_intro = tkinter.Label(
    text="Welcome! You can store your passwords, generate passwords, and retrieve stored data!",bg="alice blue")
label_intro.grid(column=1, row=1, columnspan=3)

# Website
label_website = tkinter.Label(text="Website: ", bg="alice blue")
label_website.grid(column=1, row=2)

input_website = tkinter.Entry(width=30)
input_website.grid(column=2, row=2)
# input_website.focus()

def search_btn():
    print("here")

btn_search = tkinter.Button(text="Search", fg="black", bg="light slate gray", command="search_btn", width=18)
btn_search.grid(column=3, row=2)

# Email/username

label_email = tkinter.Label(text="Email or username: ", bg="alice blue")
label_email.grid(column=1, row=3)

input_email = tkinter.Entry(width=54)
input_email.grid(column=2, row=3, columnspan=3)

# Password
label_password = tkinter.Label(text="Password: ", bg="alice blue")
label_password.grid(column=1, row=4)

input_password = tkinter.Entry(width=30)
input_password.grid(column=2, row=4)


def generate_btn():
    print("here")


btn_password = tkinter.Button(
    text="Generate password", fg="black", bg="light slate gray", width=18, command="generate_btn")
btn_password.grid(column=3, row=4)

# Add new password

def add_btn():
    the_site = input_website.get()
    the_mail = input_email.get()
    the_pwd = input_password.get()
    
    if len(the_site) == 0 or len(the_mail) == 0 or len(the_mail) == 0:
        user_warning = messagebox.showinfo(title="Empty fields", message="Make sure not to leave any field empty.")
    else:
        user_confirmation = messagebox.askokcancel(
            title="Check information before saving", message=f"Website: {the_site}\nEmail/username: {the_mail}\nPassword: {the_pwd}\nClick 'ok' to save.")
        if user_confirmation:
            with open("pmp.txt", "a") as data_file:
                data_file.write(f"{the_site}|{the_mail}|{the_pwd}\n")
                input_website.delete(0, tkinter.END)
                input_email.delete(0, tkinter.END)
                input_password.delete(0, tkinter.END)

btn_password = tkinter.Button(
    text="Add password", fg="black", bg="DarkGoldenrod1", width=25, command=add_btn)
btn_password.grid(column=2, row=5)

window.mainloop()
