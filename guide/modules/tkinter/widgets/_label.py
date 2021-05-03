"""
Label widget

* Label widgets can display one or more lines of text in the same style, or a
  bitmap or image
* Syntax:
  * tk.Label(parent, option, ...)
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
keys = tk.Label(master=window).keys()
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
compound
cursor
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
padx
pady
relief
state
takefocus
text
textvariable
underline
width
wraplength
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
widget = tk.Label(
    master=window,
    text='Hello world!'
)


# Set the position of the widget
# * The widget will be automatically adjusted
widget.pack()


# Main loop
# * Start the application
window.mainloop()
