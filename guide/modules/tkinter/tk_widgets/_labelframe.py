"""
LabelFrame widget

* The LabelFrame widget, like the Frame widget, is a spatial container—a
  rectangular area that can contain other widgets. However, unlike the Frame
  widget, the LabelFrame widget allows you to display a label as part of the
  border around the area
* Syntax:
  * tk.LabelFrame(parent, option, ...)
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
keys = tk.LabelFrame(master=window).keys()
[print(k) for k in keys]
window.destroy()
"""
bd
borderwidth
class
fg
font
foreground
labelanchor
labelwidget
relief
text
background
bg
colormap
container
cursor
height
highlightbackground
highlightcolor
highlightthickness
padx
pady
takefocus
visual
width
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
widget = tk.LabelFrame(
    master=window,
    text='Title'
)
label = tk.Label(
    master=widget,
    text='Inside'
)
label.pack()


# Set the position of the widget
# * The widget will be automatically adjusted
widget.pack()


# Main loop
# * Start the application
window.mainloop()
