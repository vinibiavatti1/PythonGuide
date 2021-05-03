"""
Frame widget

* A frame is basically just a container for other widgets
* Your application's root window is basically a frame
* Each frame has its own grid layout, so the gridding of widgets within each
  frame works independently
* Frame widgets are a valuable tool in making your application modular. You can
  group a set of related widgets into a compound widget by putting them into a
  frame. Better yet, you can declare a new class that inherits from Frame,
  adding your own interface to it. This is a good way to hide the details of
  interactions within a group of related widgets from the outside world
* Syntax:
  * tk.Frame(parent, option, ...)
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
keys = tk.Frame(master=window).keys()
[print(k) for k in keys]
window.destroy()
"""
bd
borderwidth
class
relief
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
widget = tk.Frame(
    master=window
)


# Main loop
# * Start the application
window.mainloop()
