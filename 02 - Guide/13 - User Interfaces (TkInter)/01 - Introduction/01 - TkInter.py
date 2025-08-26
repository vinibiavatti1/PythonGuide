"""
TkInter

* TkInter is a Python binding to the Tk GUI toolkit. It is a thin
  object-oriented layer on top of Tcl/Tk.
* The built-in tkinter module in Python provides access to the Tk GUI toolkit.
* TkInter is cross-platform and works on Windows, macOS, and Linux.
"""


###############################################################################
# Module Import
###############################################################################


# TkInter import
# * To start using TkInter, we must import the tkinter module.
# * Usually, the alias "tk" is used to reference the module.
import tkinter as tk


###############################################################################
# Root Window
###############################################################################


# Defining the Root Window
# * To start implementing the GUI, we need to create a root window.
# * The root window serves as the main container for all other GUI elements. It
#   is the foundational element of the library.
# * A root window is always mandatory, even if only other windows are used, or
#   only dialogs.
# * To define a root window, we create an instance of the Tk class.
root = tk.Tk()


# Defining the Title
# * We can use the `title()` method to set the title of the root window.
root.title("My Tkinter App")


# Defining the Geometry
# * We can use the `geometry()` method to set the size and position of the root
#   window.
# * This method takes a string that accepts the formats below:
#   * <width>x<height>
#   * <width>x<height>+<x_offset>+<y_offset>
#   * <x_offset>+<y_offset>
root.geometry('400x300')   # Set size
root.geometry('+100+100')  # Set position


# Defining Resizability
# * We can set the resizability of the root window using the `resizable()`
#   method.
# * This method takes two boolean arguments:
#   * The first argument controls the horizontal resizability.
#   * The second argument controls the vertical resizability.
root.resizable(True, True)


# Showing and Hiding the Window
# * We can use the `withdraw()` method to hide the root window.
# * We can use the `deiconify()` method to show the root window.
root.withdraw()
root.deiconify()


# Changing the configuration
# * The `config` or `configure` are universal methods in Tkinter.
# * They can be used to modify the properties of widgets at any time.
# * For example, we can change the text of a label or the background color of a
#   button.
# * The syntax is as follows:
#   * `widget.config(option=value, ...)`
#   * `widget.configure(option=value, ...)`
# * In the example below, we are defining the background color and cursor style
#   for the root window.
root.config(bg='lightblue', cursor='cross')


# Defining an Icon
# * We can set a custom icon for the root window using the `iconbitmap()` or
#   `iconphoto()` methods.
# * The difference between the two methods is that `iconbitmap()` is used for
#   .ico files, while `iconphoto()` is used for .png files.
from pathlib import Path
path = Path.cwd()
root.iconbitmap(path / '__resources' / 'bricks.bmp')
root.iconphoto(False, tk.PhotoImage(file=path / '__resources' / 'bricks.png'))


# Main Loop
# * The main loop is the core of any Tkinter application.
# * It listens for events, such as button clicks or keypresses.
# * The main loop is started by calling the `mainloop()` method on the root
#   window.
# * Without a main loop, the application will not respond to user input or even
#   update the GUI.
# * Since the main loop locks the main thread, no other code can run until the
#   window is closed.
root.mainloop()


# Destroying the Window
# * The `destroy()` method is used to close the window and terminate the
#   application.
# * This method should be called when the application is done and no longer
#   needs the window.
# * Since the window was already destroyed, we needed create a window again to
#   demonstrate the usage of the `destroy()` method.
root = tk.Tk()
root.destroy()
