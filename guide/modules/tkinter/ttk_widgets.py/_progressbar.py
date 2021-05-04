"""
Progressbar widget (TTK)

* The purpose of this widget is to reassure the user that something is
  happening. It can operate in one of two modes
  * In determinate mode, the widget shows an indicator that moves from
    beginning to end under program control
  * In indeterminate mode, the widget is animated so the user will believe that
    something is in progress. In this mode, the indicator bounces back and
    forth between the ends of the widget
* Syntax:
  * ttk.Progressbar(master, option=value, ...)
* Reference:
  * https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html
"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


###############################################################################
# Parameters
###############################################################################


# keys()
# * The keys method shows all parameters for the widget creation
window = tk.Tk()
window.withdraw()
keys = ttk.Progressbar(master=window).keys()
[print(k) for k in keys]
window.destroy()
"""
orient
length
mode
maximum
variable
value
phase
takefocus
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
start([interval])
step([delta])
stop()
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
widget = ttk.Progressbar(
    master=window,
    mode='determinate'
)
widget.start()


# Set the position of the widget
# * The widget will be automatically adjusted
widget.pack()


# Main loop
# * Start the application
window.mainloop()
