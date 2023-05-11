import tkinter as tk
from tkinter import messagebox as msgb
import random
import pyperclip
import json
# ---------------------------- CONSTANTS ------------------------------- #
L_BLUE = "#F1F6F9"
N_BLUE = "#394867"
D_BLUE = "#212A3E"
GRAY = "#9BA4B5"
FONT = ("Courier", 12, "bold")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_input.delete(0, "end")

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_lst = password_letters + password_symbols + password_numbers
    random.shuffle(password_lst)

    password = "".join(password_lst)
    pyperclip.copy(password)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get().capitalize()
    email = email_user_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    is_ok = False

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        msgb.showwarning(title="Error!", message="Please, don't leave any fields empty!")
    else:
        is_ok = msgb.askokcancel(title=website.capitalize(), message=f"Details:\n"
                                                f" Email: {email}\n"
                                                f" Password: {password}\n"
                                                f" Is that correct?")

    if is_ok:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)                 # reading old data

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)    # saving new data

        else:
            data.update(new_data)                          # updating old data
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)        # saving old data

        finally:
            website_input.delete(0, "end")
            password_input.delete(0, "end")


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    search = website_input.get().capitalize()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        msgb.showinfo(title="Error", message=f"No data file found.")

    else:
        if search in data:
            website = data[search]
            email = website["email"]
            password = website["password"]
            msgb.showinfo(title=search, message=f"Details:\n"
                                                f" Email: {email}\n"
                                                f" Password: {password}\n")
        elif search == "":
            msgb.showinfo(title="Error", message=f"Website cannot be blank.")
        else:
            msgb.showinfo(title="Error", message=f"No details for {search} exist.")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager 🔒")
window.config(pady=50, padx=50, bg=L_BLUE)

# LABELS
website_label = tk.Label(text="Website:", fg=D_BLUE, bg=L_BLUE, font=FONT)
website_label.grid(column=0, row=1)

email_user_label = tk.Label(text="Email/Username:", fg=D_BLUE, bg=L_BLUE, font=FONT)
email_user_label.grid(column=0, row=2)

password_label = tk.Label(text="Password:", fg=D_BLUE, bg=L_BLUE, font=FONT)
password_label.grid(column=0, row=3)

# CANVAS
canvas = tk.Canvas(width=200, height=200, bg=L_BLUE, highlightthickness=0)
logo_img = tk.PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# BUTTONS
generate_button = tk.Button(text="Generate Password", font=FONT, width=20,
                         highlightthickness=0, command=generate_password)
generate_button.grid(column=2, row=3)

search_button = tk.Button(text="Search", font=FONT, width=20,
                         highlightthickness=0, command=find_password)
search_button.grid(column=2, row=1)

add_button = tk.Button(text="Add", font=FONT, width=40,
                         highlightthickness=0, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)



# INPUT
website_input = tk.Entry(width=19, font=FONT)
website_input.grid(column=1, row=1)
website_input.focus()

email_user_input = tk.Entry(width=40, font=FONT)
email_user_input.grid(column=1, row=2, columnspan=2)
email_user_input.insert(0, "kamil.sobania.97@gmail.com")

password_input = tk.Entry(width=19, font=FONT)
password_input.grid(column=1, row=3)


window.mainloop()
