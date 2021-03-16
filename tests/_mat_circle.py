from matplotlib import pyplot
import math


def plot(x_points, y_points, g_points):
    fig = pyplot.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    pyplot.axis('equal')
    pyplot.xticks([a for a in range(-20, 20, 2)])
    pyplot.yticks([a for a in range(-20, 20, 2)])

    #pyplot.plot(x_points, y_points, label='f')
    pyplot.plot(x_points, g_points, label='g')
    pyplot.show()


x_points = []
y_points = []
g_points = []

r = 10
c1 = 10
c2 = 10


start = -10
stop = 10
step = 0.1


i = start
while i < stop:
    x_points.append(i)
    i += step


for x in x_points:
    y1 = c2 + math.sqrt(-(x - c1) ** 2 + r ** 2)
    y2 = c2 - math.sqrt(-(x - c1) ** 2 + r ** 2)
    y_points.append(y1)
    g_points.append(y2)


plot(x_points, y_points, g_points)
