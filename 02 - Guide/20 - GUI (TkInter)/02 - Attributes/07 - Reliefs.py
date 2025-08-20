"""
Reliefs

* Reliefs are used to create a 3D effect on the widget's border.
* The available relief styles are predefined constants in the tkinter module.
* The relief styles are:
  * tk.FLAT
  * tk.RAISED
  * tk.SUNKEN
  * tk.GROOVE
  * tk.RIDGE
"""
###############################################################################
# Reliefs
###############################################################################


# Import
# * We will import tkinter to be used on the examples below.
import tkinter as tk


# Root Window
# * We will create a root window to demonstrate.
window = tk.Tk()
tk.Button(master=window, text='FLAT', relief=tk.FLAT).pack(fill=tk.X)
tk.Button(master=window, text='RAISED', relief=tk.RAISED).pack(fill=tk.X)
tk.Button(master=window, text='SUNKEN', relief=tk.SUNKEN).pack(fill=tk.X)
tk.Button(master=window, text='GROOVE', relief=tk.GROOVE).pack(fill=tk.X)
tk.Button(master=window, text='RIDGE', relief=tk.RIDGE).pack(fill=tk.X)
window.mainloop()
