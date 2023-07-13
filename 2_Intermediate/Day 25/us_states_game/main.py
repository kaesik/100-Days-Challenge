import turtle
import csv
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
FONT = ("Courier", 12, "bold")
guessed_states = []
all_states = []


class State(turtle.Turtle):
    def __init__(self, name, pos):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(pos)
        self.write(arg=name, align="center", move=True, font=FONT)


with open("50_states.csv") as file:
    reader = csv.reader(file)
    file_list = list(reader)

for state, x, y in file_list[1:]:
    all_states.append(state)

while len(guessed_states) != 50:
    screen.update()
    answer_state = screen.textinput(title=f"Guess the state, {len(guessed_states)}/50", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        not_guessed_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         not_guessed_states.append(state)
        data = pandas.DataFrame(not_guessed_states)
        data.to_csv("states_to_learn.csv")
        break
    for state, x, y in file_list[1:]:
        if state in guessed_states:
            continue
        if state == answer_state:
            guessed_states.append(str(state))
            State(str(state), (int(x), int(y)))

turtle.mainloop()