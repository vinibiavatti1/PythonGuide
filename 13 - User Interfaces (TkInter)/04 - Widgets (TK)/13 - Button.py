"""
Button

* The Button widget is a standard Tkinter widget used to create clickable
  buttons in a GUI application.
* You can attach a function or a method to a button which is called
  automatically when you click the button.
* The Button widget can display text or images that convey the purpose of the
  button.
* The button can be customized using various options such as background color,
  foreground color, font, and more.
* The button can also be made to look like a link by using the `relief` option
  and setting it to `flat`.
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
button = tk.Button(
    master=root,
    text='Click me',
    command=lambda: print('Hello World!')
)
button.pack(padx=20, pady=20)
root.mainloop()
# Hello World!


###############################################################################
# Parameters & Methods
###############################################################################


# Keys
# * The `keys` method shows all parameters for the widget creation.
button = tk.Button()
[print(k) for k in button.keys()]
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


# Methods
# * The common methods for the widget are:
"""
flash()
invoke()
"""
