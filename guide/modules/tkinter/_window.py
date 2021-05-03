"""
Window

* Tkinter is the only GUI framework that's built into the Python standard
  library
* It's cross-platform, so the same code works on Windows, macOS, and Linux
* Visual elements are rendered using native operating system elements, so
  applications built with Tkinter look like they belong on the platform where
  they're run
"""
import tkinter as tk


###############################################################################
# Window
###############################################################################


# Tk
# * The foundational element of a Tkinter GUI is the window
# * Windows are the containers in which all other GUI elements live
# * Widgets are contained inside of windows
# * To create an window, we can use the Tk() class from tkinter module
window = tk.Tk()


# title(title)
# * The title of the window can be changed by title() method
window.title('Python Guide')


# geometry(size)
# * The geometry method sets the size and the position of the window by the
#   pattern:
#   * Size: '<width>x<height>'
#   * Position: '+<position_x>+<position_y>'
#   * Both: '<width>x<height>+<position_x>+<position_y>'
window.geometry('400x300')   # Set size
window.geometry('+100+100')  # Set position


# resizable(x, y)
# * The resizable() method
window.resizable(False, False)


# withdraw()
# * Hides the window
window.withdraw()


# deiconify()
# * Shows the window
window.deiconify()


# mainloop()
# * mainloop() tells Python to run the Tkinter event loop
# * This method listens for events, such as button clicks or keypresses
# * NOTE: This method blocks any code that comes after it from running until
#   the window it's called on is closed
# * NOTE: This method must be executed to allow Tkinter to render the windows
window.mainloop()


# destroy()
# * Destroys the window
window = tk.Tk()
window.destroy()
