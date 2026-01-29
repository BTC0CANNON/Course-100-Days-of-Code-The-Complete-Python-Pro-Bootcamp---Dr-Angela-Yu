"""Be aware that I had to make some changes to the screen
and map out the coordinates for myself, because I am working
on a Linux system that is split between two screens. Some
of this may not apply to your situation (e.g.
screen.setup(width=725, height=491, startx=600).
Use the original_50_states.csv, strike because 50_states.csv is
strike mapped out for my setup and personal taste as to placement
strike of the state titles.
because mine is crap."""

"""Code to map coordinates yourself"""
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

"""Code to check your coordinates when you start second-guessing yourself"""
# tim = turtle.Turtle()
# tim.penup()
# tim.goto(271, 33)

"""Where to go learn how to ba able to strikethrough comments in Pycharm:
https://stackoverflow.com/questions/67609528/how-to-strikethrough-in-pycharm-comments"""

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=725, height=491, startx=600)
turtle.shape(image)

data = pandas.read_csv("original_50_states.csv")

"""My Code"""
writer = turtle.Turtle()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's a state's name?").title()
    match = data[data.state == answer_state]
    if not match.empty:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            temp_data = match.iloc[0]
            writer.color("black")
            writer.penup()
            writer.hideturtle()
            writer.goto(temp_data.x, temp_data.y)
            writer.write(f"{temp_data.state}", align="left", font=("Courier", 10, "normal"))
    elif answer_state.lower() == "exit":
        break

no_match = data[~data.state.isin(guessed_states)]
to_study = no_match.state
to_study.to_csv("states_to_study.csv", index=False)

"""Angela's Code"""
# all_states = data.state.to_list()
# guessed_states = []

# while len(guessed_states) < 50:
#     answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
#                                     prompt="What's another state's name?").title()
#     if answer_state == "Exit":
#         missing_states = []
#         for state in all_states:
#             if state not in guessed_states:
#                 missing_states.append(state)
#         new_data = pandas.DataFrame(missing_states)
#         new_data.to_csv("states_to_learn.csv")
#         break
#     if answer_state in all_states:
#         guessed_states.append(answer_state)
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         state_data = data[data.state == answer_state]
#         t.goto(state_data.x.item(), state_data.y.item())
#         t.write(answer_state)
