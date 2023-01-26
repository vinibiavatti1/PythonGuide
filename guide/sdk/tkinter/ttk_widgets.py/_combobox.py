"""
Combobox widget (TTK)

* This widget is a combination of an Entry and a drop-down menu. In your
  application, you will see the usual text entry area, with a downward-pointing
  arrow. When the user clicks on the arrow, a drop-down menu appears. If the
  user clicks on one, that choice replaces the current contents of the entry.
  However, the user may still type text directly into the entry (when it has
  focus), or edit the current text
* Syntax:
  * ttk.Combobox(parent, option, ...)
* Reference:
  * https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html
"""
import tkinter as tk
from tkinter import ttk


###############################################################################
# Parameters
###############################################################################


# keys()
# * The keys method shows all parameters for the widget creation
window = tk.Tk()
window.withdraw()
keys = ttk.Combobox(master=window).keys()
[print(k) for k in keys]
window.destroy()
"""
height
postcommand
values
exportselection
font
invalidcommand
justify
show
state
textvariable
validate
validatecommand
width
xscrollcommand
foreground
background
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
current([index])
set(value)
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
widget = ttk.Combobox(
    master=window,
    text='Select an option',
    values=('Option 1', 'Option 2')
)


# Set the position of the widget
# * The widget will be automatically adjusted
widget.pack()


# Main loop
# * Start the application
window.mainloop()
