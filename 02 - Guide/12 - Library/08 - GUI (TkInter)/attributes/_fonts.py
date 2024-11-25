"""
Fonts

* There may be up to two ways to specify type style:
  * by simple tuple fonts
  * by Font objects
"""
import tkinter as tk
from tkinter import font as tkfont


###############################################################################
# Simple tuple fonts
###############################################################################


# Set font by tuple
# * Syntax: (name, size, styles)
font = ('Helvetica', 16, 'bold italic')


###############################################################################
# Font objects
###############################################################################


# Set font by tuple
# * Syntax: (name, size, styles)
window = tk.Tk()
font = tkfont.Font(family='Helvetica', size=16, weight='bold')
window.destroy()


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created using the font definitions
font1 = ('Helvetica', 16, 'bold italic')
font2 = tkfont.Font(family='Times', size=16, weight='bold')
b1 = tk.Button(master=window, text='Helvetica', font=font1)
b2 = tk.Button(master=window, text='Times', font=font2)


# Set the position of the widget
# * The widget will be automatically adjusted
b1.pack(fill=tk.X)
b2.pack(fill=tk.X)


# Main loop
# * Start the application
window.mainloop()
