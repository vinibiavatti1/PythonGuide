"""
List Box

* The list box widget is used to display a set of options to the user.
* It allows the user to select one or more options from the list.
* The selected options can be retrieved and processed by the application.
* The state of the Listbox can be controlled using a variable.
* In other libraries, it is often referred to as a list view or selection list.
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
options = tk.StringVar(value=['Option 1', 'Option 2', 'Option 3'])
listbox = tk.Listbox(
    master=root,
    listvariable=options
)
listbox.select_set(0)
listbox.pack(padx=20, pady=20)
root.mainloop()


###############################################################################
# Parameters & Methods
###############################################################################


# Keys
# * The `keys` method shows all parameters for the widget creation.
listbox = tk.Listbox()
[print(k) for k in listbox.keys()]
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
