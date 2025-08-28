"""
Button (TTK)

* This is the TTK (Themed Tkinter) version of the Button widget.
* It provides a more modern look and feel compared to the classic Tkinter
  version.
* The Button widget is used to create a clickable button in a GUI application.
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
import tkinter.ttk as ttk


###############################################################################
# Example
###############################################################################


# Example
# * The example below creates a simple GUI application with the widget.
root = tk.Tk()
button = ttk.Button(
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
button = ttk.Button()
[print(k) for k in button.keys()]
"""
Hello World!
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


# Methods
# * The common methods for the widget are:
"""
flash()
invoke()
"""
