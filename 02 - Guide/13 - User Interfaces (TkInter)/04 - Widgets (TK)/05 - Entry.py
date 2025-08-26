"""
Entry

* The Entry widget is used to create a single-line text input field.
* It is commonly used for user input, such as entering a name or a search
  query.
* The state of the check button can be controlled using a variable.
* In other libraries, it is often referred to as a text field or text box.
"""


###############################################################################
# Import
###############################################################################


# Import
# * We will import tkinter to be used on the examples below.
import tkinter as tk


###############################################################################
# Example
###############################################################################


# Example
# * The example below creates a simple GUI application with the widget.
root = tk.Tk()
var = tk.StringVar(value='Hello World!')
entry = tk.Entry(
    master=root,
    textvariable=var
)
entry.pack(padx=20, pady=20)
root.mainloop()


###############################################################################
# Parameters & Methods
###############################################################################


# Keys
# * The `keys` method shows all parameters for the widget creation.
entry = tk.Entry()
[print(k) for k in entry.keys()]
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
