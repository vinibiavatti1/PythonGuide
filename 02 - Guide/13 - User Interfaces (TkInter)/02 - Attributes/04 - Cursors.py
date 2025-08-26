"""
Cursors

* Tkinter supports a variety of mouse cursors that can be used in your
  applications.
* The exact appearance of each cursor may vary depending on the operating
  system.
* You can set the cursor for any widget using the `cursor` attribute.
* The available cursors are:
  * arrow
  * crosshair
  * fleur
  * hand2
  * left_ptr
  * right_ptr
  * plus
  * question_arrow
  * sb_h_double_arrow
  * sb_v_double_arrow
  * watch
  * tcross
  * xterm
"""


###############################################################################
# Cursors
###############################################################################


# Import
# * We will import tkinter to be used on the examples below.
import tkinter as tk


# Root Window
# * We will create a root window to demonstrate.
window = tk.Tk()
tk.Button(master=window, text='arrow', cursor='arrow').pack(fill=tk.X)
tk.Button(master=window, text='crosshair', cursor='crosshair').pack(fill=tk.X)
tk.Button(master=window, text='fleur', cursor='fleur').pack(fill=tk.X)
tk.Button(master=window, text='hand2', cursor='hand2').pack(fill=tk.X)
tk.Button(master=window, text='left_ptr', cursor='left_ptr').pack(fill=tk.X)
tk.Button(master=window, text='right_ptr', cursor='right_ptr').pack(fill=tk.X)
tk.Button(master=window, text='question_arrow', cursor='question_arrow').pack(fill=tk.X)
tk.Button(master=window, text='h_double', cursor='sb_h_double_arrow').pack(fill=tk.X)
tk.Button(master=window, text='v_double', cursor='sb_v_double_arrow').pack(fill=tk.X)
tk.Button(master=window, text='watch', cursor='watch').pack(fill=tk.X)
tk.Button(master=window, text='tcross', cursor='tcross').pack(fill=tk.X)
tk.Button(master=window, text='xterm', cursor='xterm').pack(fill=tk.X)
window.mainloop()
