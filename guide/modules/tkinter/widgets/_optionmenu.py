"""
OptionMenu widget

* The purpose of this widget is to offer a fixed set of choices to the user in
  a drop-down menu
* Syntax:
  * tk.OptionMenu(parent, variable, choice1, choice2, ...)
* Reference:
  * https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html
"""
import tkinter as tk


###############################################################################
# Parameters
###############################################################################


# keys()
# * The keys method shows all parameters for the widget creation
window = tk.Tk()
window.withdraw()
keys = tk.OptionMenu(window, None, None).keys()
[print(k) for k in keys]
window.destroy()
"""
activebackground
activeforeground
anchor
background
bd
bg
bitmap
borderwidth
cursor
direction
disabledforeground
fg
font
foreground
height
highlightbackground
highlightcolor
highlightthickness
image
indicatoron
justify
menu
padx
pady
relief
compound
state
takefocus
text
textvariable
underline
width
wraplength
"""


###############################################################################
# Methods
###############################################################################


# Methods
# * The common methods for the widget are:
"""
get()
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
options = ('Option 1', 'Option 2', 'Option 3')
variable = tk.StringVar()
variable.set('Select an option')
widget = tk.OptionMenu(
    window,
    variable,
    *options
)


# Set the position of the widget
# * The widget will be automatically adjusted
widget.pack()


# Main loop
# * Start the application
window.mainloop()
