from pylab import *
import math
import random

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
    robot1 = Robot(0.0, 0.0, 0.0, 0.1, 5.0)

##    samples = multivariate_normal([2.0, 2.0], [[1, 0], [0, 1.0]], 1000)
##    angles = multivariate_normal([0.0], [5.0], 1000)
    
    rand = random.random()

    N = 1000
    Xc = np.zeros(N)
    Yc = np.zeros(N)

    for i in range(N):
        Xc[i] = robot1.x
        Yc[i] = robot1.y
##        robot1.Drive(random.uniform(0, 1.0))
##        robot1.Turn(random.uniform(0, 2*math.pi))
        robot1.Drive(1)
        robot1.Turn(0.5)


    fig = figure(1)
    ax = fig.add_subplot(111)
##    ax.set_xlim(0.0, 5.0)
##    ax.set_ylim(0.0, 5.0)
    ax.plot(Xc, Yc, 'b--.')
##    ax.plot(samples[:, 0], samples[:, 1], '.')
    show()

if __name__ == "__main__":
    main()
