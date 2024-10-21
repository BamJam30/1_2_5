import turtle
import tkinter


# Create screen
pg = turtle.Screen()
pg.title("Pong Game")
pg.bgcolor("black")  #Sets background to black
pg.setup(width=1000, height=600)
pg.bgpic("Galaxy.resize.gif") #Sets the image of galaxy as a background image
pg.tracer(0)  

initial_dx = 0.45 
initial_dy = -0.45

# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square") #Sets the shape of the left paddle as a square
left_pad.color("white") #Sets the color of the paddle as white
left_pad.shapesize(stretch_wid=6, stretch_len=1) #Makes the dimensions for the left paddle
left_pad.penup()
left_pad.goto(-400, 0) #Sets position for the left paddle

# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")  #Sets the shape of the right paddle as a square
right_pad.color("white")  #Sets the color of the paddle as white
right_pad.shapesize(stretch_wid=6, stretch_len=1) #Makes the dimensions for the right paddle
right_pad.penup()
right_pad.goto(400, 0) #Sets position for the right paddle

# Ball
hit_ball = turtle.Turtle()
hit_ball.speed(1)
hit_ball.shape("circle") # Sets shape of the ball as a circle
hit_ball.color("white") #Sets color of ball as white
hit_ball.penup()
hit_ball.goto(0, 0) # Sets position of the ball to the center of the screen
hit_ball.dx = 0.225 # Sets the change in the x value (Speed)
hit_ball.dy = -0.225 # Sets the change in the y value (Also Speed)

# score variables
left_score = 0 # Sets the score at the beginning of the game to 0 for left player
right_score = 0 # Sets the score at the beginning of the gam to 0 for right player

# scoreboard
scoreboard = turtle.Turtle() # Sets scoreboard as a turtle
scoreboard.speed(0)
scoreboard.color("white") # Makes the color of the scoreboard white
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260) # Sets position of the scoreboard
scoreboard.write("Left: 0  Right: 0", align="center", font=("Courier", 24, "normal")) # Writes score board for display, and the font

# Function to update the scoreboard
def update_scoreboard():
    scoreboard.clear()
    scoreboard.write(f"Left: {left_score}  Right: {right_score}", align="center", font=("Courier", 24, "normal"))# Changes display of the scoreboard, so the display changes to the current score

# Paddle movement flags
left_up = False
left_down = False
right_up = False
right_down = False

# Functions to set movement flags
def left_pad_up():
    global left_up
    left_up = True

def left_pad_down():
    global left_down
    left_down = True

def right_pad_up():
    global right_up
    right_up = True

def right_pad_down():
    global right_down
    right_down = True

# Functions to reset movement flags
def stop_left_up():
    global left_up
    left_up = False

def stop_left_down():
    global left_down
    left_down = False

def stop_right_up():
    global right_up
    right_up = False

def stop_right_down():
    global right_down
    right_down = False

# Keyboard bindings
pg.listen()
pg.onkeypress(left_pad_up, "w") # Sets the key w to move the paddles up
pg.onkeypress(left_pad_down, "s") # Sets the key s to move the paddles up
pg.onkeypress(right_pad_up, "Up") # Sets the arrow up to move the paddles up
pg.onkeypress(right_pad_down, "Down") # Sets the arrow down to move the paddles up
pg.onkeyrelease(stop_left_up, "w") # Sets the key w to move the paddles up
pg.onkeyrelease(stop_left_down, "s") # Sets the key s to move the paddles up
pg.onkeyrelease(stop_right_up, "Up") # Sets the arrow up to move the paddles up
pg.onkeyrelease(stop_right_down, "Down") # Sets the arrow down to move the paddles up

# Main game loop
while True:
    pg.update()  # Update the screen

    # Move the ball
    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    # Move paddles based on flags
    if left_up and left_pad.ycor() < 250:
        left_pad.sety(left_pad.ycor() + 0.4) #How fast the paddle on the left goes up
    if left_down and left_pad.ycor() > -240:
        left_pad.sety(left_pad.ycor() - 0.4) #How fast the paddle on the left goes down
    if right_up and right_pad.ycor() < 250:
        right_pad.sety(right_pad.ycor() + 0.4) #How fast the paddle on the right goes up
    if right_down and right_pad.ycor() > -240:
        right_pad.sety(right_pad.ycor() - 0.4) #How fast the paddle on the right goes down

    # Border checking
    if hit_ball.ycor() > 290: #Sets an if statement when ball passes a certain point, for response
        hit_ball.sety(290)
        hit_ball.dy *= -1  # Bounce back

    if hit_ball.ycor() < -290: #Sets an if statement when ball passes a certain point, for response
        hit_ball.sety(-290)
        hit_ball.dy *= -1  # Bounce back

    if hit_ball.xcor() > 420:  #Sets an if statement when ball passes a certain point, for response
        hit_ball.goto(0, 0)
        left_score += 1  # Left player scores
        hit_ball.dx *= initial_dx
        hit_ball.dy *= initial_dy
        update_scoreboard()

    if hit_ball.xcor() < -420: #Sets an if statement when ball passes a certain point, for response
        hit_ball.goto(0, 0)
        right_score += 1  # Right player scores
        hit_ball.dx *= -initial_dx
        hit_ball.dy *= -initial_dy
        update_scoreboard()

    # Define speed increase factor
    speed_increase_factor = 1.1  # Multiplier for how fast the ball speeds up after each hit

    #Paddle collision
    if (340 < hit_ball.xcor() < 400) and (right_pad.ycor() - 50 < hit_ball.ycor() < right_pad.ycor() + 50):
        hit_ball.setx(340)
        hit_ball.dx *= -speed_increase_factor  # Bounce back and increase speed
        hit_ball.dy *= speed_increase_factor  # Also increase y speed 

    if (-400 < hit_ball.xcor() < -340) and (left_pad.ycor() - 50 < hit_ball.ycor() < left_pad.ycor() + 50):
        hit_ball.setx(-340)
        hit_ball.dx *= -speed_increase_factor  # Bounce back and increase speed
        hit_ball.dy *= speed_increase_factor  # Also increase y speed

pg.mainloop()





