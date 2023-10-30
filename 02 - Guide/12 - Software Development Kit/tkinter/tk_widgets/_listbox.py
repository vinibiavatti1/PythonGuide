"""
Listbox widget

* The purpose of a listbox widget is to display a set of lines of text.
  Generally they are intended to allow the user to select one or more items
  from a list. All the lines of text use the same font
* Syntax:
  * tk.Listbox(parent, option, ...)
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
keys = tk.Listbox(master=window).keys()
[print(k) for k in keys]
window.destroy()
"""
activestyle
background
bd
bg
borderwidth
cursor
disabledforeground
exportselection
fg
font
foreground
height
highlightbackground
highlightcolor
highlightthickness
justify
relief
selectbackground
selectborderwidth
selectforeground
selectmode
setgrid
state
takefocus
width
xscrollcommand
yscrollcommand
listvariable
"""


###############################################################################
# Methods
###############################################################################


# Methods
# * The common methods for the widget are:
"""
activate(index)
bbox(index)
curselection()
delete(first, last=None)
get(first, last=None)
index(i)
insert(index, *elements)
itemcget(index, option)
itemconfig(index, option=value, ...)
nearest(y)
scan_dragto(x, y)
scan_mark(x, y)
see(index)
selection_anchor(index)
selection_clear(first, last=None)
selection_includes(index)
selection_set(first, last=None)
size()
xview()
xview_moveto(fraction)
xview_scroll(number, what)
yview()
yview_moveto(fraction)
yview_scroll(number, what)
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
widget = tk.Listbox(
    master=window
)
widget.insert(1, 'Vini')
widget.insert(2, 'Ana')


# Set the position of the widget
# * The widget will be automatically adjusted
widget.pack()


# Main loop
# * Start the application
window.mainloop()
