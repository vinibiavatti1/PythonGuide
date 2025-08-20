"""
LabelFrame widget (TTK)

* This is the ttk version of the basic Tkinter widget
* Syntax:
  * ttk.LabelFrame(parent, option, ...)
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
keys = ttk.LabelFrame(master=window).keys()
[print(k) for k in keys]
window.destroy()
"""
labelanchor
text
underline
labelwidget
borderwidth
padding
relief
width
height
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
widget = ttk.LabelFrame(
    master=window,
    text='Title'
)
label = ttk.Label(
    master=widget,
    text='Inside'
)
label.pack()


# Set the position of the widget
# * The widget will be automatically adjusted
widget.pack()


# Main loop
# * Start the application
window.mainloop()
