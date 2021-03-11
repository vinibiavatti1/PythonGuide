"""
Tkinter file dialogs

* Provide file dialog windows that combine a native look-and-feel with
  configuration options to customize behaviour
* The following keyword arguments are applicable to the classes and functions
  listed below
  * parent - the window to place the dialog on top of
  * title - the title of the window
  * initialdir - the directory that the dialog starts in
  * initialfile - the file selected upon opening of the dialog
  * filetypes - a sequence of (label, pattern) tuples, * wildcard is allowed
  * defaultextension - default extension to append to file (save dialogs)
  * multiple - when true, selection of multiple items is allowed
"""
from tkinter import Tk, filedialog


###############################################################################
# Configuration
# * To use windows from tkinter a main window must be created as root
# * This window can be hidden which just dialogs will appear
###############################################################################


# Create Main window and hide this
root = Tk()
root.withdraw()


###############################################################################
# File dialogs
###############################################################################


# askopenfile(mode="r", **options)
# * Ask for a filename to open, and returned the opened file
# * The function creates an Open dialog and return the opened file object(s) in
#   read-only mode.
f = filedialog.askopenfile()
print(f.name)
# C:/file.txt


# askopenfiles(mode="r", **options)
# * Ask for multiple filenames and return the open file objects
# * The function creates an Open dialog and return the opened file object(s) in
#   read-only mode.
lst = filedialog.askopenfiles()
print(lst)
# [f1, f2, ...]


# asksaveasfile(mode="w", **options)
# * Ask for a filename to save as, and returned the opened file
# * Create a SaveAs dialog and return a file object opened in write-only mode
f = filedialog.asksaveasfile()
print(f.name)
# C:/file.txt


# askopenfilename(**options)
# * Ask for a filename to open
# * The function creates an Open dialog and returns the selected filename(s)
#   that correspond to existing file(s).
filename = filedialog.askopenfilename()
print(filename)
# C:/file.txt


# askopenfilenames(**options)
# * Ask for multiple filenames to open
# * The function creates an Open dialog and returns the selected filename(s)
#   that correspond to existing file(s).
filenames = filedialog.askopenfilenames()
print(filenames)
# ['C:/file.txt', 'C:/file2.txt']


# asksaveasfilename(**options)
# * Ask for a filename to save as
filenames = filedialog.asksaveasfilename()
print(filenames)
# C:/file.txt


# askdirectory(**options)
# * Ask for a directory, and return the file name
# * Additional parameter:
#   * mustexist - determines if selection must be an existing directory
directory = filedialog.askdirectory()
print(directory)
# C:/


# askdirectory(**options)
# * Ask for a directory, and return the file name
# * Additional parameter:
#   * mustexist - determines if selection must be an existing directory
directory = filedialog.askdirectory()
print(directory)
# C:/
