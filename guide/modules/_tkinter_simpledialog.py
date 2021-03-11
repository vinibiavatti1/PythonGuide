"""
TKInter simpledialog module

* The tkinter.simpledialog module contains convenience classes and functions
  for creating simple modal dialogs to get a value from the user
"""
from tkinter import Tk, simpledialog


###############################################################################
# Configuration
# * To use windows from tkinter a main window must be created as root
# * This window can be hidden which just dialogs will appear
###############################################################################


# Create Main window and hide this
root = Tk()
root.withdraw()


###############################################################################
# Input dialogs
###############################################################################


# askstring(title, prompt, **kw)
# * Ask string
answer = simpledialog.askstring('Dialog', 'Say something')
print(answer)
# Something


# askinteger(title, prompt, **kw)
# * Ask integer
answer = simpledialog.askinteger('Dialog', 'Put an integer')
print(answer)
# 1


# askfloat(title, prompt, **kw)
# * Ask float
answer = simpledialog.askfloat('Dialog', 'Put a float')
print(answer)
# 1.5
