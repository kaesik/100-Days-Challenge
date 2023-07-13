import tkinter

window = tkinter.Tk()
window.title("Notes")
window.minsize(600, 400)
window.config(padx=20, pady=20)


def button_clicked():
    my_label["text"] = f"{input.get()}"


# LABEL
my_label = tkinter.Label(text="im a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label["text"] = "new text"

# BUTTON
button1 = tkinter.Button(text="button1", command=button_clicked)
button2 = tkinter.Button(text="button2", command=button_clicked)
button1.grid(column=1, row=1)
button2.grid(column=2, row=0)

#ENTRY
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)

# RUN
window.mainloop()


"""
def add(*args):
    return sum(args)

print(add(1, 4, 10))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]

calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="Nissan", model="GT-R")
"""
