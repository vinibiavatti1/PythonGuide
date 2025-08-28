"""
File Dialog

* The `tkinter.filedialog` module provides a way to create file dialog boxes
  for opening and saving files.
* It includes functions to prompt the user for a file to open or save.
* The dialogs are modal, meaning they block input to other windows until
  closed.
* The user can cancel the dialog, which will return None.
* If the user selects an invalid file, an error message will be shown.
* The dialogs can be customized with additional options, such as initial
  directory and file types.
"""


###############################################################################
# Import
###############################################################################


# Import
# * We will import tkinter to be used on the examples below.
from tkinter import filedialog


###############################################################################
# Open File Dialogs
###############################################################################


# Open File Name
# * The `askopenfilename` function is used to open a file dialog and select a
#   single file.
# * It only returns the path of the selected file as a string. It does not open
#   or read the file.
x = filedialog.askopenfilename()
print(x)
# C:/file.txt


# Open File Names
# * Similar to `askopenfilename`, the `askopenfilenames` function is used to
#   open a file dialog and select multiple files.
# * It returns a list of the selected file's paths as strings. It does not open
#   or read the files.
x = filedialog.askopenfilenames()
print(x)
# ['C:/file.txt', 'C:/file2.txt']


# Open File
# * The `askopenfile` function is used to open a file dialog and select a
#   single file.
# * It returns a file object for the selected file. The file is opened in
#   read-only mode.
x = filedialog.askopenfile()
print(x)
# <_io.TextIOWrapper name='C:/file.txt' mode='r' encoding='UTF-8'>


# Open Files
# * The `askopenfiles` function is used to open a file dialog and select
#   multiple files.
# * It returns a list of file objects for the selected files. The files are
#   opened in read-only mode.
x = filedialog.askopenfiles()
print(x)
# [<_io.TextIOWrapper name='C:/file.txt' mode='r' encoding='UTF-8'>, ...]


###############################################################################
# Save File Dialogs
###############################################################################


# Save File Name
# * The `asksaveasfilename` function is used to open a file dialog and select
#   a file to save.
# * It returns the path of the selected file as a string. It does not open
#   or create the file.
x = filedialog.asksaveasfilename()
print(x)
# C:/file.txt


# Save File
# * The `asksaveasfile` function is used to open a file dialog and select
#   a file to save.
# * It returns a file object for the selected file. The file is opened in
#   write mode.
# * This function accepts a "mode" argument that accepts:
#   * "w" - write mode
#   * "a" - append mode
# * If the file does not exist, it will be created.
x = filedialog.asksaveasfile()
print(x)
# <_io.TextIOWrapper name='C:/file.txt' mode='w' encoding='UTF-8'>


###############################################################################
# Directory Dialogs
###############################################################################


# Select Directory
# * The `askdirectory` function is used to open a file dialog and select a
#   directory.
# * It returns the path of the selected directory as a string. It does not open
#   or create the directory.
x = filedialog.askdirectory()
print(x)
# C:/folder


###############################################################################
# File Extensions
###############################################################################


# Setting File Extensions
# * To set the file extensions for the file dialog, use the "filetypes"
#   argument.
# * This argument accepts a list of tuples, where each tuple contains a label
#   and a pattern.
# * The label is displayed in the file dialog, and the pattern is used to
#   filter the files.
x = filedialog.askopenfilename(filetypes=[("Text", "*.txt"), ("All", "*.*")])
print(x)
# C:/file.txt
