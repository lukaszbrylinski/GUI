import turtle
import pandas

turt = turtle.Turtle()
turt.hideturtle()
turt.penup()

data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

all_states = data.state.to_list()
turtle.shape(image)

guessed_states = []
missed_states = []
while len(guessed_states)<50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="What's another state's name?").title()
    # answer_state = answer_state.capitalize()
    # print(answer_state)
    if answer_state == "Exit":
        missed_states = [state for state in all_states if state not in quessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missed_states.append(state)
        # print(missed_states)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        # print(answer_state)
        guessed_states.append(answer_state)

        cur_state = data[data.state == answer_state]

        x_cor = int(cur_state.x)

        y_cor = int(cur_state.y)
        turt.goto(int(cur_state.x),int(cur_state.y))
        turt.write(answer_state,font=("Arial","8","normal"))

states_to_learn = []
# for item in all_states:
#     if item not in guessed_states:
#         states_to_learn.append(item)
#
# df = pandas.DataFrame(states_to_learn)
# df.to_csv("states_to_learn.csv")
