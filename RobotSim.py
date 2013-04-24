from pylab import *
import math
import random
from mpl_toolkits.mplot3d import Axes3D

def NormalizeAngle( angle ):
    while angle < 0:
        angle += 2*math.pi
    while angle >= 2*math.pi:
        angle -= 2*math.pi
    return angle

class Robot:
    def __init__( self, x, y, theta, varianceDrive, varianceTurn ):
        self.x = x
        self.y = y
        self.theta = theta
        self.varianceDrive = varianceDrive
        self.varianceTurn = varianceTurn

    def Drive( self, dist ):
        err = multivariate_normal([0.0, 0.0], [[self.varianceDrive, 0.0], [0.0, self.varianceDrive]])
        self.x += dist * cos( self.theta ) + err[0]
        self.y += dist * sin( self.theta ) + err[1]
        self.Turn(0.0)

    def Turn( self, angle ):
        err = normal(0.0, self.varianceTurn)
        self.theta = NormalizeAngle( self.theta + angle + err)

    def __repr__( self ):
        s = "{{ X: {0:3.3f} Y: {1:3.3f} Angle: {2:3.3f} }}".format( self.x, self.y, self.theta )
        return s

def main():
    degree = (45.0/180.0)*math.pi
    robot1 = Robot(0.0, 0.0, degree, 0.5, 0.5)

##    samples = multivariate_normal([2.0, 2.0], [[1, 0], [0, 1.0]], 1000)
##    angles = multivariate_normal([0.0], [5.0], 1000)

    #rand = random.random()

    N = 10000
    zR = 10.0
    #Xc = np.zeros(N)
    #Yc = np.zeros(N)
    X = np.arange(-1.0, zR, 1/zR)
    Y = np.arange(-1.0, zR, 1/zR)
    (X, Y) = np.meshgrid(X, Y)
    Z = np.zeros((len(X), len(Y)))

    for i in range(N):
        #Xc[i] = robot1.x
        #Yc[i] = robot1.y
##        robot1.Drive(random.uniform(0, 1.0))
##        robot1.Turn(random.uniform(0, 2*math.pi))
        robot1.Turn(0.0)
        robot1.Drive(2.0)
        x_ind = int((robot1.x+1.0) * zR)
        y_ind = int((robot1.y+1.0) * zR)
        if(x_ind > 0 and y_ind > 0 and x_ind < len(X) and y_ind < len(Y)):
            Z[x_ind][y_ind] += 1

        robot1.Turn(0.0)
        robot1.Drive(6.0)
        x_ind = int((robot1.x+1.0) * zR)
        y_ind = int((robot1.y+1.0) * zR)
        if(x_ind > 0 and y_ind > 0 and x_ind < len(X) and y_ind < len(Y)):
            Z[x_ind][y_ind] += 1

        robot1.x = 0.0
        robot1.y = 0.0
        robot1.theta = degree

    figure()
    cs = contour(X, Y, Z)

    fig = figure()
    #ax = fig.add_subplot()
    ax = Axes3D(fig)

##    ax.set_ylim(0.0, 5.0)
    #ax.plot(Xc, Yc, 'b--.')
    ax.plot_surface(X, Y, Z, rstride=2, cstride=2, cmap=cm.jet)
##    ax.plot(samples[:, 0], samples[:, 1], '.')
    show()

if __name__ == "__main__":
    main()
