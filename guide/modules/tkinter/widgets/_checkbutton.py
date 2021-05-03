"""
Checkbutton widget

* The purpose of a checkbutton widget (sometimes called “checkbox”) is to allow
  the user to read and select a two-way choice
* The indicator is the part of the checkbutton that shows its state, and the
  label is the text that appears beside it
* Notes:
  * You will need to create a control variable, an instance of the IntVar
    class, so your program can query and set the state of the checkbutton
  * You can also use event bindings to react to user actions on the checkbutton
  * You can disable a checkbutton. This changes its appearance to “grayed out”
    and makes it unresponsive to the mouse
  * You can get rid of the checkbutton indicator and make the whole widget a
    “push-push” button that looks recessed when it is set, and looks raised
    when it is cleared.
* Syntax:
  * Checkbutton(master, option, ...)
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
keys = tk.Checkbutton(master=window).keys()
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
offvalue
onvalue
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
toggle()
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
widget = tk.Checkbutton(
    master=window,
    text='Check it'
)


# Set the position of the widget
# * The widget will be automatically adjusted
widget.pack()


# Main loop
# * Start the application
window.mainloop()
