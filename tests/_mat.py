from matplotlib import pyplot
import math


def plot(x_points, y_points):
    fig = pyplot.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    print(f'Minimo X: {x_min}')
    print(f'Minimo Y: {y_min}')

    pyplot.plot(x_points, y_points, label='vals')
    pyplot.show()


x_points = []
y_points = []

start = -10
end = 10
step = 0.1
a = -2
b = 0
c = 3

x_min = None
y_min = None

x = start
while x < end:
    y = a * (x ** 2) + b * x + c
    x_points.append(x)
    y_points.append(y)
    if x_min is None or y < y_min:
        x_min = x
        y_min = y
    x += step

plot(x_points, y_points)
