#
# from turtle import Turtle
# STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# CONSTANT_DISTANCE=20
#
#
# class Snake:
#
#     def __init__(self):
#         self.segment_move= []
#         self.create_snake()
#     def create_snake(self):
#         for position_move in STARTING_POSITIONS:
#             # new_segment.speed("slow")
#             new_segment = Turtle(shape="square")
#             new_segment.color("white")
#             new_segment.penup()
#             new_segment.goto(position_move)
#             self.segment_move.append(new_segment)
#     def move(self):
#         for seg_num in range(len(self.segment_move) - 1, 0, -1):
#             new_x = self.segment_move[seg_num - 1].xcor()
#             new_y = self.segment_move[seg_num - 1].ycor()
#             self.segment_move[seg_num].goto(new_x, new_y)
#         self.segment_move[0].forward(CONSTANT_DISTANCE)
#         # self.segment_move[0].left(90)
#     def up(self):
#         self.segment_move[0].setheading(90)
#     def down(self):
#         pass
#     def right(self):
#         pass
#     def left(self):
#         pass
#
from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    def reset(self):
        for each_segment in self.segments:
            each_segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]

    def extend_snake_size(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

