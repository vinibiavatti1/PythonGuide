"""
Checkbutton widget (TTK)

* This widget is the ttk version of Checkbutton from TK
* Syntax:
  * ttk.Checkbutton(master, option, ...)
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
keys = ttk.Checkbutton(master=window).keys()
[print(k) for k in keys]
window.destroy()
"""
variable
onvalue
offvalue
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
widget = ttk.Checkbutton(
    master=window,
    text='Check it'
)


# Set the position of the widget
# * The widget will be automatically adjusted
widget.pack()


# Main loop
# * Start the application
window.mainloop()
