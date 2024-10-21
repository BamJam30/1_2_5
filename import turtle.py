import turtle
import time
import webbrowser  # Import webbrowser module

# Create screen
pg = turtle.Screen()
pg.title("E-Card")
pg.bgcolor("blue")  # Sets background to blue
pg.setup(width=1000, height=600)
pg.tracer(0)

# Make The Card
def create_card():
    card = turtle.Turtle()
    card.speed(0)
    card.shape("square")
    card.color("white")
    card.shapesize(stretch_wid=8, stretch_len=10)
    card.penup()
    card.goto(0, 0)
    return card

# Function to write text on the card
def write_text(text, x, y, font_size=20, color="black"):
    writer = turtle.Turtle()
    writer.penup()
    writer.goto(x, y)
    writer.color(color)
    writer.hideturtle()
    writer.write(text, align="center", font=("Arial", font_size, "bold"))
    return writer

# Function to add a logo
def add_logo(image_path):
    try:
        pg.register_shape(image_path)  # Register the image
        logo = turtle.Turtle()
        logo.penup()
        logo.goto(0, -80)
        logo.shape(image_path)  # Set the shape to the image
        logo.showturtle()
        return logo
    except Exception as e:
        print(f"Error loading image: {e}")

# Bounce animation for the card
def bounce_card(card):
    for _ in range(10):
        card.sety(card.ycor() + 10)
        pg.update()
        time.sleep(0.05)
        card.sety(card.ycor() - 10)
        pg.update()
        time.sleep(0.05)

# Animate text with a fade-in effect
def animate_text(text, x, y, font_size=20, color="black"):
    writer = turtle.Turtle()
    writer.penup()
    writer.goto(x, y)
    writer.hideturtle()
    
    # Fade-in effect
    for alpha in range(0, 256, 5):
        writer.color((alpha / 255, 0, 0))  # Fade to red
        writer.write(text, align="center", font=("Arial", font_size, "bold"))
        pg.update()
        time.sleep(0.02)
        writer.clear()  # Clear previous text

    writer.write(text, align="center", font=("Arial", font_size, "bold"))

# Interactive proposal reveal that opens an HTML page
def reveal_proposal(x, y):
    # Change this URL to the path of your HTML file
    webbrowser.open("file:///path/to/your/file.html")  # Adjust the path as necessary

# Main execution
card = create_card()
bounce_card(card)

# Animate text with fade-in effect
time.sleep(0.5)
animate_text("🎉 Homecoming Proposal 🎉", 0, 150, font_size=24, color="red")
time.sleep(0.5)
animate_text("Hey [Name]!", 0, 80, font_size=20)
time.sleep(0.5)
animate_text("Let's team up like our favorite Brawlers!", 0, 40, font_size=20)

# Add your logo image here
add_logo("stardrop_pop.gif")  # Ensure this path is correct
time.sleep(0.5)

# Draw footer
write_text("💥 Brawl Stars Forever! 💥", 0, -200, font_size=18)

# Make the proposal clickable
pg.onclick(reveal_proposal)

pg.mainloop()
