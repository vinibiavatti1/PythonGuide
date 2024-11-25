"""
Reliefs

* The relief style of a widget refers to certain simulated 3D effects around
  the outside of the widget. Here is a screenshot of a row of buttons
  exhibiting all the possible relief styles
"""
import tkinter as tk


###############################################################################
# Reliefs
###############################################################################


# Reliefs
# * The relief styles are:
"""
FLAT
RAISED
SUNKEN
GROOVE
RIDGE
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
b1 = tk.Button(master=window, text='FLAT', relief=tk.FLAT)
b2 = tk.Button(master=window, text='RAISED', relief=tk.RAISED)
b3 = tk.Button(master=window, text='SUNKEN', relief=tk.SUNKEN)
b4 = tk.Button(master=window, text='GROOVE', relief=tk.GROOVE)
b5 = tk.Button(master=window, text='RIDGE', relief=tk.RIDGE)


# Set the position of the widget
# * The widget will be automatically adjusted
b1.pack(fill=tk.X)
b2.pack(fill=tk.X)
b3.pack(fill=tk.X)
b4.pack(fill=tk.X)
b5.pack(fill=tk.X)


# Main loop
# * Start the application
window.mainloop()
