"""
Frame widget (TTK)

* Like the Tkinter Frame widget, the ttk.Frame widget is a rectangular
  container for other widgets
* Syntax:
  * ttk.Frame(parent, option, ...)
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
keys = ttk.Frame(master=window).keys()
[print(k) for k in keys]
window.destroy()
"""
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
widget = ttk.Frame(
    master=window
)


# Main loop
# * Start the application
window.mainloop()
