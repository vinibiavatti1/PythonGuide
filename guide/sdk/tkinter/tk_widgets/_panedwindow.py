"""
PanedWindow widget

* The purpose of the PanedWindow widget is to give the application's user some
  control over how space is divided up within the application
* A PanedWindow is somewhat like a Frame: it is a container for child widgets.
  Each PanedWindow widget contains a horizontal or vertical stack of child
  widgets. Using the mouse, the user can drag the boundaries between the child
  widgets back and forth
  * You may choose to display handles within the widget. A handle is a small
    square that the user can drag with the mouse
  * You may choose to make sashes visible. A sash is a bar placed between the
    child widgets
  * A pane is the area occupied by one child widget
* Syntax:
  * tk.PanedWindow(parent, option, ...)
* Reference:
  * https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html
"""
import tkinter as tk


###############################################################################
# Parameters
###############################################################################


# keys()
# * The keys method shows all parameters for the widget creation
window = tk.Tk()
window.withdraw()
keys = tk.PanedWindow(master=window).keys()
[print(k) for k in keys]
window.destroy()
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


###############################################################################
# Methods
###############################################################################


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


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
widget = tk.PanedWindow(
    master=window
)
left = tk.Label(master=widget, text='Left')
right = tk.Label(master=widget, text='Right')
widget.add(left)
widget.add(right)


# Set the position of the widget
# * The widget will be automatically adjusted
widget.pack()


# Main loop
# * Start the application
window.mainloop()
