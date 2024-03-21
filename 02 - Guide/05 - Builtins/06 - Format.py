"""
Format

* The `format()` method returns a formatted value based on the specified
  formatter
* It calls the `__format__` method from the Format Protocol
* Syntax: format(value, format_spec = '')

###############################################################################
Format tokens
###############################################################################
format_spec:     [[fill]align][sign][#][0][width][grouping_option][.precision]
                 [type]
fill:            <any character>
align:           "<" | ">" | "=" | "^"
sign:            "+" | "-" | " "
width:           digit+
grouping_option: "_" | ","
precision:       digit+
type:            "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" |
                 "o" | "s" | "x" | "X" | "%"
###############################################################################
"""


###############################################################################
# Format Examples
###############################################################################


# Formating an integer to binary
# * We can format a integer value to a binary representation
x = 13
y = format(x, 'b')
print(y)
# 1101


# Formating a float with precision
# * We can format a float value with a specific precision
x = 3.141592653589793
y = format(x, '.2f')
print(y)
# 3.14


# Formating a float as a percentage
# * We can format a float value as a percentage value
x = 0.25
y = format(x, '%')
print(y)
# 25.000000%
