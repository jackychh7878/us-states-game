import turtle
import pandas
FONT = ("Courier", 8, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

map_locator = turtle.Turtle()
map_locator.hideturtle()
map_locator.penup()

game_data = pandas.read_csv("50_states.csv")
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in game_data.state:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("learning_data.csv")
        break

    if answer_state in game_data.state.to_list():
        guessed_states.append(answer_state)
        correct_answer = game_data[game_data.state == answer_state]
        map_locator.goto(correct_answer.x.iloc[0], correct_answer.y.iloc[0])
        map_locator.write(f"{answer_state}", align="center", font=FONT)

turtle.mainloop()
