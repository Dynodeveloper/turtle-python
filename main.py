from turtle import Screen, Turtle

screen = Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Stelar")



starting_positions=[(0,0),(-17,0),(-38,0)]

segments= []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("lightpink")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True

while game_is_on:
    for seg in segments:
        seg.forward(20)












screen.exitonclick()

