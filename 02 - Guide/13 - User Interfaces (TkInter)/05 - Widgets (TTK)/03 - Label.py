"""
Label (TTK)

* This is the TTK (Themed Tkinter) version of the Label widget.
* It provides a more modern look and feel compared to the classic Tkinter
  version.
* The Label widget is used to display text or images in a window.
* It can be customized with various options such as font, color, and size.
"""


###############################################################################
# Import
###############################################################################


# Import
# * We will import tkinter to be used on the examples below.
import tkinter as tk
import tkinter.ttk as ttk


###############################################################################
# Example
###############################################################################


# Example
# * The example below creates a simple GUI application with the widget.
root = tk.Tk()
label = ttk.Label(
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
label = ttk.Label()
[print(k) for k in label.keys()]
"""
background
foreground
font
borderwidth
relief
anchor
justify
wraplength
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
