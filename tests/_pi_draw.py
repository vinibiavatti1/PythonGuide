import tkinter


WIDTH = 800
HEIGHT = 600
PI = '31415926535897932384626433832795028841971693993751058209749445923078' + \
    '164062862089986280348253421170679821480865132823066470938446095505822' + \
    '317253594081284811174502841027019385211055596446229489549303819644288' + \
    '109756659334461284756482337867831652712019091456485669234603486104543' + \
    '26648213393607260249141273'
INC = 20
RULES = {
    '0': lambda x, y: (x, y - INC),
    '1': lambda x, y: (x + INC, y - INC),
    '2': lambda x, y: (x + INC, y),
    '3': lambda x, y: (x + INC, y + INC),
    '4': lambda x, y: (x, y + INC),
    '5': lambda x, y: (x - INC, y + INC),
    '6': lambda x, y: (x - INC, y),
    '7': lambda x, y: (x - INC, y - INC),
    '8': lambda x, y: (x, y),
    '9': lambda x, y: (x, y),
}

tk = tkinter.Tk()
screen = tkinter.Canvas(tk, width=WIDTH, height=HEIGHT, bg='black')


x = 10
y = 10


for n in PI:
    x2, y2 = RULES[n](x, y)
    screen.create_line(x, y, x2, y2, fill='white', width=4)
    x, y = x2, y2


screen.pack()
tk.mainloop()
