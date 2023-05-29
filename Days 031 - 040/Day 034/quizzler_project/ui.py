import tkinter as tk
import time as tm
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
GREEN = "#5D9C59"
RED = "#F55050"
WHITE = "#F0F0F0"
FONT = ("Arial", 20, "italic")


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        true_image = tk.PhotoImage(file="./images/true.png")
        false_image = tk.PhotoImage(file="./images/false.png")

        self.canvas = tk.Canvas(width=300, height=250, bg=WHITE)
        self.question = self.canvas.create_text(150, 125, text="Question", width=280, font=FONT, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score = tk.Label(text=f"Score: {self.quiz.score}/{self.quiz.question_number}", font=FONT, bg=THEME_COLOR, fg=WHITE)
        self.score.grid(row=4, column=0, columnspan=2)

        self.category = tk.Label(text=f"Category:\n{self.quiz.category}", width=30, font=FONT, bg=THEME_COLOR, fg=WHITE)
        self.category.grid(row=0, column=0, columnspan=2)

        self.true = tk.Button(image=true_image, highlightthickness=0, command=self.true_ans)
        self.true.grid(row=2, column=0)

        self.false = tk.Button(image=false_image, highlightthickness=0, command=self.false_ans)
        self.false.grid(row=2, column=1)

        self.get_question()

        self.window.mainloop()

    def get_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            q_category = self.quiz.category
            self.canvas.itemconfig(self.question, text=q_text)
            self.category.config(text=f"Category:\n{q_category}")
        else:
            self.score.config(text=f"")
            self.canvas.itemconfig(self.question,
                                   text=f"Congratulation!\n"
                                        f"Your Final score is:\n"
                                        f"{self.quiz.score}/{self.quiz.question_number}")
            self.true.config(state="disabled")
            self.false.config(state="disabled")
        self.canvas.config(bg=WHITE)

    def true_ans(self):
        self.feedback(self.quiz.check_answer("True"))
        self.score.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")

    def false_ans(self):
        self.feedback(self.quiz.check_answer("False"))
        self.score.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")

    def feedback(self, check):
        self.click()
        if check:
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.config(bg=RED)
        self.window.after(1500, lambda: self.get_question())

    def button_off(self):
        self.true.config(state="disabled")
        self.false.config(state="disabled")

    def button_on(self):
        self.true.config(state="active")
        self.false.config(state="active")

    def click(self):
        self.button_off()
        self.window.after(1500, lambda: self.button_on())