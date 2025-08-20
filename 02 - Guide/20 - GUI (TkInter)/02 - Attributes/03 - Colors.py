"""
Colors

* The colors in Tkinter can be specified using either string names or
  hexadecimal values.
* Any hexadecimal color can be specified using the format "#RRGGBB".
* It can be set by setting the "bg" and "fg" attributes of a widget.
* The available string colors are:
  * white
  * black
  * red
  * green
  * blue
  * cyan
  * yellow
  * magenta
"""


###############################################################################
# Colors
###############################################################################


# Import
# * We will import tkinter to be used on the examples below.
import tkinter as tk


# Root Window
# * We will create a root window to demonstrate.
window = tk.Tk()
tk.Button(master=window, text='White', bg='white').pack(fill=tk.X)
tk.Button(master=window, text='Black', bg='black', fg='white').pack(fill=tk.X)
tk.Button(master=window, text='Red', bg='red').pack(fill=tk.X)
tk.Button(master=window, text='Green', bg='green').pack(fill=tk.X)
tk.Button(master=window, text='Blue', bg='blue').pack(fill=tk.X)
tk.Button(master=window, text='Cyan', bg='cyan').pack(fill=tk.X)
tk.Button(master=window, text='Yellow', bg='yellow').pack(fill=tk.X)
tk.Button(master=window, text='Magenta', bg='magenta').pack(fill=tk.X)
tk.Button(master=window, text='Orange', bg='#FFA500').pack(fill=tk.X)
tk.Button(master=window, text='Grey', bg='#808080').pack(fill=tk.X)
window.mainloop()
