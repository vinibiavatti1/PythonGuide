"""
Entry widget

* The purpose of an Entry widget is to let the user see and modify a single
  line of text
* The selection is a highlighted region of the text in an Entry widget, if
  there is one
* The insertion cursor shows where new text will be inserted. It is displayed
  only when the user clicks the mouse somewhere in the widget. It usually
  appears as a blinking vertical line inside the widget. You can customize its
  appearance in several ways
* Positions within the widget's displayed text are given as an index. There are
  several ways to specify an index:
  * As normal Python indexes, starting from 0
  * The constant tk.END refers to the position after the existing text
  * The constant tk.INSERT refers to the current position of the insertion
    cursor
  * The constant tk.ANCHOR refers to the first character of the selection, if
    there is a selection
* Syntax:
  * tk.Entry(parent, option, ...)
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
keys = tk.Entry(master=window).keys()
[print(k) for k in keys]
window.destroy()
"""
background
bd
bg
borderwidth
cursor
disabledbackground
disabledforeground
exportselection
fg
font
foreground
highlightbackground
highlightcolor
highlightthickness
insertbackground
insertborderwidth
insertofftime
insertontime
insertwidth
invalidcommand
invcmd
justify
readonlybackground
relief
selectbackground
selectborderwidth
selectforeground
show
state
takefocus
textvariable
validate
validatecommand
vcmd
width
xscrollcommand
"""


###############################################################################
# Methods
###############################################################################


# Methods
# * The common methods for the widget are:
"""
delete(first, last=None)
get()
icursor(index)
index(index)
insert(index, s)
scan_dragto(x)
scan_mark(x)
select_adjust(index)
select_clear()
select_from(index)
select_present()
select_range(start, end)
select_to(index)
xview(index)
xview_moveto(f)
xview_scroll(number, what)
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
variable = tk.StringVar(master=window)
variable.set('Hello World!')
widget = tk.Entry(
    master=window,
    textvariable=variable
)


# Set the position of the widget
# * The widget will be automatically adjusted
widget.pack()


# Main loop
# * Start the application
window.mainloop()
