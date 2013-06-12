from pylab import *
import math
import random
from mpl_toolkits.mplot3d import Axes3D

def deg2rad(deg):
    return (deg/180.0)*math.pi

def NormalizeAngle( angle ):
    while angle < 0:
        angle += 2*math.pi
    while angle >= 2*math.pi:
        angle -= 2*math.pi
    return angle

class Robot:
    def __init__( self, initPos, varianceDrive, varianceTurn ):
        self.theta = initPos[2]
        self.Pos = [initPos[0], initPos[1]]
        self.varianceDrive = varianceDrive
        self.varianceTurn = varianceTurn

    def Drive( self, dist ):
        if self.varianceDrive:
            err = multivariate_normal([0.0, 0.0], self.varianceDrive)
        else:
            err = [0.0, 0.0]
        self.Pos[0] += dist * cos( self.theta ) + err[0]
        self.Pos[1] += dist * sin( self.theta ) + err[1]
        self.Turn(0.0)

    def Turn( self, angle ):
        if self.varianceTurn:
            err = normal(0.0, self.varianceTurn)
        else:
            err = 0
        self.theta = NormalizeAngle( self.theta + angle + err)

    def __repr__( self ):
        s = "{{ X: {0:3.3f} Y: {1:3.3f} Angle: {2:3.3f} }}".format( self.Pos[0], self.Pos[1], self.theta )
        return s

def main():
    initPos = (0.0, 0.0, deg2rad(0.0))
    motionVariance = [ [1.0, 0.0], [0.0, 1.0] ]
    sensorVariance = [ [3.0, 0.0], [0.0, 0.1] ]

    degree = deg2rad(45.0)
    robotIdeal = Robot(initPos, None, None)
    robot1 = Robot(initPos, motionVariance, None)

    N = 1000
    zR = 10.0
    X = np.arange(-1.0, zR, 1/zR)
    Y = np.arange(-1.0, zR, 1/zR)
    (X, Y) = np.meshgrid(X, Y)
    Z = np.zeros((len(X), len(Y)))

    for i in range(N):
        robot1.Turn(0.0)
        robot1.Drive(2.0)
        x_ind = int((robot1.Pos[0]+1.0) * zR)
        y_ind = int((robot1.Pos[1]+1.0) * zR)
        if(x_ind > 0 and y_ind > 0 and x_ind < len(X) and y_ind < len(Y)):
            Z[x_ind][y_ind] += 1

        robot1.Turn(0.0)
        robot1.Drive(6.0)
        x_ind = int((robot1.Pos[0]+1.0) * zR)
        y_ind = int((robot1.Pos[1]+1.0) * zR)
        if(x_ind > 0 and y_ind > 0 and x_ind < len(X) and y_ind < len(Y)):
            Z[x_ind][y_ind] += 1

        robot1.Pos[0] = 0.0
        robot1.Pos[1] = 0.0
        robot1.theta = degree

    fig = figure()
    cs = contour(X, Y, Z)
    #ax = Axes3D(fig)
    #ax.plot_surface(X, Y, Z, rstride=2, cstride=2, cmap=cm.jet)
    show()

if __name__ == "__main__":
    main()
