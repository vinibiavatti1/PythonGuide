"""
Paned Window

* The PanedWindow widget is a container widget that allows the user to arrange
  child widgets horizontally or vertically. It provides a way to create
  resizable panes within a window.
* The user can adjust the size of each pane by dragging the sash (the divider
  between panes) with the mouse.
* The PanedWindow widget can contain any number of child widgets, and each pane
  can be a different type of widget (e.g., frames, labels, text boxes).
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
paned_window = tk.PanedWindow(
    master=root,
    width=400,
    height=200,
    relief=tk.GROOVE,
    borderwidth=2,
)
paned_window.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
left_button = tk.Button(
    master=paned_window,
    text="Left Button",
    width=100,
    height=50
)
right_button = tk.Button(
    master=paned_window,
    text="Right Button",
    width=100,
    height=50
)
paned_window.add(left_button, minsize=100)
paned_window.add(right_button, minsize=100)
paned_window.sash_place(0, 200, 0)
root.mainloop()


###############################################################################
# Parameters & Methods
###############################################################################


# Keys
# * The `keys` method shows all parameters for the widget creation.
widget = tk.PanedWindow()
[print(k) for k in widget.keys()]
"""
background
bd
bg
borderwidth
cursor
handlepad
handlesize
height
opaqueresize
orient
proxybackground
proxyborderwidth
proxyrelief
relief
sashcursor
sashpad
sashrelief
sashwidth
showhandle
width
"""


# Methods
# * The common methods for the widget are:
"""
add(child[, option=value] ...)
forget(child)
identify(x, y)
panecget(child, option)
paneconfig(child, option=value, ...)
panes()
remove(child)
sash_coord(index)
sash_place(index, x, y)
"""
