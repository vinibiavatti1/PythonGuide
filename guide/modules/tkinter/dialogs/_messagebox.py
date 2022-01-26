"""
TKInter messagebox module

* The message boxes are modal and will return a subset of (True, False, OK,
  None, Yes, No) based on the user's selection
"""
from tkinter import Tk, messagebox


###############################################################################
# Configuration
# * To use windows from tkinter a main window must be created as root
# * This window can be hidden which just messagebox will appear
###############################################################################


# Create Main window and hide this
root = Tk()
root.withdraw()


###############################################################################
# Information message box
###############################################################################


# Show info
messagebox.showinfo('Information', 'Information box')


###############################################################################
# Warning message boxes
###############################################################################


# Show warning
messagebox.showwarning('Warning', 'Warning box')


# Show error
messagebox.showerror('Error', 'Error box')


###############################################################################
# Question message boxes
###############################################################################


# Ask question
# * Returns 'yes' or 'no'
answer = messagebox.askquestion('Question', 'YES or NO question (return str)')
print(answer)
# yes


# Ask OK or CANCEL
# * Returns True or False
answer = messagebox.askokcancel('Question', 'OK or CANCEL question')
print(answer)
# True


# Ask RETRY or CANCEL
# * Returns True or False
answer = messagebox.askretrycancel('Question', 'RETRY or CANCEL question')
print(answer)
# True


# Ask YES or NO
# * Returns True or False
answer = messagebox.askyesno('Question', 'YES or NO question')
print(answer)
# True


# Ask YES, NO or CANCEL
# Returns True, False or None
answer = messagebox.askyesnocancel('Question', 'YES, NO or CANCEL question')
print(answer)
# True
