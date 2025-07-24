from turtle import Turtle
with open("data.txt") as file:
    text_score=file.read()
class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score=int(text_score)
        self.color("yellow")
        self.penup()
        self.goto(-10, 270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"here is your 👾👾score: {self.score}  High score: {self.high_score} ", align="center",font=('courier', 13, 'normal'))

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update_score()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.color("white")
    #     self.write( "game over bruh failed 😎😎 ",align="center", font=('courier', 25, 'normal'))




    def score_mark(self):
        self.score+=1
        # self.clear()
        self.update_score()





        # turtle.write((0, 0), True)
