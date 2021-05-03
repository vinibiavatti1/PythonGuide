"""
Menu widget

* “Drop-down” menus are a popular way to present the user with a number of
  choices, yet take up minimal space on the face of the application when the
  user is not making a choice
  * A menubutton is the part that always appears on the application
  * A menu is the list of choices that appears only after the user clicks on
    the menubutton
  * To select a choice, the user can drag the mouse from the menubutton down
    onto one of the choices. Alternatively, they can click and release the
    menubutton: the choices will appear and stay until the user clicks one of
    them
* Syntax:
  * tk.Menu(mb, option, ...)
* Reference:
  * https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html
"""
import tkinter as tk


###############################################################################
# Parameters
###############################################################################


# keys()
# * The keys method shows all parameters for the widget creation
window = tk.Tk()
window.withdraw()
keys = tk.Menu(master=window).keys()
[print(k) for k in keys]
window.destroy()
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


###############################################################################
# Methods
###############################################################################


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


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
widget = tk.Menu(master=window)
widget.add_command(label='Option 1')
widget.add_command(label='Option 2')


# Set the menu to the window
# * The menu must be set in the configuration of the window
window.config(menu=widget)


# Main loop
# * Start the application
window.mainloop()
