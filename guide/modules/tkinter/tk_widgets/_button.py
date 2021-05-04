"""
Button widget

* The Button widget is used to add buttons in a Python application
* These buttons can display text or images that convey the purpose of the
  buttons
* You can attach a function or a method to a button which is called
  automatically when you click the button
* Syntax:
  * tk.Button(master, option=value, ...)
* Reference:
  * https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html
"""
import tkinter as tk
from tkinter import messagebox


###############################################################################
# Parameters
###############################################################################


# keys()
# * The keys method shows all parameters for the widget creation
window = tk.Tk()
window.withdraw()
keys = tk.Button(master=window).keys()
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
command
compound
cursor
default
disabledforeground
fg
font
foreground
height
highlightbackground
highlightcolor
highlightthickness
image
justify
overrelief
padx
pady
relief
repeatdelay
repeatinterval
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
flash()
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
widget = tk.Button(
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
