import tkinter

window = tkinter.Tk()
window.title("Password Manager Python")
window.config(padx=15, pady=15)

# Introduction
canvas_intro = tkinter.Canvas(height=210, width=210)
canvas_img = tkinter.PhotoImage(file="lock.png")
canvas_intro.create_image(105, 105, image=canvas_img)
canvas_intro.grid(column=1, row=0, columnspan=3)

label_intro = tkinter.Label(
    text="Welcome! You can store your passwords, generate passwords, and retrieve stored data!")
label_intro.grid(column=1, row=1, columnspan=3)

# Website
label_website = tkinter.Label(text="Website: ")
label_website.grid(column=1, row=2)

input_website = tkinter.Entry(width=30)
input_website.grid(column=2, row=2)

def search_btn():
    print("here")

btn_search = tkinter.Button(text="Search", fg="black", bg="light slate gray", command="search_btn", width=18)
btn_search.grid(column=3, row=2)

# Email/username

label_email = tkinter.Label(text="Email or username: ")
label_email.grid(column=1, row=3)

input_email = tkinter.Entry(width=54)
input_email.grid(column=2, row=3, columnspan=3)

# Password
label_password = tkinter.Label(text="Password: ")
label_password.grid(column=1, row=4)

input_password = tkinter.Entry(width=30)
input_password.grid(column=2, row=4)


def generate_btn():
    print("here")


btn_password = tkinter.Button(
    text="Generate password", fg="black", bg="light slate gray", command="generate_btn", width=18)
btn_password.grid(column=3, row=4)

# Add new password

def add_btn():
    print("here")

btn_password = tkinter.Button(
    text="Add password", fg="black", bg="DarkGoldenrod1", command="add_btn", width=25)
btn_password.grid(column=2, row=5)

window.mainloop()
