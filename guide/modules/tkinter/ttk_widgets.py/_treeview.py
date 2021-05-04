"""
Treeview (TTK)

* The purpose of the ttk.Treeview widget is to present a hierarchical structure
  so that the user can use mouse actions to reveal or hide any part of the
  structure
* Your Treeview widget will be structured with multiple columns. The first
  column, which we'll call the icon column, displays the icons that collapse or
  expand items. In the remaining columns, you may display whatever information
  you like
* The operations of the Treeview widget even allow you to use it as a tree
  editor. Your program can remove an entire subtree from its location in the
  main tree and then attach it later at an entirely different point
* Here is the general procedure for setting up a Treeview widget:
  * Create the widget with the ttk.Treeview constructor. Use the columns
    keyword argument to specify the number of columns to be displayed and to
    assign symbolic names to each column
  * Use the .column() and .heading() methods to set up column headings
    (if you want them) and configure column properties such as size and
    stretchability
  * Starting with the top-level entries, use the .insert() method to populate
    the tree. Each call to this method adds one item to the tree. Use the open
    keyword argument of this method to specify whether the item is initially
    expanded or collapsed
* Syntax:
  * ttk.Treeview(master, option=value, ...)
* Reference:
  * https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html
"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


###############################################################################
# Parameters
###############################################################################


# keys()
# * The keys method shows all parameters for the widget creation
window = tk.Tk()
window.withdraw()
keys = ttk.Treeview(master=window).keys()
[print(k) for k in keys]
window.destroy()
"""
columns
displaycolumns
show
selectmode
height
padding
xscrollcommand
yscrollcommand
takefocus
cursor
style
class
"""


###############################################################################
# Methods
###############################################################################


# Methods
# * The common methods for the widget are:
"""
bbox(item, column=None)
column(cid, option=None, **kw)
delete(*items)
detach(*items)
exists(iid)
focus([iid])
get_children([item])
heading(cid, option=None, **kw)
identify_column(x)
identify_element(x, y)
identify_region(x, y))
identify_row(y)
index(iid)
set_children(item, *newChildren)
insert(parent, index, iid=None, **kw)
item(iid[, option[, **kw]])
move(iid, parent, index)
next(iid)
parent(iid)
prev(iid)
see(iid)
selection_add(items)
selection_remove(items)
selection_set(items)
selection_toggle(items)
set(iid, column=None, value=None)
tag_bind(tagName, sequence=None, callback=None)
tag_configure(tagName, option=None, **kw)
tag_has(tagName[, iid])
xview(*args)
yview(*args)
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
widget = ttk.Treeview(
    master=window,
    columns=('KB')
)
widget.heading('#0', text='Files')
widget.heading('KB', text='Size')
widget.insert('', tk.END, 'Folder', text='Folder')
widget.insert('Folder', tk.END, 'File 1', text='File 1', values=('19 KB',))
widget.insert('Folder', tk.END, 'File 2', text='File 2', values=('2 MB',))
widget.insert('Folder', tk.END, 'File 3', text='File 3', values=('780 B',))


# Set the position of the widget
# * The widget will be automatically adjusted
widget.pack()


# Main loop
# * Start the application
window.mainloop()
