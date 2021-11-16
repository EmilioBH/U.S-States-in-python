import turtle
import pandas


sc = turtle.Screen()
sc.title("U.S. States Game")
image = "blank_states_img.gif"
sc.addshape(image)
turtle.shape(image)

answer_state = sc.textinput(title="Guess the State", prompt="What's another state's name? ").title()
print(answer_state)
