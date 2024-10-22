from sense_hat import SenseHat
import time, datetime

hat = SenseHat()

year_color = (0, 255, 0)
month_color = (0, 0, 255)
day_color = (255, 0, 0)
hour_color = (0, 255, 0)
minute_color = (0, 0, 255)
second_color = (255, 0, 0)
hundredths_color = (127, 127, 0)
off = (0, 0, 0)
show_clock = True
special_display_active = False  # To track if we are in a special display mode

hat.clear()

# Function to display a binary number on a specific row
def display_binary(value, row, color):
    binary_str = "{0:08b}".format(value)  # 8-bit binary format
    for x in range(0, 8):
        if binary_str[x] == '1':
            hat.set_pixel(x, row, color)
        else:
            hat.set_pixel(x, row, off)

# Function to handle joystick events for rotating the display or special actions
def handle_joystick(event):
    global show_clock, special_display_active  # Access global variables
    if event.action == 'pressed':
        if event.direction == 'up':
            hat.set_rotation(0)  # 0 degrees
        elif event.direction == 'down':
            hat.set_rotation(90)  # 90 degrees
        elif event.direction == 'left':
            hat.set_rotation(180)  # 180 degrees
        elif event.direction == 'right':
            hat.set_rotation(270)  # 270 degrees
        elif event.direction == 'middle':
            if special_display_active:
                # If special display is active, return to clock immediately
                special_display_active = False
                show_clock = True
                hat.clear()
            else:
                # Activate special display based on current rotation
                rotation = hat.rotation
                special_display_active = True
                show_clock = False  # Stop showing the clock while displaying special info
                if rotation == 0:
                    show_temperature()
                elif rotation == 180:
                    show_humidity()
                elif rotation == 270:
                    show_danish_flag()

# Function to display temperature on the LED matrix
def show_temperature():
    hat.clear()
    temperature = round(hat.get_temperature(), 1)  # Get the temperature
    hat.show_message(f"{temperature}C", scroll_speed=0.05, text_colour=[0, 0, 255])

# Function to display humidity on the LED matrix
def show_humidity():
    hat.clear()
    hat.set_rotation(0)
    humidity = round(hat.get_humidity(), 1)  # Get the humidity
    hat.show_message(f"{humidity}%", scroll_speed=0.05, text_colour=[0, 255, 0])

# Function to display the Danish flag on the LED matrix
def show_danish_flag():
    hat.clear()
    danish_flag = [
        [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 0, 0], [255, 0, 0],
        [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 0, 0], [255, 0, 0],
        [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255],
        [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255],
        [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 0, 0], [255, 0, 0],
        [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 0, 0], [255, 0, 0],
        [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 0, 0], [255, 0, 0],
        [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 0, 0], [255, 0, 0]
    ]
    hat.set_pixels(danish_flag)
    time.sleep(2)  # Show the flag for 2 seconds before resuming the clock

# Register the joystick event handler
hat.stick.direction_any = handle_joystick

# Main loop to display the time in binary
while True:
    if show_clock:
        hat.clear()  # Clear the display to avoid overlap with old pixels
        t = datetime.datetime.now()
        display_binary(t.year % 100, 0, year_color)   # Year (last 2 digits)
        display_binary(t.month, 1, month_color)       # Month
        display_binary(t.day, 2, day_color)           # Day
        display_binary(t.hour, 3, hour_color)         # Hour
        display_binary(t.minute, 4, minute_color)     # Minute
        display_binary(t.second, 5, second_color)     # Second
        display_binary(t.microsecond // 10000, 6, hundredths_color)  # Hundredths of a second
        time.sleep(0.1)  # Update every 0.1 seconds
