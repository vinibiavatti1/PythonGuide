"""
Scrollbar widget

* A number of widgets, such as listboxes and canvases, can act like sliding
  windows into a larger virtual area. You can connect scrollbar widgets to them
  to give the user a way to slide the view around relative to the contents
  * Scrollbars can be horizontal, like the one shown above, or vertical. A
    widget that has two scrollable dimensions, such as a canvas or listbox, can
    have both a horizontal and a vertical scrollbar
  * The slider, or scroll thumb, is the raised-looking rectangle that shows the
    current scroll position
  * The two triangular arrowheads at each end are used for moving the position
    by small steps. The one on the left or top is called arrow1, and the one on
    the right or bottom is called arrow2
  * The trough is the sunken-looking area visible behind the arrowheads and
    slider. The trough is divided into two areas named trough1 (above or to the
    left of the slider) and trough2 (below or to the right of the slider)
  * The slider's size and position, relative to the length of the entire
    widget, show the size and position of the view relative to its total size.
    For example, if a vertical scrollbar is associated with a listbox, and its
    slider extends from 50% to 75% of the height of the scrollbar, that means
    that the visible part of the listbox shows that portion of the overall list
    starting at the halfway mark and ending at the three-quarter mark
  * In a horizontal scrollbar, clicking B1 (button 1) on the left arrowhead
    moves the view by a small amount to the left. Clicking B1 on the right
    arrowhead moves the view by that amount to the right. For a vertical
    scrollbar, clicking the upward- and downward-pointing arrowheads moves the
    view small amounts up or down. Refer to the discussion of the associated
    widget to find out the exact amount that these actions move the view
  * The user can drag the slider with B1 or B2 (the middle button) to move the
    view
  * For a horizontal scrollbar, clicking B1 in the trough to the left of the
    slider moves the view left by a page, and clicking B1 in the trough to the
    right of the slider moves the view a page to the right. For a vertical
    scrollbar, the corresponding actions move the view a page up or down
  * Clicking B2 anywhere along the trough moves the slider so that its left or
    top end is at the mouse, or as close to it as possible
* The normalized position of the scrollbar refers to a number in the closed
  interval [0.0, 1.0] that defines the slider's position. For vertical
  scrollbars, position 0.0 is at the top and 1.0 at the bottom; for horizontal
  scrollbars, position 0.0 is at the left end and 1.0 at the right
* Syntax:
  * tk.Scrollbar(parent, option, ...)
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
keys = tk.Scrollbar(master=window).keys()
[print(k) for k in keys]
window.destroy()
"""
activebackground
activerelief
background
bd
bg
borderwidth
command
cursor
elementborderwidth
highlightbackground
highlightcolor
highlightthickness
jump
orient
relief
repeatdelay
repeatinterval
takefocus
troughcolor
width
"""


###############################################################################
# Methods
###############################################################################


# Methods
# * The common methods for the widget are:
"""
activate(element=None)
delta(dx, dy)
fraction(x, y)
get()
identify(x, y)
set(first, last)
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
widget = tk.Scrollbar(master=window)


# Set the position of the widget
# * The widget will be automatically adjusted
widget.pack(side=tk.RIGHT, fill=tk.Y)


# Create the panel to be scrooled
# * For the example, the Text widget was used
text = tk.Text(master=window, yscrollcommand=widget.set)
text.insert('1.0', 'example\n' * 50)
widget.config(command=text.yview)


# Set the position of the panel
# * The widget will be automatically adjusted
text.pack(side=tk.LEFT)


# Main loop
# * Start the application
window.mainloop()
