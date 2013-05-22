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

def KalmanFilterPredict(motion, x_m, P_m, Q):
    (d,t) = motion
    nt = NormalizeAngle(t + x_m[2])
    dx = d*math.cos(nt)
    dy = d*math.sin(nt)
    xn = [ x_m[0]+dx, x_m[1]+dy, nt ]
    Pn = P_m + Q
    return (xn, Pn)

def KalmanFilterCorrect(sensor, x_u, P_u, R):
    K = P_u/(P_u + R)
    diff = (sensor[0]-x_u[0], sensor[1]-x_u[1])
    nd = (d[0]+x_m[0], d[1]+x_m[1])
    P = P_m + Q
    return (nd, nt), P

def KalmanFilterCorrect(sensor, x_u, P_u, sensorVariance):
    K = P_u/(P_u + sensorVariance)
    diff = (sensor[0]-x_u[0], sensor[1]-x_u[1])


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
    motionVariance = [ [2.0, 0.0], [0.0, 5.0] ]
    sensorVariance = [ [3.0, 0.0], [0.0, 0.1] ]

    degree = deg2rad(45.0)
    robotIdeal = Robot(initPos, None, None)
    robot1 = Robot(initPos, motionVariance, None)

    N = 50
    #zR = 10.0
    pos = np.zeros((N, 2))
    pos_ideal = np.zeros((N, 2))
    pos_sensor = np.zeros((N, 2))
    pos_kalman = np.zeros((N, 2))
    #X = np.arange(-1.0, zR, 1/zR)
    #Y = np.arange(-1.0, zR, 1/zR)
    #(X, Y) = np.meshgrid(X, Y)
    #Z = np.zeros((len(X), len(Y)))

    drive_count = 10

    for i in range(N):
        #robot1.Turn(0.0)
        #robot1.Drive(2.0)
        #x_ind = int((robot1.x+1.0) * zR)
        #y_ind = int((robot1.y+1.0) * zR)
        #if(x_ind > 0 and y_ind > 0 and x_ind < len(X) and y_ind < len(Y)):
        #    Z[x_ind][y_ind] += 1

        #robot1.Turn(0.0)
        #robot1.Drive(6.0)
        #x_ind = int((robot1.x+1.0) * zR)
        #y_ind = int((robot1.y+1.0) * zR)
        #if(x_ind > 0 and y_ind > 0 and x_ind < len(X) and y_ind < len(Y)):
        #    Z[x_ind][y_ind] += 1

        #robot1.x = 0.0
        #robot1.y = 0.0
        #robot1.theta = degree

        pos[i] = robot1.Pos
        pos_ideal[i] = robotIdeal.Pos
        err = multivariate_normal([0.0, 0.0], sensorVariance)
        pos_sensor[i] = [pos[i][0] + err[0], pos[i][1] + err[0]]

        robot1.Drive(drive_count)
        robot1.Turn(degree)
        robotIdeal.Drive(drive_count)
        robotIdeal.Turn(degree)

        drive_count += 0.3

    #figure()
    #cs = contour(X, Y, Z)

    fig = figure()
    ax = fig.add_subplot(111)
    #ax = Axes3D(fig)

    #ax.set_xlim(0.0, 5.0)
    #ax.set_ylim(0.0, 5.0)
    ax.plot(pos[:,0], pos[:,1], 'bo-')
    ax.plot(pos_ideal[:,0], pos_ideal[:,1], 'ro-')
    ax.plot(pos_sensor[:,0], pos_sensor[:,1], 'go-')
    ax.plot(pos_kalman[:,0], pos_kalman[:,1], 'yo-')
    #ax.plot_surface(X, Y, Z, rstride=2, cstride=2, cmap=cm.jet)
    show()

if __name__ == "__main__":
    main()
