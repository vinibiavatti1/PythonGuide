"""
Grid

* This geometry manager organizes widgets in a table-like structure in the
  parent widget
* Syntax:
  * widget.grid(options)
"""
import tkinter as tk


###############################################################################
# Parameters
###############################################################################


# Parameters
# * Here is the list of possible options
"""
column          The column to put widget in; default 0 (leftmost column)
columnspan      How many columns widgetoccupies; default 1
ipadx, ipady    How many pixels to pad widget, horizontally and vertically,
                inside widget's borders
padx, pady      How many pixels to pad widget, horizontally and vertically,
                outside v's borders
row             The row to put widget in; default the first row that is still
                empty
rowspan         How many rowswidget occupies; default 1
sticky          What to do if the cell is larger than widget. By default, with
                sticky='', widget is centered in its cell. sticky may be the
                string concatenation of zero or more of N, E, S, W, NE, NW, SE,
                and SW, compass directions indicating the sides and corners of
                the cell to which widget sticks
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create widgets
# * Create widgets to represent the layout
r1c1 = tk.Label(master=window, text='R1C1')
r1c2 = tk.Label(master=window, text='R1C2')
r1c3 = tk.Label(master=window, text='R1C3')
r2c1 = tk.Label(master=window, text='R2C1')
r2c2 = tk.Label(master=window, text='R2C2')
r2c3 = tk.Label(master=window, text='R2C3')
r3c1 = tk.Label(master=window, text='R3C1')
r3c2 = tk.Label(master=window, text='R3C2')
r3c3 = tk.Label(master=window, text='R3C3')


# Define layout
# * The grid layout will be defined for each widget
r1c1.grid(row=1, column=1)
r1c2.grid(row=1, column=2)
r1c3.grid(row=1, column=3)
r2c1.grid(row=2, column=1)
r2c2.grid(row=2, column=2)
r2c3.grid(row=2, column=3)
r3c1.grid(row=3, column=1)
r3c2.grid(row=3, column=2)
r3c3.grid(row=3, column=3)


# Main loop
# * Start the application
window.mainloop()
