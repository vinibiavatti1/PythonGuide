"""
Operators precedence

* Python doc: https://docs.python.org/3/reference/expressions.html#operator-pre
              cedence

###############################################################################
Priority	    Operator	    Description            Example
###############################################################################
1.              (expr)          expression             (1 + 2)
-               [list]          list display           [1, 2]
-               {key:v}         dict display           {'k': v}
-               {set}           set display            {1, 2}
2.              x[y]            subscription           x[1]
-               x[y:z]          slicing                x[2:3]
-               fn(args)        call                   fn(x, y)
-               x.y             attr ref               obj.x
3.              await x         await expr             await x
4.              **              exponentiation         2 ** 3
5.              +x              positive               +5
-               -x              negative               -5
-               ~x              bitwise not            ~5
6.              *               multiplication         2 * 3
-               @               matrix multip.         a @ b
-               /               division               10 / 5
-               //              floor div.             7 // 8
-               %               remainder              5 % 3
7.              +               add                    1 + 2
-               -               sub                    5 - 3
8.              <<              bitwise lshift         16 << 1
-               >>              bitwise rshift         32 >> 1
9.              &               bitwise and            10 & 5
10.             ^               bitwise xor            10 ^ 5
11.             |               bitwise or             10 | 5
12.             in              membership             x in z
-               not in          membership             x not in z
-               is              identity               x is z
-               is not          identity               x is not z
-               <               comparison             5 < 10
-               <=              comparison             5 <= 10
-               >               comparison             5 > 10
-               >=              comparison             5 >= 10
-               !=              comparison             5 != 10
-               ==              comparison             5 == 10
13.             not x           bool not               not True
14.             and             bool and               x and y
15.             or              bool or                x or y
16.             if-else         condition              if x == 1:
17.             lambda          lambda expr            lambda x: x * x
18.             :=              assignment exp         3 += 1
###############################################################################
"""


# Expression 1
x = 3 + 5 * 2
print(x)
# 13


# Expression 2
x = 2 ** 2 / 4 * 1
print(x)
# 1.0


# Expression 3
x = 1 - 3 * -4 // -5.
print(x)
# -1.0


# Expression 4
x = -2 ** 3
print(x)
# 256


# Right sided binding (**)
# NOTE: Important!
print(2 ** 2 ** 3)
# It is calculed as 2 ** (2 ** 3)
# 256
