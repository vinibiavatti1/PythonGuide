from matplotlib import pyplot
import math

s1 = []
s2 = []
c1 = []
c2 = []
t1 = []
t2 = []

x = -10.0
while x < 10.0:
    x = round(x, 2)
    y = math.sin(x)
    y2 = math.cos(x)
    y3 = math.tan(x)
    s1.append(x)
    s2.append(y)
    c1.append(x)
    c2.append(y2)
    t1.append(x)
    t2.append(y3)
    x += 0.1

fig = pyplot.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

pyplot.plot(s1, s2, label='sen')
pyplot.plot(c1, c2, label='cos')
pyplot.plot(t1, t2, label='tan')
pyplot.show()
