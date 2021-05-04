"""
Menubutton widget (TTK)

* There is no ttk version of the Menu widget. Use the regular Tkinter widget
* Syntax:
  * ttk.Menubutton(parent, option, ...)
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
keys = ttk.Menubutton(master=window).keys()
[print(k) for k in keys]
window.destroy()
"""
menu
direction
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
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
widget = ttk.Menubutton(
    master=window,
    text='Click here'
)
menu = tk.Menu(
    master=widget
)
menu.add_checkbutton(label='Option 1')
menu.add_checkbutton(label='Option 2')


# Set the menu for the menubutton
# * The configure method can be used to change some property of the widget
widget.configure(menu=menu)


# Set the position of the widget
# * The widget will be automatically adjusted
widget.pack()


# Main loop
# * Start the application
window.mainloop()
