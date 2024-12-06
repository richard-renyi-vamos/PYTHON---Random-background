import tkinter as tk
import random

def change_color():
    # Generate a random color in HEX format
    random_color = f"#{random.randint(0, 0xFFFFFF):06x}"
    # Change the background color of the window
    window.config(bg=random_color)
    # Call this function again after 1000 milliseconds (1 second)
    window.after(1000, change_color)

# Create the main tkinter window
window = tk.Tk()
window.title("Color Changer")

# Set the initial size of the window
window.geometry("800x600")

# Start changing colors
change_color()

# Run the tkinter event loop
window.mainloop()
