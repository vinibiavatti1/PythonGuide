"""
PDB (Python Debugger)

* The module pdb defines an interactive source code debugger for Python
  programs. It supports setting (conditional) breakpoints and single stepping
  at the source line level, inspection of stack frames, source code listing,
  and evaluation of arbitrary Python code in the context of any stack frame.
  It also supports post-mortem debugging and can be called under program
  control
* To define breakpoints the module doens't need to be imported anymore since
  Python 3.7. This version brought a builtin method called breakpoint()
* The IDE knows how to use the module to make the interaction debug with the
  developer
* The PDB has some commands to interact with debugger. These commands are used
  in breakpoints (set_trace()).
* Reference: https://docs.python.org/3/library/pdb.html

###############################################################################
Command                 Description
###############################################################################

!                       Execute the (one-line) statement in the context of the
                        current stack frame. The exclamation point can be
                        omitted unless the first word of the statement
                        resembles a debugger command

alias:                  Create an alias called name that executes command. The
                        command must not be enclosed in quotes. Replaceable
                        parameters can be indicated by %1, %2, and so on, while
                        %* is replaced by all the parameters. If no command is
                        given, the current alias for name is shown. If no
                        arguments are given, all aliases are listed

a(rgs):                 Print the argument list of the current function

b(reak):                With a lineno argument, set a break there in the
                        current file. With a function argument, set a break at
                        the first executable statement within that function.
                        The line number may be prefixed with a filename and a
                        colon, to specify a breakpoint in another file
                        (probably one that hasn't been loaded yet)

cl(ear):                With a filename:lineno argument, clear all the
                        breakpoints at this line. With a space separated list
                        of breakpoint numbers, clear those breakpoints. Without
                        argument, clear all breaks (but first ask confirmation)

commands:               Specify a list of commands for breakpoint number
                        bpnumber. The commands themselves appear on the
                        following lines. Type a line containing just end to
                        terminate the commands

condition:              Set a new condition for the breakpoint, an expression
                        which must evaluate to true before the breakpoint is
                        honored. If condition is absent, any existing condition
                        is removed; i.e., the breakpoint is made unconditional

c(ont(inue)):           Continue execution, only stop when a breakpoint is
                        encountered

debug:                  Enter a recursive debugger that steps through the code
                        argument (which is an arbitrary expression or statement
                        to be executed in the current environment)

disable:                Disable the breakpoints given as a space separated list
                        of breakpoint numbers. Disabling a breakpoint means it
                        cannot cause the program to stop execution, but unlike
                        clearing a breakpoint, it remains in the list of
                        breakpoints and can be (re-)enabled

display:                Display the value of the expression if it changed, each
                        time execution stops in the current frame. Without
                        expression, list all display expressions for the
                        current frame

d(own):                 Move the current frame count (default one) levels down
                        in the stack trace (to a newer frame)

enable:                 Enable the breakpoints specified

h(elp):                 Without argument, print the list of available commands.
                        With a command as argument, print help about that
                        command

ignore:                 Set the ignore count for the given breakpoint number.
                        If count is omitted, the ignore count is set to 0. A
                        breakpoint becomes active when the ignore count is
                        zero. When non-zero, the count is decremented each time
                        the breakpoint is reached and the breakpoint is not
                        disabled and any associated condition evaluates to true

interact:               Start an interactive interpreter (using the code
                        module) whose global namespace contains all the (global
                        and local) names found in the current scope

j(ump):                 Set the next line that will be executed. Only available
                        in the bottom-most frame. This lets you jump back and
                        execute code again, or jump forward to skip code that
                        you don't want to run

l(ist):                 List source code for the current file

ll:                     List all source code for the current function or frame.
                        Interesting lines are marked as for list

n(ext):                 Continue execution until the next line in the current
                        function is reached or it returns

p:                      Evaluate the expression in the current context and
                        print its value

pp:                     Like the p command, except the value of the expression
                        is pretty-printed using the pprint module

q(uit):                 Quit from the debugger. The program being executed is
                        aborted

restart:                Restart the debugged Python program

r(eturn):               Continue execution until the current function returns

retval:                 Print the return value for the last return of a
                        function

source:                 Try to get source code for the given object and display
                        it

s(tep):                 Execute the current line, stop at the first possible
                        occasion (either in a function that is called or on the
                        next line in the current function)

tbreak:                 Temporary breakpoint, which is removed automatically
                        when it is first hit. The arguments are the same as for
                        break

unalias:                Delete the specified alias

undisplay:              Do not display the expression any more in the current
                        frame. Without expression, clear all display
                        expressions for the current frame

unt(il):                Without argument, continue execution until the line
                        with a number greater than the current one is reached.
                        With a line number, continue execution until a line
                        with a number greater or equal to that is reached.
                        In both cases, also stop when the current frame returns

u(p):                   Move the current frame count (default one) levels up in
                        the stack trace (to an older frame)

whatis:                 Print the type of the expression

w(here):                Print a stack trace, with the most recent frame at the
                        bottom. An arrow indicates the current frame, which
                        determines the context of most commands

###############################################################################
"""


###############################################################################
# Module
###############################################################################


# Importing the module
# * We will import the module
import pdb


# Make breakpoint using builtin function
# * The `breakpoint()` function is a builtin function that will call the PDB
#   debugger
x = 1
breakpoint()  # will wait for commands...
x += 1
print(x)
# 2
