"""
Entry widget (TTK)

* The purpose of an Entry widget is to allow the user to enter or edit a single
  line of text. This is the ttk version of Entry from TKInter
* Syntax:
  * ttk.Entry(parent, option, ...)
* Reference:
  * https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html
"""
import tkinter as tk
from tkinter import ttk


###############################################################################
# Parameters
###############################################################################


# keys()
# * The keys method shows all parameters for the widget creation
window = tk.Tk()
window.withdraw()
keys = ttk.Entry(master=window).keys()
[print(k) for k in keys]
window.destroy()
"""
exportselection
font
invalidcommand
justify
show
state
textvariable
validate
validatecommand
width
xscrollcommand
foreground
background
takefocus
cursor
style
class
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
variable = tk.StringVar(master=window)
variable.set('Hello World!')
widget = ttk.Entry(
    master=window,
    textvariable=variable
)


# Set the position of the widget
# * The widget will be automatically adjusted
widget.pack()


# Main loop
# * Start the application
window.mainloop()
