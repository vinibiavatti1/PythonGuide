"""
Menu

* The menu widget is a standard Tkinter widget used to create menus in a GUI
  application.
* You can add various types of menu items such as commands, checkbuttons, and
  radiobuttons.
* The menu can be displayed as a dropdown menu or as a context menu.
* The menu can be customized using various options such as background color,
  foreground color, font, and more.
"""


###############################################################################
# Import
###############################################################################


# Import
# * We will import tkinter to be used on the examples below.
import tkinter as tk


###############################################################################
# Example
###############################################################################


# Example
# * The example below creates a simple GUI application with the widget.
# * Note that to add the menu to the main window, you must configure the window
#   to use the menu.
root = tk.Tk()
menu = tk.Menu(
    master=root,
)
file_menu = tk.Menu(
    master=menu,
    tearoff=0
)
file_menu.add_command(label='New', command=lambda: print('New'))
file_menu.add_command(label='Open', command=lambda: print('Open'))
file_menu.add_separator()
file_menu.add_checkbutton(label='Auto Save')
menu.add_cascade(label='File', menu=file_menu)
root.config(menu=menu)
root.mainloop()


###############################################################################
# Parameters & Methods
###############################################################################


# Keys
# * The `keys` method shows all parameters for the widget creation.
menu = tk.Menu()
[print(k) for k in menu.keys()]
"""
activebackground
activeborderwidth
activeforeground
background
bd
bg
borderwidth
cursor
disabledforeground
fg
font
foreground
postcommand
relief
selectcolor
takefocus
tearoff
tearoffcommand
title
type
"""


# Methods
# * The common methods for the widget are:
"""
add(kind, coption, ...)
add_cascade(coption, ...)
add_checkbutton(coption, ...)
add_command(coption, ...)
add_radiobutton(coption, ...)
add_separator()
delete(index1, index2=None)
entrycget(index, coption)
entryconfigure(index, coption, ...)
index(i)
insert_cascade(index, coption, ...)
insert_checkbutton(index, coption, ...)
insert_command(index, coption, ...)
insert_radiobutton(index, coption, ...)
insert_separator(index)
invoke(index)
post(x, y)
type(index)
yposition(n)
"""
