import tkinter


def calculate():
    punkty_sukcesu = int(input_ps.get())

    if punkty_sukcesu < 0:
        punkty_sukcesu_procent = 25
    elif 0 <= punkty_sukcesu and punkty_sukcesu <= 2:
        punkty_sukcesu_procent = 30
    elif 3 <= punkty_sukcesu and punkty_sukcesu <= 4:
        punkty_sukcesu_procent = 40
    elif 5 <= punkty_sukcesu and punkty_sukcesu <= 6:
        punkty_sukcesu_procent = 50
    else:
        punkty_sukcesu_procent = 60

    if przedmiot_kupiony_state.get():
        przedmiot_kupiony_procent = 15
    else:
        przedmiot_kupiony_procent = 0

    if poswiecony_czas_state.get():
        poswiecony_czas_procent = 10
    else:
        poswiecony_czas_procent = 0

    total_procent = punkty_sukcesu_procent + przedmiot_kupiony_procent + poswiecony_czas_procent
    punkty_sukcesu_output["text"] = f"{punkty_sukcesu_procent}%"
    pens_output["text"] = f"{round(int(input_pens.get()) * total_procent / 100, 2)}"
    szyling_output["text"] = f"{round(int(input_szyling.get()) * total_procent / 100, 2)}"
    korona_output["text"] = f"{round(int(input_korona.get()) * total_procent / 100, 2)}"


# SCREEN SETUP
window = tkinter.Tk()
window.title("Kalkulator Handlu")
window.minsize(300, 200)
window.config(padx=20, pady=20)

# LABEL
punkty_sukcesu_text = tkinter.Label(text="Punkty Sukcesu", font=("Arial", 16, "bold"))
pens_text = tkinter.Label(text="BP", font=("Arial", 16, "bold"))
szyling_text = tkinter.Label(text="SS", font=("Arial", 16, "bold"))
korona_text = tkinter.Label(text="ZK", font=("Arial", 16, "bold"))
procent_kupiony1_text = tkinter.Label(text="Przedmiot Kupiony", font=("Arial", 16, "bold"))
procent_kupiony2_text = tkinter.Label(text="15%", font=("Arial", 16, "bold"))
procent_czas1_text = tkinter.Label(text="Poświęcony Czas", font=("Arial", 16, "bold"))
procent_czas2_text = tkinter.Label(text="10%", font=("Arial", 16, "bold"))
cena_rynkowa_text = tkinter.Label(text="Cena Rynkowa", font=("Arial", 16, "bold"))
propozycja_handlarza = tkinter.Label(text="Propozycja Handlarza", font=("Arial", 16, "bold"))
punkty_sukcesu_text.grid(column=0, row=0)
pens_text.grid(column=0, row=6)
szyling_text.grid(column=0, row=5)
korona_text.grid(column=0, row=4)
cena_rynkowa_text.grid(column=1, row=3)
propozycja_handlarza.grid(column=2, row=3)
procent_kupiony1_text.grid(column=0, row=1)
procent_kupiony2_text.grid(column=2, row=1)
procent_czas1_text.grid(column=0, row=2)
procent_czas2_text.grid(column=2, row=2)

# INPUT
input_pens = tkinter.Entry(width=10, font=("Arial", 16, "bold"))
input_szyling = tkinter.Entry(width=10, font=("Arial", 16, "bold"))
input_korona = tkinter.Entry(width=10, font=("Arial", 16, "bold"))
input_ps = tkinter.Entry(width=10, font=("Arial", 16, "bold"))
input_pens.insert(0, 0)
input_szyling.insert(0, 0)
input_korona.insert(0, 0)
input_ps.insert(0, 0)
input_ps.grid(column=1, row=0)
input_pens.grid(column=1, row=6)
input_szyling.grid(column=1, row=5)
input_korona.grid(column=1, row=4)

# CHECK
przedmiot_kupiony_state = tkinter.IntVar()
poswiecony_czas_state = tkinter.IntVar()
przedmiot_kupiony_check = tkinter.Checkbutton(variable=przedmiot_kupiony_state)
poswiecony_czas_check = tkinter.Checkbutton(variable=poswiecony_czas_state)
przedmiot_kupiony_check.grid(column=1, row=1)
poswiecony_czas_check.grid(column=1, row=2)

# OUTPUT
pens_output = tkinter.Label(text=f"", font=("Arial", 24, "bold"))
szyling_output = tkinter.Label(text=f"", font=("Arial", 24, "bold"))
korona_output = tkinter.Label(text=f"", font=("Arial", 24, "bold"))
punkty_sukcesu_output = tkinter.Label(text=f"", font=("Arial", 16, "bold"))
pens_output.grid(column=2, row=6)
szyling_output.grid(column=2, row=5)
korona_output.grid(column=2, row=4)
punkty_sukcesu_output.grid(column=2, row=0)

# BUTTON
policz = tkinter.Button(text="Policz", font=("Arial", 16, "bold"), command=calculate)
policz.grid(column=0, row=3)

# RUN
window.mainloop()
