"""
Canvas widget

* A canvas is a rectangular area intended for drawing pictures or other complex
* Syntax:
  * tk.Canvas(parent, option=value, ...)
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
keys = tk.Canvas(master=window).keys()
[print(k) for k in keys]
window.destroy()
"""
background
bd
bg
borderwidth
closeenough
confine
cursor
height
highlightbackground
highlightcolor
highlightthickness
insertbackground
insertborderwidth
insertofftime
insertontime
insertwidth
offset
relief
scrollregion
selectbackground
selectborderwidth
selectforeground
state
takefocus
width
xscrollcommand
xscrollincrement
yscrollcommand
yscrollincrement
"""


###############################################################################
# Methods
###############################################################################


# Methods
# * The common methods for the widget are:
"""
create_arc(x0, y0, x1, y1, option, ...)
create_bitmap(x, y, *options ...)
create_image(x, y, option, ...)
create_line(x0, y0, x1, y1, ..., xn, yn, option, ...)
create_oval(x0, y0, x1, y1, option, ...)
create_polygon(x0, y0, x1, y1, ..., option, ...)
create_rectangle(x0, y0, x1, y1, option, ...)
create_text(x, y, option, ...)
create_window(x, y, option, ...)
addtag_above(newTag, tagOrId)
addtag_all(newTag)
addtag_below(newTag, tagOrID)
addtag_closest(newTag, x, y, halo=None, start=None)
addtag_enclosed(newTag, x1, y1, x2, y2)
addtag_overlapping(newTag, x1, y1, x2, y2)
addtag_withtag(newTag, tagOrId)
bbox(tagOrId=None)
canvasx(screenx, gridspacing=None)
canvasy(screeny, gridspacing=None)
coords(tagOrId, x0, y0, x1, y1, ..., xn, yn)
dchars(tagOrId, first=0, last=first)
delete(tagOrId)
dtag(tagOrId, tagToDelete)
find_above(tagOrId)
find_all()
find_below(tagOrId)
find_closest(x, y, halo=None, start=None)
find_enclosed(x1, y1, x2, y2)
find_overlapping(x1, y1, x2, y2)
find_withtag(tagOrId)
focus(tagOrId=None)
gettags(tagOrId)
icursor(tagOrId, index)
index(tagOrId, specifier)
insert(tagOrId, specifier, text)
itemcget(tagOrId, option)
itemconfigure(tagOrId, option, ...)
move(tagOrId, xAmount, yAmount)
postscript(option, ...)
scale(tagOrId, xOffset, yOffset, xScale, yScale)
scan_dragto(x, y, gain=10.0)
scan_mark(x, y)
select_adjust(oid, specifier)
select_clear()
select_from(oid, specifier)
select_item()
select_to(oid, specifier)
tag_bind(tagOrId, sequence=None, function=None, add=None)
tag_lower(tagOrId, belowThis)
tag_raise(tagOrId, aboveThis)
tag_unbind(tagOrId, sequence, funcId=None)
type(tagOrId)
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
widget = tk.Canvas(
    master=window,
    width=400,
    height=300,
    bg='black'
)


# Set the position of the widget
# * The widget will be automatically adjusted
widget.pack()


# Main loop
# * Start the application
window.mainloop()
