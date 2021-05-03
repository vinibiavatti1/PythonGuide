"""
Colors

* Tkinter represents colors with strings. There are two general ways to specify
  colors in Tkinter:
  * Hexadecimal
  * String names
* Reference:
  * https://www.tutorialspoint.com/python/python_gui_programming.htm
"""
import tkinter as tk


###############################################################################
# Colors
###############################################################################


# Colors
# * There are preset colors in tkinter that can be used with their string names
# * The hexadecimal value can be used also to define a specific color
"""
###############################################################################
Color                   String name                 Hexadecimal
###############################################################################
white                   'white'                     #FFFFFF
black                   'black'                     #000000
red                     'red'                       #FF0000
green                   'green'                     #00FF00
blue                    'blue'                      #0000FF
cyan                    'cyan'                      #00FFFF
yellow                  'yellow'                    #FFFF00
magenta                 'magenta'                   #FF00FF
###############################################################################
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
b1 = tk.Button(master=window, text='White', bg='white')
b2 = tk.Button(master=window, text='Black', bg='black', fg='white')
b3 = tk.Button(master=window, text='Red', bg='red')
b4 = tk.Button(master=window, text='Green', bg='green')
b5 = tk.Button(master=window, text='Blue', bg='blue')
b6 = tk.Button(master=window, text='Cyan', bg='cyan')
b7 = tk.Button(master=window, text='Yellow', bg='yellow')
b8 = tk.Button(master=window, text='Magenta', bg='magenta')
b9 = tk.Button(master=window, text='Orange', bg='#FFA500')
b10 = tk.Button(master=window, text='Grey', bg='#808080')


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
