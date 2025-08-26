"""
Menu Button

* The menubutton widget is a standard Tkinter widget used to create a button
  that displays a menu when clicked.
* It can be used to create dropdown menus or context menus.
* The menubutton can be customized using various options such as background
  color, foreground color, font, and more.
* The menu can contain various types of menu items such as commands,
  checkbuttons, and radiobuttons.
* The menubutton can be easily integrated with other widgets in a Tkinter
  application.
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
root = tk.Tk()
menu_button = tk.Menubutton(
    master=root,
    text='Menu',
    relief=tk.RAISED
)
menu = tk.Menu(
    master=menu_button,
    tearoff=0
)
menu.add_command(label='New', command=lambda: print('New'))
menu.add_command(label='Open', command=lambda: print('Open'))
menu.add_separator()
menu.add_checkbutton(label='Auto Save')
menu_button.config(menu=menu)
menu_button.pack(padx=20, pady=20)
root.mainloop()


###############################################################################
# Parameters & Methods
###############################################################################


# Keys
# * The `keys` method shows all parameters for the widget creation.
menu_button = tk.Menubutton()
[print(k) for k in menu_button.keys()]
"""
activebackground
activeforeground
anchor
background
bd
bg
bitmap
borderwidth
cursor
direction
disabledforeground
fg
font
foreground
height
highlightbackground
highlightcolor
highlightthickness
image
indicatoron
justify
menu
padx
pady
relief
compound
state
takefocus
text
textvariable
underline
width
wraplength
"""
