"""
Place

* This geometry manager organizes widgets by placing them in a specific
  position in the parent widget
* Syntax:
  * widget.place(options)
"""
import tkinter as tk


###############################################################################
# Parameters
###############################################################################


# Parameters
# * Here is the list of possible options
"""
anchor                  The exact spot of widget other options refer to: may be
                        N, E, S, W, NE, NW, SE, or SW, compass directions
                        indicating the corners and sides of widget; default is
                        NW (the upper left corner of widget)
bordermode              INSIDE (the default) to indicate that other options
                        refer to the parent's inside (ignoring the parent's
                        border); OUTSIDE otherwise
height, width           Height and width in pixels.
relheight, relwidth     Height and width as a float between 0.0 and 1.0, as a
                        fraction of the height and width of the parent widget
relx, rely              Horizontal and vertical offset as a float between 0.0
                        and 1.0, as a fraction of the height and width of the
                        parent widget
x, y                    Horizontal and vertical offset in pixels.
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create widgets
# * Create widgets to represent the layout
lb1 = tk.Label(master=window, text='Hello')
lb2 = tk.Label(master=window, text='World')
lb3 = tk.Label(master=window, text='!!!')


# Define layout
# * The grid layout will be defined for each widget
lb1.place(x=10, y=10)
lb2.place(x=15, y=25)
lb3.place(x=55, y=20)


# Main loop
# * Start the application
window.mainloop()
