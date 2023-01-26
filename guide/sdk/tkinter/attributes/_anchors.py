"""
Anchors

* Anchors are used to define where text is positioned relative to a reference
  point
"""
import tkinter as tk


###############################################################################
# Anchors
###############################################################################


# Anchors
# * There are constants in tkinter to represent the position by the points:
"""
###############################################################################
Point                   Description
###############################################################################
N                       North
NE                      North-East
E                       East
SE                      South-East
S                       South
SW                      South-West
W                       West
NW                      North-West
CENTER                  Center
###############################################################################
"""


# Representation
# * The positional representation for the points is:
"""
+-----------------+
| NW     N     NE |
|                 |
| W      C      E |
|                 |
| SW     S     SE |
+-----------------+
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
b1 = tk.Button(master=window, text='N', height=3, anchor=tk.N)
b2 = tk.Button(master=window, text='NE', height=3, anchor=tk.NE)
b3 = tk.Button(master=window, text='E', height=3, anchor=tk.E)
b4 = tk.Button(master=window, text='SE', height=3, anchor=tk.SE)
b5 = tk.Button(master=window, text='S', height=3, anchor=tk.S)
b6 = tk.Button(master=window, text='SW', height=3, anchor=tk.SW)
b7 = tk.Button(master=window, text='W', height=3, anchor=tk.W)
b8 = tk.Button(master=window, text='NW', height=3, anchor=tk.NW)
b9 = tk.Button(master=window, text='C', height=3, anchor=tk.CENTER)


# Set the position of the widget
# * The widget will be automatically adjusted
b1.pack(fill=tk.X)
b2.pack(fill=tk.X)
b3.pack(fill=tk.X)
b4.pack(fill=tk.X)
b5.pack(fill=tk.X)
b6.pack(fill=tk.X)
b7.pack(fill=tk.X)
b8.pack(fill=tk.X)
b9.pack(fill=tk.X)


# Main loop
# * Start the application
window.mainloop()
