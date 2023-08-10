import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guess = True
correct_guesses = []
# states_to_learn = []

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

while guess:

    if len(correct_guesses) == 0:
        answer = screen.textinput(title="Guess The State", prompt="Guess a state!")
    elif len(correct_guesses) == 50:
        guess = False
    else:
        answer = screen.textinput(title=f"{len(correct_guesses)}/50 Guess The State", prompt="What's another state's name?")

    t_answer = answer.title()

    if t_answer == "Exit":
        # for guessed in states:
        #     if guessed not in correct_guesses:
        #         states_to_learn.append(guessed)
        states_to_learn = [item for item in states if item not in correct_guesses]
        pandas.DataFrame(states_to_learn).to_csv("States to learn.csv")
        break
    if t_answer in states:
        correct_guesses.append(t_answer)
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        text.goto(int(data.loc[data.state.isin([t_answer]), "x"]), int(data.loc[data.state.isin([t_answer]), "y"]))
        text.write(t_answer)
