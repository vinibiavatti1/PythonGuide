"""
Message

* The Message widget is used to display text messages to the user.
* It is similar to the Label widget but is designed for displaying messages
  over multiple lines.
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
message = tk.Message(
    master=root,
    text='Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
)
message.pack(padx=20, pady=20)
root.mainloop()


###############################################################################
# Parameters & Methods
###############################################################################


# Keys
# * The `keys` method shows all parameters for the widget creation.
message = tk.Message()
[print(k) for k in message.keys()]
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
