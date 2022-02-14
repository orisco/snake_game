from turtle import Turtle
# constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.initialize_snake()
        self.head = self.segments[0]

    def initialize_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.pu()
        new_segment.setpos(position)
        self.segments.append(new_segment)

    def extend_snake(self):
        self.add_segment(self.segments[-1].pos())

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)


    def snake_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def snake_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def snake_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def snake_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)