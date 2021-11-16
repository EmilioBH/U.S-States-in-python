import turtle
import pandas

game_on = True
states_guessed = []

sc = turtle.Screen()
sc.title("U.S. States Game")
image = "blank_states_img.gif"
sc.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
print(data)

while game_on:
    answer_state = sc.textinput(title=f"{len(states_guessed)}/50 Guess the State",
                                prompt="What's another state's name? ").title()
    print(answer_state)

    counter = 0
    for state in data["state"]:
        if state == answer_state and state not in states_guessed:
            states_guessed.append(state)
            if len(states_guessed) == 50:
                game_on = False
            x_cord = data["x"]
            y_cord = data["y"]
            new_state = turtle.Turtle()
            new_state.penup()
            new_state.goto(x_cord[counter], y_cord[counter])
            new_state.write(f"{state}")
            new_state.hideturtle()

        counter += 1

end_game = turtle.Turtle()
end_game.hideturtle()
end_game.color("red")
end_game.write("You complete the game!! 😁", font=("Arial", 20, "normal"))
sc.exitonclick()

