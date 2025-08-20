"""
Scrollbar widget (TTK)

* This is the ttk version of Scrollbar widget from TK
* Syntax:
  * ttk.Scrollbar(parent, option, ...)
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
keys = ttk.Scrollbar(master=window).keys()
[print(k) for k in keys]
window.destroy()
"""
command
orient
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
delta(dx, dy)
fraction(x, y)
get()
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
widget = ttk.Scrollbar(master=window)


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
