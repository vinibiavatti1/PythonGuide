"""
Widget (TTK)

* The ttk module contains different versions of most of the standard Tkinter
  widgets and a few new ones.
* These widgets replace the ones from Tkinter of the same name.
* Both sets of widgets can be used interchangeably, but the ttk widgets offer
  a more modern look and feel.
* The ttk module also provides additional features, such as improved styling
  options and better support for themes.
* These features make it easier to create visually appealing and user-friendly
  applications.
* To define styles for ttk widgets, you can use the `ttk.Style` class.
* Reference: https://docs.python.org/3/library/tkinter.ttk.html
"""


###############################################################################
# Standard Options
###############################################################################


# Standard Options
# * The TTK widgets standard options are:
"""
class
cursor
takefocus
style
"""


###############################################################################
# Styles
###############################################################################


# Import
# * We will import tkinter to be used on the examples below.
import tkinter as tk
import tkinter.ttk as ttk


# Defining Styles
# * We can create a new style using the `ttk.Style().configure()` method.
# * We can also modify existing styles by calling the same method with the
#   style name.
# * Styles can be applied to individual widgets or globally to all widgets of
#   a certain type.
root = tk.Tk()
style = ttk.Style()
style.configure(
    "My.TButton",
    padding=6,
    foreground="blue",
)


# Using Styles
# * We can now use the custom style for our button.
button1 = ttk.Button(
    master=root,
    text='Default',
)
button2 = ttk.Button(
    master=root,
    text='Custom',
    style='My.TButton'
)
button1.pack(padx=20, pady=20)
button2.pack(padx=20, pady=20)
root.mainloop()
