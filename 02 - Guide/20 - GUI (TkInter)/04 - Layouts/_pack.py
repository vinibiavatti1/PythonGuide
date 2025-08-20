"""
Pack

* This geometry manager organizes widgets in blocks before placing them in the
  parent widget
* Syntax:
  * widget.pack(options)
"""
import tkinter as tk


###############################################################################
# Parameters
###############################################################################


# Parameters
# * Here is the list of possible options
"""
expand          When set to true, widget expands to fill any space not
                otherwise used in widget's parent
fill            Determines whether widget fills any extra space allocated to it
                by the packer, or keeps its own minimal dimensions: NONE
                (default), X (fill only horizontally), Y (fill only
                vertically), or BOTH (fill both horizontally and vertically)
side            Determines which side of the parent widget packs against: TOP
                (default), BOTTOM, LEFT, or RIGHT
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create widgets
# * Create widgets to represent the layout
top = tk.Label(master=window, text='top')
bottom = tk.Label(master=window, text='bottom')
left = tk.Label(master=window, text='left')
right = tk.Label(master=window, text='right')


# Define layout
# * The pack layout will be defined for each widget
top.pack(side=tk.TOP)
bottom.pack(side=tk.BOTTOM)
left.pack(side=tk.LEFT)
right.pack(side=tk.RIGHT)


# Main loop
# * Start the application
window.mainloop()
