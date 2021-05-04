"""
Notebook widget (TTK)

* The purpose of a Notebook widget is to provide an area where the user can
  select pages of content by clicking on tabs at the top of the area
* Each time the user clicks on one of these tabs, the widget will display the
  child pane associated with that tab. Typically, each pane will be a Frame
  widget, although a pane can be any widget
* The tab for the child pane that is currently showing is referred to as the
  selected tab
* You will use the Notebook widget's .add() method to attach a new tab, and its
  related content. Other methods let you remove or temporarily hide tabs
* Each tab has its own set of options that control its appearance and behavior
* A number of the methods of this widget use the idea of a tabId to refer to
  one of the tabs
* Syntax:
  * ttk.Notebook(parent, option=value, ...)
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
keys = ttk.Notebook(master=window).keys()
[print(k) for k in keys]
window.destroy()
"""
width
height
padding
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
add(child, **kw)
enable_traversal()
forget(child)
hide(tabId)
index(tabId)
insert(where, child,**kw)
select([tabId])
tab(tabId, option=None, **kw)
tabs()
"""


###############################################################################
# Tab options
###############################################################################


# Tab options
# * Here are the tab options used in the .add() and .tab() methods
"""
compound
padding
sticky
image
text
underline
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
widget = ttk.Notebook(master=window)
panel1 = ttk.Frame(master=window, width=400, height=300)
panel2 = ttk.Frame(master=window, width=400, height=300)
panel3 = ttk.Frame(master=window, width=400, height=300)
widget.add(panel1, text='Tab 1')
widget.add(panel2, text='Tab 2')
widget.add(panel3, text='Tab 3')


# Set the position of the widget
# * The widget will be automatically adjusted
widget.pack()


# Main loop
# * Start the application
window.mainloop()
