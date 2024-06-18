from turtle import Turtle

FONT = ('Ariel', 20, "italic")
ALIGNMENT = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open('highscore', mode='r') as file:
            self.highscore = file.read()
            self.highscore = int(self.highscore)
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.color('white')
        self.text_score()

    def text_score(self):
        self.write(f'Score: {self.score}    High Score: {self.highscore}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        with open('highscore', mode='w') as file:
            file.write(f'{self.highscore}')
        self.write(f'''Game Over
        
   Score: {self.score}''', align=ALIGNMENT, font=('Ariel', 40, "bold"))

    def add_score(self):
        self.score += 1
        self.clear()
        if self.score > self.highscore:
            self.highscore = self.score

        self.text_score()
