from sense_hat import SenseHat
import time
import random

# Initialize Sense HAT
sense = SenseHat()

# Function to generate random RGB color
def random_color():
    return [random.randint(0, 255) for _ in range(3)]

# Infinite loop to repeat "Hello, World!" with different colors
while True:
    text_color = random_color()           # Generate a random text color
    background_color = random_color()     # Generate a random background color

    # Ensure the text and background colors are not too similar (for readability)
    while text_color == background_color:
        background_color = random_color()

    sense.show_message("Hello, World!", text_colour=text_color, back_colour=background_color, scroll_speed=0.1)

    # Optional: short delay between repeats
    time.sleep(1)

# Clear the LED matrix (this won't be reached unless you break the loop)
sense.clear()
