"""
Widget

* TkInter Widgets are the building blocks of a GUI application.
* They provide a way to create user interface elements such as buttons, labels,
  and text boxes.
* In other languages, these elements may be referred to as controls or
  components.
* NOTE: It is always recommended to use the TTK (Themed Tkinter) widgets
  for a more modern look and feel.
* Reference: https://docs.python.org/3/library/tkinter.html
"""


###############################################################################
# Styles
###############################################################################


# Import
# * We will import tkinter to be used on the examples below.
import tkinter as tk


# Defining Styles
# * Since only TTK widgets support styling, we can still set custom styles for
#   regular Tkinter widgets by configuring their options directly.
root = tk.Tk()
button1 = tk.Button(
    master=root,
    text='Default',
)
button2 = tk.Button(
    master=root,
    text='Custom',
    padx=6,
    pady=6,
    foreground="blue",
)
button1.pack(padx=20, pady=20)
button2.pack(padx=20, pady=20)
root.mainloop()
