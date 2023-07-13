import tkinter


def calculate():
    result["text"] = f"{float(input_mile.get()) * 161 / 100}"


# SCREEN SETUP
window = tkinter.Tk()
window.title("Notes")
window.minsize(300, 200)
window.config(padx=20, pady=20)

# LABEL
miles = tkinter.Label(text="Miles", font=("Arial", 24, "bold"))
is_equal_to = tkinter.Label(text="is equal to", font=("Arial", 24, "bold"))
km = tkinter.Label(text="Km", font=("Arial", 24, "bold"))
result = tkinter.Label(text=f"", font=("Arial", 24, "bold"))
miles.grid(column=2, row=0)
is_equal_to.grid(column=0, row=1)
km.grid(column=2, row=1)
result.grid(column=1, row=1)

#ENTRY
input_mile = tkinter.Entry(width=10, font=("Arial", 24, "bold"))
input_mile.grid(column=1, row=0)

# BUTTON
calculate_button = tkinter.Button(text="Calculate", font=("Arial", 24, "bold"), command=calculate)
calculate_button.grid(column=1, row=2)

# RUN
window.mainloop()
