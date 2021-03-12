"""
Format function

* Check the link for more information: https://docs.python.org/3/library/string
                                       .html#format-specification-mini-language
* Returns a formatted representation of the given value controlled by the
  format specifier
* Calls __format__ method from class
* Syntax
  * format(value[, format_spec])

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

TODO
"""
