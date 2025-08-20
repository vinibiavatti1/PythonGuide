"""
Pack

* The pack geometry manager is one of the simplest ways to manage widget layout
  in Tkinter.
* It is based on the concept of "packing" widgets into a parent container.
* The pack manager automatically arranges widgets in the specified order.

* The available packing options include:
###############################################################################
Parameter  Description                                               Default
###############################################################################
expand     Widget expands to fill any space                          False
fill       Determines whether widget fills any extra space           NONE
side       Determines which side of the parent widget packs against  TOP
###############################################################################

* Syntax:
  * x.pack(options)
"""


###############################################################################
# Import
###############################################################################


# Import
# * We will import tkinter to be used on the examples below.
import tkinter as tk


###############################################################################
# Expand
###############################################################################


# Expand
# * The expand option allows a widget to expand and fill any extra space in the
#   parent container.
# * By default, widgets do not expand to fill available space.
# * To enable expansion, set the expand option to True when packing the widget.
# * The example below shows two buttons with different expansion behaviors.
root = tk.Tk()
root.geometry("400x300")
b1 = tk.Button(master=root, text="Not expanded")
b2 = tk.Button(master=root, text="Expanded")
b1.pack(side=tk.TOP)
b2.pack(expand=True, fill=tk.BOTH)
root.mainloop()


###############################################################################
# Fill
###############################################################################


# Fill
# * The fill option determines whether a widget should fill any extra space
#   allocated to it by the packer.
# * The available fill options are:
#   * tk.NONE (default): The widget keeps its own minimal dimensions.
#   * tk.X: The widget fills the available horizontal space.
#   * tk.Y: The widget fills the available vertical space.
#   * tk.BOTH: The widget fills both horizontally and vertically.
root = tk.Tk()
root.geometry("400x300")
b1 = tk.Button(master=root, text="No Fill")
b2 = tk.Button(master=root, text="Fill X")
b3 = tk.Button(master=root, text="Fill Y")
b1.pack(expand=True)
b2.pack(expand=True, fill=tk.X)
b3.pack(expand=True, fill=tk.Y)
root.mainloop()


###############################################################################
# Side
###############################################################################


# Side
# * The side option determines which side of the parent widget the current
#   widget is to be packed against.
# * The available side options are:
#   * tk.TOP (default): The widget is packed at the top of the parent.
#   * tk.BOTTOM: The widget is packed at the bottom of the parent.
#   * tk.LEFT: The widget is packed at the left of the parent.
#   * tk.RIGHT: The widget is packed at the right of the parent.
root = tk.Tk()
root.geometry("400x300")
b1 = tk.Button(master=root, text="Side Top")
b2 = tk.Button(master=root, text="Side Left")
b3 = tk.Button(master=root, text="Side Right")
b4 = tk.Button(master=root, text="Side Bottom")
b1.pack(side=tk.TOP)
b2.pack(side=tk.LEFT)
b3.pack(side=tk.RIGHT)
b4.pack(side=tk.BOTTOM)
root.mainloop()
