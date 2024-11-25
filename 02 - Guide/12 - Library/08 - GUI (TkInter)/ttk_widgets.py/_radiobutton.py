"""
Radiobutton widget (TTK)

* This widget is the ttk version of Radiobutton widget from TK
* Syntax:
  * ttk.Radiobutton(parent, option, ...)
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
keys = ttk.Radiobutton(master=window).keys()
[print(k) for k in keys]
window.destroy()
"""
variable
value
command
takefocus
text
textvariable
underline
width
image
compound
padding
state
cursor
style
class
"""


###############################################################################
# Methods
###############################################################################


# Methods
# * The common methods for the widget are:
"""
invoke()
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
variable = tk.IntVar()
variable.set(1)
radio1 = ttk.Radiobutton(
    master=window,
    text='Option 1',
    variable=variable,
    value=1
)
radio2 = ttk.Radiobutton(
    master=window,
    text='Option 2',
    variable=variable,
    value=2
)
radio3 = ttk.Radiobutton(
    master=window,
    text='Option 3',
    variable=variable,
    value=3
)


# Set the position of the widget
# * The widget will be automatically adjusted
radio1.pack()
radio2.pack()
radio3.pack()


# Main loop
# * Start the application
window.mainloop()
