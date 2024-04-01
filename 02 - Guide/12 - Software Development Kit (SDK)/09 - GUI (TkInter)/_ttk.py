"""
TTK (Themed TKInter)

* Starting with Tk 8.5, the ttk module became available. This module replaces
  much (but not all) of the original Tkinter machinery. Use this module to gain
  these advantages:
  * Platform-specific appearance. In releases before Tk 8.5, one of the
    commonest complaints about Tk applications was that they did not conform to
    the style of the various platforms
  * The ttk module allows you to write your application in a generic way, yet
    your application can look like a Windows application under Windows, like a
    MacOS app under MacOS, and so on, without any change to your program
  * Each possible different appearance is represented by a named ttk theme. For
    example, the classic theme gives you the appearance of the original Tkinter
    widgets described in the previous sections
  * Simplification and generalization of state-specific widget behavior. In the
    basic Tkinter world, there are a lot of widget options that specify how the
    widget should look or behave depending on various conditions, but in tkk,
    the options were minimized using states, etc.
"""


###############################################################################
# Importation
###############################################################################


# TTK
# * To follow the best concepts, you can import tkinter like this
from tkinter import ttk


# TK
# * Standart Tkinter must be imported too, cause some resource will be used
#   from this package
import tkinter as tk


# Diaglos
# * The dialogs must be import separatelly
from tkinter import messagebox


###############################################################################
# Themes
###############################################################################


# Check themes
# * TTK has by default some themes
# * To check the available themes you can check the list inside the Style class
window = tk.Tk()
style = ttk.Style(window)
print(style.theme_names())
# ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')


# Define theme
# * To define the theme to use, you can call the theme_use() function
style.theme_use('xpnative')
