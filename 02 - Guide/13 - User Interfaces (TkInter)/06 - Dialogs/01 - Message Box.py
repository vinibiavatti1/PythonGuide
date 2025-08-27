"""
Message Box

* Message box are used to display information to the user or prompt for
  confirmation.
* It can be modal or modeless.
* To use message boxes, you must import the `messagebox` module from `tkinter`.
"""


###############################################################################
# Import
###############################################################################


# Import
# * We will import tkinter to be used on the examples below.
from tkinter import messagebox


###############################################################################
# Message Boxes
###############################################################################


# Information Box
# * The `showinfo` function is used to display an informational message box.
messagebox.showinfo('Information', 'Lorem ipsum dolor sit amet.')


# Warning Box
# * The `showwarning` function is used to display a warning message box.
messagebox.showwarning('Warning', 'Lorem ipsum dolor sit amet.')


# Error Box
# * The `showerror` function is used to display an error message box.
messagebox.showerror('Error', 'Lorem ipsum dolor sit amet.')


###############################################################################
# Confirmation Prompts
###############################################################################


# Confirmation (YES or NO)
# * Used to ask a yes or no question.
# * Returns a string with the answer ('yes' or 'no').
x = messagebox.askquestion('Question', 'YES or NO question (return str)')
print(x)
# yes


# Confirmation (OK or CANCEL)
# * Used to ask a question with OK and CANCEL options.
# * Returns True if the user selects OK.
x = messagebox.askokcancel('Question', 'OK or CANCEL question')
print(x)
# True


# Confirmation (RETRY or CANCEL)
# * Used to ask a question with RETRY and CANCEL options.
# * Returns True if the user selects RETRY.
x = messagebox.askretrycancel('Question', 'RETRY or CANCEL question')
print(x)
# True


# Confirmation (YES or NO)
# * Used to ask a yes or no question.
# * The difference with askquestion is that this returns True or False.
# * Returns True if the user selects YES.
x = messagebox.askyesno('Question', 'YES or NO question')
print(x)
# True


# Confirmation (YES, NO or CANCEL)
# * Used to ask a yes, no or cancel question.
# * Returns True if the user selects YES, False if NO and None if CANCEL.
x = messagebox.askyesnocancel('Question', 'YES, NO or CANCEL question')
print(x)
# True
