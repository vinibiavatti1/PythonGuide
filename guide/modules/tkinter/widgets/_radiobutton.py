"""
Radiobutton widget

* Radiobuttons are sets of related widgets that allow the user to select only
  one of a set of choices. Each radiobutton consists of two parts, the
  indicator and the label
  * The indicator is the diamond-shaped part that turns red in the selected
    item
  * The label is the text, although you can use an image or bitmap as the label
  * If you prefer, you can dispense with the indicator. This makes the
    radiobuttons look like “push-push” buttons, with the selected entry
    appearing sunken and the rest appearing raised
  * To form several radiobuttons into a functional group, create a single
    control variable, and set the variable option of each radiobutton to that
    variable
  * The control variable can be either an IntVar or a StringVar. If two or more
    radiobuttons share the same control variable, setting any of them will
    clear the others
  * Each radiobutton in a group must have a unique value option of the same
    type as the control variable. For example, a group of three radiobuttons
    might share an IntVar and have values of 0, 1, and 99. Or you can use a
    StringVar control variable and give the radiobuttons value options like
    'too hot', 'too cold', and 'just right'
* Syntax:
  * tk.Radiobutton(parent, option, ...)
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
keys = tk.Radiobutton(master=window).keys()
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
command
compound
cursor
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
offrelief
overrelief
padx
pady
relief
selectcolor
selectimage
state
takefocus
text
textvariable
tristateimage
tristatevalue
underline
value
variable
width
wraplength
"""


###############################################################################
# Methods
###############################################################################


# Methods
# * The common methods for the widget are:
"""
deselect()
flash()
invoke()
select()
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
variable = tk.IntVar()
variable.set(1)
radio1 = tk.Radiobutton(
    master=window,
    text='Option 1',
    variable=variable,
    value=1
)
radio2 = tk.Radiobutton(
    master=window,
    text='Option 2',
    variable=variable,
    value=2
)
radio3 = tk.Radiobutton(
    master=window,
    text='Option 3',
    variable=variable,
    value=3
)


# Set the position of the widget
# * The widget will be automatically adjusted
radio1.pack()
radio2.pack()
radio3.pack()


# Main loop
# * Start the application
window.mainloop()
