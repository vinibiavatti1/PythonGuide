"""
Text widget

* Text widgets are a much more generalized method for handling multiple lines
  of text than the Label widget. Text widgets are pretty much a complete text
  editor in a window
  * You can mix text with different fonts, colors, and backgrounds
  * You can intersperse embedded images with text. An image is treated as a
    single character
  * An index is a way of describing a specific position between two characters
    of a text widget
  * A text widget may contain invisible mark objects between character
    positions
  * Text widgets allow you to define names for regions of the text called tags.
    You can change the appearance of a tagged region, changing its font,
    foreground and background colors, and other option
  * You can bind events to a tagged region
  * You can even embed a text widget in a “window” containing any Tkinter
    widget—even a frame widget containing other widgets. A window is also
    treated as a single character
* Syntax:
  * tk.Text(parent, option, ...)
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
keys = tk.Text(master=window).keys()
[print(k) for k in keys]
window.destroy()
"""
autoseparators
background
bd
bg
blockcursor
borderwidth
cursor
endline
exportselection
fg
font
foreground
height
highlightbackground
highlightcolor
highlightthickness
inactiveselectbackground
insertbackground
insertborderwidth
insertofftime
insertontime
insertunfocussed
insertwidth
maxundo
padx
pady
relief
selectbackground
selectborderwidth
selectforeground
setgrid
spacing1
spacing2
spacing3
startline
state
tabs
tabstyle
takefocus
undo
width
wrap
xscrollcommand
yscrollcommand
"""


###############################################################################
# Methods
###############################################################################


# Methods
# * The common methods for the widget are:
"""
bbox(index)
compare(index1, op, index2)
delete(index1, index2=None)
dlineinfo(index)
edit_modified(arg=None)
edit_redo()
edit_reset()
edit_separator()
edit_undo()
image_create(index[, option=value, ...])
get(index1, index2=None)
image_cget(index, option)
image_configure(index, option, ...)
image_names()
index(i)
insert(index, text, tags=None)
mark_gravity(mark, gravity=None)
mark_names()
mark_next(index)
mark_previous(index)
mark_set(mark, index)
mark_unset(mark)
scan_dragto(x, y)
scan_mark(x, y)
search(pattern, index, option, ...)
see(index)
tag_add(tagName, index1, index2=None)
tag_bind(tagName, sequence, func, add=None)
tag_cget(tagName, option)
tag_config(tagName, option, ...)
tag_delete(tagName, ...)
tag_lower(tagName, belowThis=None)
tag_names(index=None)
tag_nextrange(tagName, index1, index2=None)
tag_prevrange(tagName, index1, index2=None)
tag_raise(tagName, aboveThis=None)
tag_ranges(tagName)
tag_remove(tagName, index1, index2=None)
tag_unbind(tagName, sequence, funcid=None)
window_cget(index, option)
window_configure(index, option)
window_create(index, option, ...)
window_names()
xview(tk.MOVETO, fraction)
xview(tk.SCROLL, n, what)
xview_moveto(fraction)
xview_scroll(n, what)
yview(tk.MOVETO, fraction)
yview(tk.SCROLL, n, what)
yview_moveto(fraction)
yview_scroll(n, what)
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
widget = tk.Text(
    master=window
)
widget.insert('1.0', 'def main():\n')
widget.insert('2.0', '    pass\n')
widget.tag_add('styled', '1.0', '1.3')
widget.tag_add('styled', '2.4', '2.8')
widget.tag_config('styled', foreground='blue')


# Set the position of the widget
# * The widget will be automatically adjusted
widget.pack()


# Main loop
# * Start the application
window.mainloop()
