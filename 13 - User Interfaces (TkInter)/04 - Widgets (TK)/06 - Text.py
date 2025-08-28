"""
Text

* The Text widget is used to create a multi-line text input field.
* It is commonly used for user input, such as entering a message or a
  comment.
* The state of the Text widget cannot be controlled using a variable. We must
  use the widget's methods to manipulate its content.
* In other libraries, it is often referred to as a text area.
* The Text widget supports various text formatting options, such as font
  styles, colors, and sizes. It also can be used to display syntax-highlighted
  code.
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
# * We can use the tags to style specific parts of the text.
# * Note that this widget doesn't support a variable binding.
root = tk.Tk()
text = tk.Text(
    master=root,
    width=50,
    height=20,
)
text.insert('1.0', 'def main():\n')
text.insert('2.0', '    pass\n')
text.tag_add('styled', '1.0', '1.3')
text.tag_add('styled', '2.4', '2.8')
text.tag_config('styled', foreground='blue')
text.pack(padx=20, pady=20)
root.mainloop()


###############################################################################
# Parameters & Methods
###############################################################################


# Keys
# * The `keys` method shows all parameters for the widget creation.
text = tk.Text()
[print(k) for k in text.keys()]
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
