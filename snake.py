from turtle import Turtle
COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
34

class Snake:

    def __init__(self):
        self.all_turtle = []
        self.create_snake()
        self.head = self.all_turtle[0]

    def create_snake(self):
        for position in COORDINATES:
            self.add_seg(position)

    def add_seg(self, position):
        timmy = Turtle(shape="square")
        timmy.penup()
        timmy.color("white")
        timmy.goto(position)
        self.all_turtle.append(timmy)

    def reset(self):
        for segs in self.all_turtle:
            segs.goto(1000, 1000)
        self.all_turtle.clear()#clears all segments in the list
        self.create_snake()
        self.head = self.all_turtle[0]


    def extend(self):
        self.add_seg(self.all_turtle[-1].position())

    def move(self):
        for turtle_num in range(len(self.all_turtle) - 1, 0, -1):
            new_x = self.all_turtle[turtle_num - 1].xcor()
            new_y = self.all_turtle[turtle_num - 1].ycor()
            self.all_turtle[turtle_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)