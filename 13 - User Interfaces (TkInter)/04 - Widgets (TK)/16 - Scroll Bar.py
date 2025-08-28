"""
Scroll Bar

* The scroll bar widget is a standard Tkinter widget used to add scrolling
  capability to other widgets.
* The scroll bar can be configured to scroll horizontally or vertically.
* It can be attached to various widgets such as text boxes, canvases, and
  frames.
* The scroll bar can be customized using various options such as background
  color, foreground color, and width.
* The scroll bar can be easily integrated with other widgets in a Tkinter
  application.
* The widgets that support scrolling with a scroll bar include:
  * Text boxes
  * Canvases
  * List boxes
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
frame = tk.Frame(
    master=root,
    relief=tk.GROOVE,
    borderwidth=1
)
text = tk.Text(
    master=frame,
    width=50,
    height=20,
    relief=tk.FLAT,
)
scrollbar = tk.Scrollbar(
    master=frame,
    orient=tk.VERTICAL,
    command=text.yview,
)
text.config(yscrollcommand=scrollbar.set)
frame.pack(padx=20, pady=20)
text.pack(side=tk.LEFT)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
root.mainloop()


###############################################################################
# Parameters & Methods
###############################################################################


# Keys
# * The `keys` method shows all parameters for the widget creation.
scrollbar = tk.Scrollbar()
[print(k) for k in scrollbar.keys()]
"""
activebackground
activerelief
background
bd
bg
borderwidth
command
cursor
elementborderwidth
highlightbackground
highlightcolor
highlightthickness
jump
orient
relief
repeatdelay
repeatinterval
takefocus
troughcolor
width
"""


# Methods
# * The common methods for the widget are:
"""
activate(element=None)
delta(dx, dy)
fraction(x, y)
get()
identify(x, y)
set(first, last)
"""
