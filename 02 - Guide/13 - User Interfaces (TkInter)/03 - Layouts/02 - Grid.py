"""
Grid

* The grid geometry manager is another way to manage widget layout in Tkinter.
* It organizes widgets in a table-like structure in the parent widget.
* Widgets can be placed in specific rows and columns.

* The available grid options include:
###############################################################################
Parameter  Description                                                Default
###############################################################################
column     The column to put the widget in                            0
row        The row to put the widget in                               0
columnspan How many columns the widget occupies                       1
rowspan    How many rows the widget occupies                          1
sticky     What to do if the cell is larger than the widget           center
padx       How many pixels to pad the widget horizontally             0
pady       How many pixels to pad the widget vertically               0
ipadx      How many pixels to pad the widget's interior horizontally  0
ipady      How many pixels to pad the widget's interior vertically    0
###############################################################################

* Syntax:
  * widget.grid(options)
"""


###############################################################################
# Import
###############################################################################


# Import
# * We will import tkinter to be used on the examples below.
import tkinter as tk


###############################################################################
# Row and Column
###############################################################################


# Row and Column
# * The row and column options determine the position of a widget in the grid.
# * The example below shows how to place widgets in different cells.
root = tk.Tk()
root.geometry("400x300")
b1 = tk.Button(master=root, text="Row 0, Col 0")
b2 = tk.Button(master=root, text="Row 0, Col 1")
b3 = tk.Button(master=root, text="Row 1, Col 0")
b4 = tk.Button(master=root, text="Row 1, Col 1")
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=1, column=0)
b4.grid(row=1, column=1)
root.mainloop()


###############################################################################
# Sticky
###############################################################################


# Sticky
# * The sticky option determines where the widget "sticks" inside its cell.
# * It is the equivalent of pack's fill and expand options.
# * The values are compass directions (N, S, E, W) or a combination.
# * The example below shows how to use sticky to make a widget fill its cell.
# * NOTE: The 'weight' configuration below makes the row and column expand with
#   the window. Without this, the cell would not grow and sticky would have no
#   effect.
root = tk.Tk()
root.geometry("400x300")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
b1 = tk.Button(master=root, text="Sticks to all sides")
b1.grid(row=0, column=0, sticky=tk.NSEW)
root.mainloop()


###############################################################################
# Padding and Spanning
###############################################################################


# Padding and Spanning
# * The padx and pady options add external padding to a widget.
# * The rowspan and columnspan options make a widget span multiple cells.
# * The example below shows a button that spans two rows and two columns.
root = tk.Tk()
root.geometry("400x300")
b1 = tk.Button(master=root, text="Spans two rows")
b2 = tk.Button(master=root, text="Regular button 1")
b3 = tk.Button(master=root, text="Regular button 2")
b4 = tk.Button(master=root, text="Spans two columns")
b1.grid(row=0, column=0, rowspan=2, padx=5, pady=5)
b2.grid(row=0, column=1, padx=5, pady=5)
b3.grid(row=1, column=1, padx=5, pady=5)
b4.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
root.mainloop()
