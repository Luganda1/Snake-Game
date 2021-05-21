from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 20, "normal")




class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_num = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.writing()

    def writing(self):
        self.clear()
        self.write(f"Score : {self.score_num}  High score : {self.high_score}", align=ALIGN, font=FONT)

    def  reset(self):
        if self.score_num > self.high_score:
            self.high_score = self.score_num
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.score_num = 0
        self.writing()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score_num += 1
        self.writing()

    def start_over(self):
        self.goto(0, 0)

