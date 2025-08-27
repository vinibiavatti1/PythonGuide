"""
Progress Bar (TTK)

* The Progress Bar widget (TTK) is used to indicate the progress of a
  long-running operation.
* It can be used in two modes: determinate and indeterminate.
* In determinate mode, the progress bar shows the exact progress of the
  operation.
* In indeterminate mode, the progress bar shows that an operation is ongoing
  without indicating how much progress has been made.
* The progress bar can be customized in terms of its appearance and behavior.
"""


###############################################################################
# Import
###############################################################################


# Import
# * We will import tkinter to be used on the examples below.
import tkinter as tk
import tkinter.ttk as ttk


###############################################################################
# Example
###############################################################################


# Example
# * The example below creates a simple GUI application with the widget.
root = tk.Tk()
root.geometry('400x300')
progress_bar = ttk.Progressbar(
    master=root,
    mode='determinate'
)
progress_bar.pack(fill=tk.X, padx=20, pady=20)
progress_bar.start(100)
root.mainloop()


###############################################################################
# Parameters & Methods
###############################################################################


# Keys
# * The `keys` method shows all parameters for the widget creation.
progress_bar = ttk.Progressbar()
[print(k) for k in progress_bar.keys()]
"""
orient
length
mode
maximum
variable
value
phase
takefocus
cursor
style
class
"""


# Methods
# * The common methods for the widget are:
"""
start([interval])
step([delta])
stop()
"""
