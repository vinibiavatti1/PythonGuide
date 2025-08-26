"""
Label Frame

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


###############################################################################
# Example
###############################################################################


# Example
# * The example below creates a simple GUI application with the widget.
root = tk.Tk()
label_frame = tk.LabelFrame(
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
label_frame = tk.LabelFrame()
[print(k) for k in label_frame.keys()]
"""
bd
borderwidth
class
fg
font
foreground
labelanchor
labelwidget
relief
text
background
bg
colormap
container
cursor
height
highlightbackground
highlightcolor
highlightthickness
padx
pady
takefocus
visual
width
"""
