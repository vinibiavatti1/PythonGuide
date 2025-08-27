"""
Notebook (TTK)

* The Notebook widget (TTK) is used to create a tabbed interface.
* It allows the user to switch between different frames (tabs) within the same
  window.
* Each tab can contain its own set of widgets and layout.
* The Notebook widget can be customized in terms of its appearance and
  behavior.
* It is useful for organizing related content and improving the user
  experience.
* The Notebook widget is part of the TTK (Themed Tkinter) module, which
  provides a more modern look and feel for Tkinter applications.
* In other languages, similar tabbed interfaces are often referred to as
  "tabbed panels" or "tab views."
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
notebook = ttk.Notebook(master=root)
panel1 = ttk.Frame(master=root, width=400, height=300)
panel2 = ttk.Frame(master=root, width=400, height=300)
panel3 = ttk.Frame(master=root, width=400, height=300)
notebook.add(panel1, text='Tab 1')
notebook.add(panel2, text='Tab 2')
notebook.add(panel3, text='Tab 3')
notebook.pack(padx=20, pady=20)
root.mainloop()


###############################################################################
# Parameters & Methods
###############################################################################


# Keys
# * The `keys` method shows all parameters for the widget creation.
notebook = ttk.Notebook()
[print(k) for k in notebook.keys()]
"""
width
height
padding
takefocus
cursor
style
class
"""
