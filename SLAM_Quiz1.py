from pylab import *

X1 = [ 0, 5, -5, 0 ]
Y1 = [ 7, 4, 4, 7]

X2 = [ -5, 5 , 5, -5, -5]
Y2 = [ 4, 4, -5, -5, 4]

X3 = [ -3, -1, -1, -3, -3]
Y3 = [ 3, 3, 1, 1, 3]

X4 = [ 0, 2, 2, 0, 0]
Y4 = [ 1, 1, -5, -5, 1]

fig = figure(1)
ax = fig.add_subplot(111)

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

ax.plot(X1, Y1, 'b-')
ax.plot(X2, Y2, 'r-')
ax.plot(X3, Y3, 'g-')
ax.plot(X4, Y4, 'g-')

show()
