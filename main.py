import tkinter

window = tkinter.Tk()
window.title("Password Manager Python")
window.minsize(width=500, height=300)

# Introduction
label_intro = tkinter.Label(text="Welcome. You can store your passwords, generate password, and retrieve stored data!")
label_intro.grid(column=1, row=1)

# Website
label_website = tkinter.Label(text="Website: ")
label_website.grid(column=1, row=2)

input_website = tkinter.Entry(width=15)
input_website.grid(column=2, row=2)

def search_btn():
    print("here")
    # changing label on click: the_label.config(text="")

btn_search = tkinter.Button(text="Search", fg="black", bg="grey", command="search_btn")
btn_search.grid(column=3, row=2)

# Email/username

label_email = tkinter.Label(text="Email or username: ")
label_email.grid(column=1, row=3)

input_email = tkinter.Entry(width=15)
input_email.grid(column=2, row=3)

# Password
label_password = tkinter.Label(text="Website: ")
label_password.grid(column=1, row=4)

input_password = tkinter.Entry(width=15)
input_password.grid(column=2, row=4)


def generate_btn():
    print("here")
    # changing label on click: the_label.config(text="")


btn_password = tkinter.Button(
    text="Search", fg="black", bg="grey", command="generate_btn")
btn_password.grid(column=3, row=4)

# Add new password

def add_btn():
    print("here")
    # changing label on click: the_label.config(text="")

btn_password = tkinter.Button(
    text="Search", fg="black", bg="white", command="ass_btn")
btn_password.grid(column=1, row=5)

window.mainloop()
