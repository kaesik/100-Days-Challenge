import tkinter

window = tkinter.Tk()
window.title("Notes")
window.minsize(600, 400)

# LABEL
my_label = tkinter.Label(text="im a label", font=("Arial", 24, "bold"))
my_label.pack(side="bottom")

def add(*args):
    return sum(args)

print(add(1, 4, 10))
# RUN
window.mainloop()