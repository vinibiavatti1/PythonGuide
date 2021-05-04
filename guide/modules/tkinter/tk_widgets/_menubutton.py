"""
Menubutton widget

* A menubutton is the part of a drop-down menu that stays on the screen all the
  time. Every menubutton is associated with a Menu widget (see above) that can
  display the choices for that menubutton when the user clicks on it
* Syntax:
  * tk.Menubutton(parent, option, ...)
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
keys = tk.Menubutton(master=window).keys()
[print(k) for k in keys]
window.destroy()
"""
activebackground
activeforeground
anchor
background
bd
bg
bitmap
borderwidth
cursor
direction
disabledforeground
fg
font
foreground
height
highlightbackground
highlightcolor
highlightthickness
image
indicatoron
justify
menu
padx
pady
relief
compound
state
takefocus
text
textvariable
underline
width
wraplength
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
widget = tk.Menubutton(
    master=window,
    text='Click here'
)
menu = tk.Menu(
    master=widget
)
menu.add_checkbutton(label='Option 1')
menu.add_checkbutton(label='Option 2')


# Set the menu for the menubutton
# * The configure method can be used to change some property of the widget
widget.configure(menu=menu)


# Set the position of the widget
# * The widget will be automatically adjusted
widget.pack()


# Main loop
# * Start the application
window.mainloop()
