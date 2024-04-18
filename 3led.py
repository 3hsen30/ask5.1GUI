import RPi.GPIO as GPIO
import tkinter as tk
#Ehsen Tahir
# GPIO pins for LEDs
WHITE_PIN = 17  
GREEN_PIN = 18
BLUE_PIN = 27

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(WHITE_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

# Function to turn off all LEDs
def turn_off_all():
    GPIO.output(WHITE_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.LOW)
    GPIO.output(BLUE_PIN, GPIO.LOW)

# Function to turn on a specific LED
def turn_on_led(led_pin):
    turn_off_all()
    GPIO.output(led_pin, GPIO.HIGH)

# Function to handle radio button click
def handle_radio_button(led_pin):
    turn_on_led(led_pin)

# Create GUI
root = tk.Tk()
root.title("LED Controller")

# Radio buttons
white_radio = tk.Radiobutton(root, text="White LED", command=lambda: handle_radio_button(WHITE_PIN))
white_radio.pack()

green_radio = tk.Radiobutton(root, text="Green LED", command=lambda: handle_radio_button(GREEN_PIN))
green_radio.pack()

blue_radio = tk.Radiobutton(root, text="Blue LED", command=lambda: handle_radio_button(BLUE_PIN))
blue_radio.pack()

# Exit button
exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack()

# Run the GUI
root.mainloop()

# Cleanup GPIO
GPIO.cleanup()
