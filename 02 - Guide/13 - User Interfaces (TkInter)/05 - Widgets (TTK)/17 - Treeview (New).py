"""
Tree View (TTK)

* The Treeview widget (TTK) is used to display hierarchical data in a tree-like
  structure.
* It allows the user to expand and collapse items to reveal or hide their
  children.
* Each item in the tree can have its own set of attributes and can be
  associated with images or icons.
* The Treeview widget can be customized in terms of its appearance and
  behavior.
* It is useful for displaying complex data structures and improving the user
  experience.
* The Treeview widget is part of the TTK (Themed Tkinter) module, which
  provides a more modern look and feel for Tkinter applications.
* In other languages, similar tree structures are often referred to as
  "tree grids" or "hierarchical views."
* It is usually used to create table-like structures with rows and columns.
"""


###############################################################################
# Import
###############################################################################


# Import
# * We will import tkinter to be used on the examples below.
import tkinter as tk
import tkinter.ttk as ttk


###############################################################################
# Example
###############################################################################


# Example
# * The example below creates a simple GUI application with the widget.
root = tk.Tk()
tree = ttk.Treeview(
    master=root,
    columns=('Length', 'Size')
)
tree.heading('#0', text='Music')
tree.heading('#1', text='Length')
tree.heading('#2', text='Size')
tree.insert('', tk.END, 'A1', text='Artist 1')
tree.insert('A1', tk.END, text='Music 1', values=('3:18', '2.10 MB',))
tree.insert('A1', tk.END, text='Music 2', values=('2:45', '1.90 MB',))
tree.insert('A1', tk.END, text='Music 3', values=('4:12', '4.14 MB',))
tree.insert('', tk.END, 'A2', text='Artist 2')
tree.insert('A2', tk.END, text='Music 1', values=('5:01', '3.23 MB',))
tree.insert('A2', tk.END, text='Music 2', values=('2:59', '2.00 MB',))
tree.insert('A2', tk.END, text='Music 3', values=('3:09', '3.12 MB',))
tree.pack(padx=20, pady=20)


# Table Example
# * We can also use this widget to create a table-like structure with rows and
#   columns.
table = ttk.Treeview(
    root,
    columns=('Music', 'Length', 'Size'),
    show='headings'  # Show only headings
)
table.heading('#1', text='Music')
table.heading('#2', text='Length')
table.heading('#3', text='Size')
table.insert('', tk.END, values=('Music 1', '3:18', '2.10 MB',))
table.insert('', tk.END, values=('Music 2', '2:45', '1.90 MB',))
table.insert('', tk.END, values=('Music 3', '4:12', '4.14 MB',))
table.pack(padx=20, pady=20)
root.mainloop()


###############################################################################
# Parameters & Methods
###############################################################################


# Keys
# * The `keys` method shows all parameters for the widget creation.
tree = ttk.Treeview()
[print(k) for k in tree.keys()]
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
