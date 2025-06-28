import turtle

nemo = turtle.Turtle()
button = turtle.Screen()
button.tracer(0)
nemo.speed(0)
nemo.hideturtle()

cell_position = [
    (-150, 150), (-50, 150), (50, 150),
    (-150, 50), (-50, 50), (50, 50),
    (-150, -50), (-50, -50), (50, -50)
]

board = [""] * 9
current_player = "X"

def draw_grid():
    for i in range(3):
        for j in range(3):
            x = -150 + j * 100
            y = 150 - i * 100
            nemo.penup()
            nemo.goto(x, y)
            nemo.pendown()
            for _ in range(4):
                nemo.forward(100)
                nemo.right(90)

draw_grid()

def draw_cross(x, y):
    nemo.penup()
    nemo.goto(x + 20, y - 20)
    nemo.setheading(315)
    nemo.pendown()
    nemo.forward(60)
    nemo.penup()
    nemo.goto(x + 80, y - 20)
    nemo.setheading(225)
    nemo.pendown()
    nemo.forward(60)
    nemo.penup()

def draw_zero(x, y):
    nemo.penup()
    nemo.goto(x + 50, y - 90)
    nemo.setheading(0)
    nemo.pendown()
    nemo.circle(30)
    nemo.penup()

def cell_click(x, y):
    global current_player
    for idx, (cx, cy) in enumerate(cell_position):
        if cx < x < cx + 100 and cy - 100 < y < cy:
            if board[idx] == "":
                board[idx] = current_player
                if current_player == "X":
                    draw_cross(cx, cy)
                    current_player = "O"
                else:
                    draw_zero(cx, cy)
                    current_player = "X"
                button.update()
            break

button.onclick(cell_click)
button.update()
turtle.mainloop()