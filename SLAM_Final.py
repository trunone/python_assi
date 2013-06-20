##!/bin/env python3
from pylab import *
import math
limit = 3
count = 1
positions = np.zeros((1 + 5**limit, 2))

def VanKochLine(pos, line, lim, lv = 0):
    global count
    sx = line[0][0]
    sy = line[0][1]
    ex = line[1][0]
    ey = line[1][1]
    dx = 0.33*(ex - sx)
    dy = 0.33*(ey - sy)
    if(lv >= lim):
        pos[count][0] = ex
        pos[count][1] = ey
        count = count + 1
    else:
        VanKochLine(pos, [[sx, sy], [sx+dx, sy+dy]], lim, lv+1)
        VanKochLine(pos, [[sx+dx, sy+dy], [sx+dx-dy, sy+dy+dx]], lim, lv+1)
        VanKochLine(pos, [[sx+dx-dy, sy+dy+dx], [sx+2*dx-dy, sy+2*dy+dx]], lim, lv+1)
        VanKochLine(pos, [[sx+2*dx-dy, sy+2*dy+dx], [sx+2*dx, sy+2*dy]], lim, lv+1)
        VanKochLine(pos, [[sx+2*dx, sy+2*dy], [sx+3*dx, sy+3*dy]], lim, lv+1)

positions[0][0] = 0.0
positions[0][1] = 0.0
VanKochLine(positions, [[0.0, 0.0], [8.0, 0.0]], limit)
print(positions)
fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.set_xlim(-1.0, 10.0)
ax.set_ylim(-1.0, 10.0)
ax.plot(positions[:,0], positions[:,1], 'b-')
show()

