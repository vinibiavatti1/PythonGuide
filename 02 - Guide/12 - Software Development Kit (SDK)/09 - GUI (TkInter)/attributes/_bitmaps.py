"""
Bitmaps

* This attribute to displays a bitmap image to the widget
* There are some bitmaps available on tkinter
"""
import tkinter as tk


###############################################################################
# Bitmaps
###############################################################################


# Bitmaps
# * The bitmaps are:
"""
error
gray75
gray50
gray25
gray12
hourglass
info
questhead
question
warning
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
b1 = tk.Button(master=window, bitmap='error')
b2 = tk.Button(master=window, bitmap='gray75')
b3 = tk.Button(master=window, bitmap='gray50')
b4 = tk.Button(master=window, bitmap='gray25')
b5 = tk.Button(master=window, bitmap='gray12')
b6 = tk.Button(master=window, bitmap='hourglass')
b7 = tk.Button(master=window, bitmap='info')
b8 = tk.Button(master=window, bitmap='questhead')
b9 = tk.Button(master=window, bitmap='question')
b10 = tk.Button(master=window, bitmap='warning')


# Set the position of the widget
# * The widget will be automatically adjusted
b1.pack(fill=tk.X)
b2.pack(fill=tk.X)
b3.pack(fill=tk.X)
b4.pack(fill=tk.X)
b5.pack(fill=tk.X)
b6.pack(fill=tk.X)
b7.pack(fill=tk.X)
b8.pack(fill=tk.X)
b9.pack(fill=tk.X)
b10.pack(fill=tk.X)


# Main loop
# * Start the application
window.mainloop()
