import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
L_BLUE = "#F1F6F9"
N_BLUE = "#394867"
D_BLUE = "#212A3E"
GRAY = "#9BA4B5"
FONT = ("Courier", 12, "bold")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    pass


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

add_button = tk.Button(text="Add", font=FONT, width=40,
                         highlightthickness=0, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

# INPUT
website_input = tk.Entry(width=40, font=FONT)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_user_input = tk.Entry(width=40, font=FONT)
email_user_input.grid(column=1, row=2, columnspan=2)
email_user_input.insert(0, "kamil.sobania.97@gmail.com")

password_input = tk.Entry(width=19, font=FONT)
password_input.grid(column=1, row=3)


window.mainloop()
