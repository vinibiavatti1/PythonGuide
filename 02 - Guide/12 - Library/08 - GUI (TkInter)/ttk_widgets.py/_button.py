"""
Button widget (TTK)

* This widget is the ttk version of Tk Button
* Syntax:
  * ttk.Button(master, option=value, ...)
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
keys = ttk.Button(master=window).keys()
[print(k) for k in keys]
window.destroy()
"""
command
default
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


# Create the command function
# * This function will be executed when the button is clicked
def command(message):
    messagebox.showinfo('Information', message)


# Create the widget
# * The widget will be created and put inside the window
widget = ttk.Button(
    master=window,
    text='Click',
    command=lambda: command('Hello world!')
)


# Set the position of the widget
# * The widget will be automatically adjusted
widget.pack()


# Main loop
# * Start the application
window.mainloop()
