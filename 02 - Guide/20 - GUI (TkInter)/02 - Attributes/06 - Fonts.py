"""
Fonts

* Fonts are used to define the appearance of text in a GUI application.
* They can be specified by two main methods:
  * Font tuple (name, size, styles)
  * Using tkinter.font
"""


###############################################################################
# Fonts
###############################################################################


# Import
# * We will import tkinter to be used on the examples below.
# * We will also import the font module. Usually, the font module is imported
#   as tkfont
import tkinter as tk
import tkinter.font as tkfont


# Root Window
# * We will create a root window to demonstrate.
# * Note that we will use the tuple and font object methods to define fonts.
root = tk.Tk()
font1 = ('Helvetica', 16, 'bold italic')
font2 = tkfont.Font(family='Times', size=16, weight='bold')
tk.Button(master=root, text='Helvetica', font=font1).pack(fill=tk.X)
tk.Button(master=root, text='Times', font=font2).pack(fill=tk.X)
root.mainloop()
