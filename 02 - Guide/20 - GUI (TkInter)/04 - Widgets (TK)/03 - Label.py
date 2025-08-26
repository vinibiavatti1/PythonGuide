"""
Label

* The Label widget is used to display text or images in a window.
* It can be customized with various options such as font, color, and size.
"""


###############################################################################
# Import
###############################################################################


# Import
# * We will import tkinter to be used on the examples below.
import tkinter as tk


###############################################################################
# Example
###############################################################################


# Example
# * The example below creates a simple GUI application with the widget.
root = tk.Tk()
label = tk.Label(
    master=root,
    text='Hello world!'
)
label.pack(padx=20, pady=20)
root.mainloop()


###############################################################################
# Parameters & Methods
###############################################################################


# Keys
# * The `keys` method shows all parameters for the widget creation.
label = tk.Label()
[print(k) for k in label.keys()]
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
