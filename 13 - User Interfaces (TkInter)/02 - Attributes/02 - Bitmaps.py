"""
Bitmaps

* Bitmaps are monochrome images used in GUI applications.
* They are often used to represent icons or simple graphics.
* The TkInter provides some predefined bitmap images.
* It can be displayed using the `bitmap` attribute of a widget.

* The available bitmaps are:
  * error
  * gray75
  * gray50
  * gray25
  * gray12
  * hourglass
  * info
  * questhead
  * question
  * warning
"""


###############################################################################
# Bitmaps
###############################################################################


# Import
# * We will import tkinter to be used on the examples below.
import tkinter as tk


# Root Window
# * We will create a root window to demonstrate.
window = tk.Tk()
tk.Button(master=window, bitmap='error').pack(fill=tk.X)
tk.Button(master=window, bitmap='gray75').pack(fill=tk.X)
tk.Button(master=window, bitmap='gray50').pack(fill=tk.X)
tk.Button(master=window, bitmap='gray25').pack(fill=tk.X)
tk.Button(master=window, bitmap='gray12').pack(fill=tk.X)
tk.Button(master=window, bitmap='hourglass').pack(fill=tk.X)
tk.Button(master=window, bitmap='info').pack(fill=tk.X)
tk.Button(master=window, bitmap='questhead').pack(fill=tk.X)
tk.Button(master=window, bitmap='question').pack(fill=tk.X)
tk.Button(master=window, bitmap='warning').pack(fill=tk.X)
window.mainloop()
