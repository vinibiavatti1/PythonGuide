"""
Anchors

* Anchors are used to specify the position of a widget within its parent
  container.
* The available anchors are predefined constants in the tkinter module.

* The available anchors are:
  * tk.N
  * tk.NE
  * tk.E
  * tk.SE
  * tk.S
  * tk.SW
  * tk.W
  * tk.NW
  * tk.CENTER

* The representation below shows the position of each anchor point:
###################
# NW     N     NE #
#                 #
# W    CENTER   E #
#                 #
# SW     S     SE #
###################
"""


###############################################################################
# Anchors
###############################################################################


# Import
# * We will import tkinter to be used on the examples below.
import tkinter as tk


# Root Window
# * We will create a root window to demonstrate.
root = tk.Tk()
tk.Button(master=root, text='N', height=3, anchor=tk.N).pack(fill=tk.X)
tk.Button(master=root, text='NE', height=3, anchor=tk.NE).pack(fill=tk.X)
tk.Button(master=root, text='E', height=3, anchor=tk.E).pack(fill=tk.X)
tk.Button(master=root, text='SE', height=3, anchor=tk.SE).pack(fill=tk.X)
tk.Button(master=root, text='S', height=3, anchor=tk.S).pack(fill=tk.X)
tk.Button(master=root, text='SW', height=3, anchor=tk.SW).pack(fill=tk.X)
tk.Button(master=root, text='W', height=3, anchor=tk.W).pack(fill=tk.X)
tk.Button(master=root, text='NW', height=3, anchor=tk.NW).pack(fill=tk.X)
tk.Button(master=root, text='CENTER', height=3, anchor=tk.CENTER).pack(fill=tk.X)
root.mainloop()
