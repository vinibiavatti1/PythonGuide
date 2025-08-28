"""
Paned Window (TTK)

* This is the TTK (Themed Tkinter) version of the PanedWindow widget.
* It provides a more modern look and feel compared to the classic Tkinter
  version.
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
import tkinter.ttk as ttk


###############################################################################
# Example
###############################################################################


# Example
# * The example below creates a simple GUI application with the widget.
root = tk.Tk()
paned_window = ttk.Panedwindow(
    master=root,
    width=400,
    height=200,
    orient=tk.HORIZONTAL,
)
paned_window.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
left_button = ttk.Button(
    master=paned_window,
    text="Left Button",
)
right_button = ttk.Button(
    master=paned_window,
    text="Right Button",
)
paned_window.add(left_button)
paned_window.add(right_button)
root.mainloop()


###############################################################################
# Parameters & Methods
###############################################################################


# Keys
# * The `keys` method shows all parameters for the widget creation.
widget = ttk.Panedwindow()
[print(k) for k in widget.keys()]
"""
orient
width
height
takefocus
cursor
style
class
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
