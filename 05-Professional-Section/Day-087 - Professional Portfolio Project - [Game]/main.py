import turtle

# Set up the game window
win = turtle.Screen()
win.title("Breakout Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Bricks
bricks = []

def create_brick(x, y):
    brick = turtle.Turtle()
    brick.speed(0)
    brick.shape("square")
    brick.color("blue")
    brick.shapesize(stretch_wid=1, stretch_len=3)
    brick.penup()
    brick.goto(x, y)
    bricks.append(brick)

# Create a grid of bricks
for i in range(-350, 350, 80):
    for j in range(150, 250, 30):
        create_brick(i, j)

# Score
score = 0

# Display the score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Paddle movement
def paddle_right():
    x = paddle.xcor()
    if x < 350:
        x += 20
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    if x > -350:
        x -= 20
    paddle.setx(x)

# Keyboard binding
win.listen()
win.onkeypress(paddle_right, "Right")
win.onkeypress(paddle_left, "Left")

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1
        # Game over: reset the ball
        print("Game Over")
        break

    # Paddle collision
    if (ball.ycor() > -240 and ball.ycor() < -230) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.sety(-230)
        ball.dy *= -1

    # Brick collision
    for brick in bricks:
        if brick.distance(ball) < 50:
            ball.dy *= -1
            brick.goto(1000, 1000)  # Move the brick off the screen
            bricks.remove(brick)
            score += 10
            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # Win condition: all bricks are destroyed
    if not bricks:
        print("You Win!")
        break
