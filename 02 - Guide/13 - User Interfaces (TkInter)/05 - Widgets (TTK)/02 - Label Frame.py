"""
Label Frame (TTK)

* This is the TTK (Themed Tkinter) version of the LabelFrame widget.
* It provides a more modern look and feel compared to the classic Tkinter
  version.
* The LabelFrame widget is used to create a container with a border and a
  title.
* It can be used to group related widgets together.
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
label_frame = ttk.Labelframe(
    master=root,
    text='Title',
    width=200,
    height=200,
)
label_frame.pack(padx=20, pady=20)
root.mainloop()


###############################################################################
# Parameters & Methods
###############################################################################


# Keys
# * The `keys` method shows all parameters for the widget creation.
label_frame = ttk.Labelframe()
[print(k) for k in label_frame.keys()]
"""
labelanchor
text
underline
labelwidget
borderwidth
padding
relief
width
height
takefocus
cursor
style
class
"""
