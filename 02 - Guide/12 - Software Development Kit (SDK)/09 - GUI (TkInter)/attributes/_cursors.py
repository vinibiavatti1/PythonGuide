"""
Cursors

* Python Tkinter supports quite a number of different mouse cursors available.
  The exact graphic may vary according to your operating system
* There are some cursors available on tkinter
"""
import tkinter as tk


###############################################################################
# Cursors
###############################################################################


# Cursors
# * The common available cursors are:
"""
arrow
crosshair
fleur
hand2
left_ptr
right_ptr
plus
question_arrow
sb_h_double_arrow
sb_v_double_arrow
watch
tcross
xterm
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
b1 = tk.Button(master=window, text='arrow', cursor='arrow')
b2 = tk.Button(master=window, text='crosshair', cursor='crosshair')
b3 = tk.Button(master=window, text='fleur', cursor='fleur')
b4 = tk.Button(master=window, text='hand2', cursor='hand2')
b5 = tk.Button(master=window, text='left_ptr', cursor='left_ptr')
b6 = tk.Button(master=window, text='right_ptr', cursor='right_ptr')
b7 = tk.Button(master=window, text='question_arrow', cursor='question_arrow')
b8 = tk.Button(master=window, text='h_double', cursor='sb_h_double_arrow')
b9 = tk.Button(master=window, text='v_double', cursor='sb_v_double_arrow')
b10 = tk.Button(master=window, text='watch', cursor='watch')
b11 = tk.Button(master=window, text='tcross', cursor='tcross')
b12 = tk.Button(master=window, text='xterm', cursor='xterm')


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
b11.pack(fill=tk.X)
b12.pack(fill=tk.X)


# Main loop
# * Start the application
window.mainloop()
