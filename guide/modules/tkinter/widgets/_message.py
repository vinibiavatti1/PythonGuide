"""
Message widget

* This widget is similar to the Label widget but it is intended for displaying
  messages over multiple lines
* Syntax:
  * tk.Message(parent, option, ...)
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
keys = tk.Message(master=window).keys()
[print(k) for k in keys]
window.destroy()
"""
anchor
aspect
background
bd
bg
borderwidth
cursor
fg
font
foreground
highlightbackground
highlightcolor
highlightthickness
justify
padx
pady
relief
takefocus
text
textvariable
width
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
widget = tk.Message(
    master=window,
    text='Hello World\nThis is a message widget'
)


# Set the position of the widget
# * The widget will be automatically adjusted
widget.pack()


# Main loop
# * Start the application
window.mainloop()
