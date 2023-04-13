import tkinter


def pens_to_szyling():
    pens = str(int(input_pens.get()) - 12)
    szyling = str(int(input_szyling.get()) + 1)

    if check(int(input_pens.get()), 12):
        input_pens.insert(0, pens)
        input_pens.delete(len(pens), len(input_pens.get()))
        input_szyling.insert(0, szyling)
        input_szyling.delete(len(szyling), len(input_szyling.get()))


def szyling_to_korona():
    szyling = str(int(input_szyling.get()) - 20)
    korona = str(int(input_korona.get()) + 1)

    if check(int(input_szyling.get()), 20):
        input_szyling.insert(0, szyling)
        input_szyling.delete(len(szyling), len(input_szyling.get()))
        input_korona.insert(0, korona)
        input_korona.delete(len(korona), len(input_korona.get()))


def korona_to_szyling():
    szyling = str(int(input_szyling.get()) + 20)
    korona = str(int(input_korona.get()) - 1)

    if check(int(input_korona.get()), 1):
        input_szyling.insert(0, szyling)
        input_szyling.delete(len(szyling), len(input_szyling.get()))
        input_korona.insert(0, korona)
        input_korona.delete(len(korona), len(input_korona.get()))


def szyling_to_pens():
    pens = str(int(input_pens.get()) + 12)
    szyling = str(int(input_szyling.get()) - 1)

    if check(int(input_szyling.get()), 1):
        input_pens.insert(0, pens)
        input_pens.delete(len(pens), len(input_pens.get()))
        input_szyling.insert(0, szyling)
        input_szyling.delete(len(szyling), len(input_szyling.get()))


def check(value1, value2):
    return value1 >= value2


def calculate():
    pens_output["text"] = f"{round(int(input_pens.get()) + int(input_szyling.get()) * 12 + int(input_korona.get()) * 240, 2)}"
    szyling_output["text"] = f"{round(int(input_pens.get()) / 12 + int(input_szyling.get()) + int(input_korona.get()) * 20, 2)}"
    korona_output["text"] = f"{round(int(input_pens.get()) / 240 + int(input_szyling.get()) / 20 + int(input_korona.get()), 2)}"


# SCREEN SETUP
window = tkinter.Tk()
window.title("Kalkulator Monet")
window.minsize(300, 200)
window.config(padx=20, pady=20)

# LABEL
pens_text = tkinter.Label(text="Brązowe Pensy", font=("Arial", 16, "bold"))
szyling_text = tkinter.Label(text="Srebrne Szylingi", font=("Arial", 16, "bold"))
korona_text = tkinter.Label(text="Złote Korony", font=("Arial", 16, "bold"))
pens_text.grid(column=0, row=1)
szyling_text.grid(column=2, row=1)
korona_text.grid(column=4, row=1)

# INPUT
input_pens = tkinter.Entry(width=10, font=("Arial", 16, "bold"))
input_szyling = tkinter.Entry(width=10, font=("Arial", 16, "bold"))
input_korona = tkinter.Entry(width=10, font=("Arial", 16, "bold"))
input_pens.insert(0, 0)
input_szyling.insert(0, 0)
input_korona.insert(0, 0)
input_pens.grid(column=0, row=0)
input_szyling.grid(column=2, row=0)
input_korona.grid(column=4, row=0)

# OUTPUT
pens_output = tkinter.Label(text=f"", font=("Arial", 24, "bold"))
szyling_output = tkinter.Label(text=f"", font=("Arial", 24, "bold"))
korona_output = tkinter.Label(text=f"", font=("Arial", 24, "bold"))
pens_output.grid(column=0, row=3)
szyling_output.grid(column=2, row=3)
korona_output.grid(column=4, row=3)

# BUTTON
pens2szyling = tkinter.Button(text="12→1", font=("Arial", 16, "bold"), command=pens_to_szyling)
szyling2korona = tkinter.Button(text="20→1", font=("Arial", 16, "bold"), command=szyling_to_korona)
korona2szyling = tkinter.Button(text="20←1", font=("Arial", 16, "bold"), command=korona_to_szyling)
szyling2pens = tkinter.Button(text="12←1", font=("Arial", 16, "bold"), command=szyling_to_pens)
policz = tkinter.Button(text="Policz", font=("Arial", 16, "bold"), command=calculate)
pens2szyling.grid(column=1, row=0)
szyling2korona.grid(column=3, row=0)
szyling2pens.grid(column=1, row=1)
korona2szyling.grid(column=3, row=1)
policz.grid(column=2, row=2)

# RUN
window.mainloop()
