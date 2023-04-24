import tkinter as tk
import math as mt
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
FONT_TIMER = (FONT_NAME, 35, "bold")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark_label.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = mt.floor(count / 60)
    count_sec = count % 60

    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = mt.floor(reps/2)
        for i in range(work_sessions):
            marks += "✓"
        checkmark_label.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro 🍅")
window.config(pady=50, padx=100,  bg=YELLOW)

# LABELS
timer_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=FONT_TIMER)
checkmark_label = tk.Label(text="", fg=GREEN, bg=YELLOW, font=FONT_TIMER)

# BUTTONS
start_button = tk.Button(text="Start", font=(FONT_NAME, 16, "bold"),
                         highlightthickness=0, command=start_timer)
reset_button = tk.Button(text="Reset", font=(FONT_NAME, 16, "bold"),
                         highlightthickness=0, command=reset_timer)

# CANVAS
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=FONT_TIMER)


# GRIDS
canvas.grid(column=1, row=1)
timer_label.grid(column=1, row=0)
checkmark_label.grid(column=1, row=3)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

window.mainloop()
