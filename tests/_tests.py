from matplotlib import pyplot

x = [i for i in range(1, 30)]
y = [len(str(i / 3)) for i in range(1, 30)]
pyplot.plot(x, y, label='val')


pyplot.legend()
pyplot.show()
"""
2.0
2.2222222222222223
2.5
2.857142857142857
3.3333333333333335
4.0
5.0
6.666666666666667
10.0
20.0
"""
