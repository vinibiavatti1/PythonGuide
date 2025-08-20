"""
Place

* The place geometry manager is the simplest and most direct way to manage
  widget layout.
* It allows you to position widgets at specific coordinates using a rigid,
  absolute positioning system.
* It is useful for simple layouts, but can be difficult to manage when
  resizing windows.

* The available packing options include:
###############################################################################
Parameter    Description                                        Default
###############################################################################
x, y                The absolute x and y coordinates            0
relx, rely          The relative x and y coordinates (0.0-1.0)  0.0
width, height       The absolute width and height in pixels     widget's size
relwidth, relheight The relative width and height (0.0-1.0)     0.0
anchor              The point of the widget to be anchored      NW
bordermode          The mode for handling the widget's border   INSIDE
###############################################################################

* Syntax:
  * x.place(options)
"""


###############################################################################
# Import
###############################################################################


# Import
# * We will import tkinter to be used on the examples below.
import tkinter as tk


###############################################################################
# Absolute Positioning
###############################################################################


# Absolute Positioning
# * Widgets are placed at a fixed pixel coordinate relative to the parent.
# * The x and y options are used to set the position.
root = tk.Tk()
root.geometry("400x300")
b1 = tk.Button(master=root, text="Absolute at (50, 50)")
b2 = tk.Button(master=root, text="Absolute at (150, 100)")
b1.place(x=50, y=50)
b2.place(x=150, y=100)
root.mainloop()


###############################################################################
# Relative Positioning
###############################################################################


# Relative Positioning
# * Widgets are placed relative to the parent's size (0.0 to 1.0).
# * The relx, rely, relwidth, and relheight options are used.
root = tk.Tk()
root.geometry("400x300")
b1 = tk.Button(master=root, text="Relative Position")
b2 = tk.Button(master=root, text="Relative Size")
b1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
b2.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)
root.mainloop()
