"""
TTk (Themed TkInter)

* The Themed TkInter is a submodule of Tkinter that provides a more modern and
  visually appealing set of widgets.
* It allows for easier styling and theming of widgets, making it simpler to
  create visually attractive applications.
* The style of the ttk widgets follows the native look and feel of the
  operating system.
* While ttk provides a more modern appearance, we can always mix ttk and
  classic widgets in the same application.
* It is always recommended to use ttk widgets when possible, as they provide
  a more consistent and visually appealing look.
"""


###############################################################################
# Module Import
###############################################################################


# Tk and TTk import
# * We will import the tkinter main module, and the ttk submodule to use the
#   themed widgets.
# * Usually, the alias "tk" is used to reference the main module, and "ttk"
#   is used for the themed submodule.
import tkinter as tk
import tkinter.ttk as ttk


###############################################################################
# Widgets Difference
###############################################################################


# Root Window
# * We will create a root window normally, and set some properties.
root = tk.Tk()
root.title("Tk vs TTk")


# Tk Button
# * A classic Tk button will be added to the root window.
button_old = tk.Button(root, text="Tk (Classic)")
button_old.pack()


# Ttk Button
# * A modern Ttk button will be also added to the root window.
button_new = ttk.Button(root, text="Ttk (Modern)")
button_new.pack()


# Main loop
# * Now, take a look the appearance of the buttons.
# * Note that the classic button has a more traditional look, while the Ttk
#   button appears more modern (follows the native look and feel of the OS).
root.mainloop()


###############################################################################
# Ttk Themes
###############################################################################


# Root Window
# * We will create another root window for the Ttk theme demonstration.
root = tk.Tk()
root.title("Ttk Theme Demo")


# Defining a theme
# * Ttk also provides a way to define custom themes.
# * You can create a new theme by subclassing the existing ones and overriding
#   the desired options.
# * You can also use pre-defined themes as a base for your custom theme.
# * The code below creates a theme object, and prints all available themes.
style = ttk.Style()
print(style.theme_names())
# ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')


# Changing the theme
# * You can change the theme at any time using the theme_use() function.
# * The code below changes the theme to 'clam'.
# * Now, the ttk widgets will use the 'clam' theme.
style.theme_use('clam')


# Creating a new button after changing the theme
# * The code below creates a new Ttk button after changing the theme.
button_new = ttk.Button(root, text="Ttk (Modern)")
button_new.pack()


# Main loop
# * Look that the Ttk button has a 'clam' style.
root.mainloop()
