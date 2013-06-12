from pylab import *

def KalmanFilterPredict(motion, x_m, P_m, Q):
    (dx, dy) = motion
    xn = (x_m[0]+dx, x_m[1]+dy)
    Pn = P_m + Q
    return (xn, Pn)

def KalmanFilterCorrect(sensor, x_u, P_u, R):
    K = (P_u[1][1]/(P_u[0][0]+P_u[1][1]), P_u[0][0]/(P_u[0][0]+P_u[1][1]))
    diff = ((sensor[0]-x_u[0])*K[0], (sensor[1]-x_u[1])*K[1])
    xn = (x_u[0] + diff[0], x_u[1] + diff[1])
    Pn = P_u + R
    return (xn, Pn)

def main():
    Q = [[2.0, 0.0], [0.0, 2.0]]
    R = [[1.0, 0.0], [0.0, 1.0]]

    N = 5

    motion = np.zeros((N, 2))
    sensor = np.zeros((N, 2))
    kalman = np.zeros((N, 2))

    x_m = np.array([0.0, 0.0])

    A = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]

    P_m = np.zeros((2, 2))
    P_m[0][0] = Q[0][0]
    P_m[1][1] = Q[1][1]

    motion = np.array([[10.0, 0.0], [20.0, 0.0], [30.0, 0.0], [40.0, 0.0], [50.0, 0.0]])

    sensor  = np.array([[11.63030579, 1.69531229], [20.34811166, 0.62385913],
                        [31.32411393, -5.44629289], [40.83444465, -3.29843939],
                        [56.595500437, -3.08443923]])

    com = (10.0, 0.0)

    for i in range(N):
        (x_u, P_u) = KalmanFilterPredict(com, x_m, P_m, Q)
        print("Predicted state", x_u)
        print("Predicted Covariance", P_u)

        (x_m, P_m) = KalmanFilterCorrect((sensor[i][0], sensor[i][1]), x_u, P_u, R)
        print("Updated state", x_m)
        print("Updated Covariance", P_m)
        kalman[i][0] = x_m[0]
        kalman[i][1] = x_m[1]
        print("Variance:", P_m)

    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    ax.set_xlim(-1, 60)
    ax.set_ylim(-5, 5)
    ax.plot(motion[:, 0], motion[:, 1], "ro")
    ax.plot(sensor[:, 0], sensor[:, 1], "g*")
    ax.plot(kalman[:, 0], kalman[:, 1], "y.-")
    show()

if __name__ == "__main__":
    main()
