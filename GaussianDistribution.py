from pylab import *
import math
from mpl_toolkits.mplot3d import Axes3D

def GaussianDistribution(x, mu, sigma2):
    return (1.0/(math.sqrt(sigma2) * math.sqrt(2*math.pi))) * \
           math.exp((-(x-mu)**2)/(2*sigma2))

def Gaussian2D( x, mu, sigma2 ):
    d1 = math.sqrt( 2*math.pi * sigma2[0] )
    d2 = math.sqrt( 2*math.pi * sigma2[1] )
    s1 = ( x[0] - mu[0] )**2 / (2*sigma2[0])
    s2 = ( x[1] - mu[1] )**2 / (2*sigma2[1])
    return 1.0 / (d1 * d2) * math.exp( -(s1 + s2) )

def main():

    X = []
    Y = []
    Z = []
    bound = 10

##X.append(np.arange(-bound, bound, 0.1))
##Y.append(np.zeros(len(X[0])))
##
##X.append(np.arange(-bound, bound, 0.1))
##Y.append(np.zeros(len(X[0])))
##
##X.append(np.arange(-bound, bound, 0.1))
##Y.append(np.zeros(len(X[0])))

##for i in range(len(Y[0])):
##    Y[0][i] = GaussianDistribution(X[0][i], 0., 1.)
##
##for i in range(len(Y[0])):
##    Y[1][i] = GaussianDistribution(X[1][i], 1., 4.)
##
##for i in range(len(Y[0])):
##    Y[2][i] = GaussianDistribution(X[2][i], 1.5, 0.3)

    X.append(np.arange(-bound, bound, 0.1))
    Y.append(np.arange(-bound, bound, 0.1))
    (X[0], Y[0]) = np.meshgrid(X[0], Y[0])
    Z.append(np.zeros((len(X[0]), len(Y[0]))))

    for i in range(len(X[0])):
        for j in range(len(Y[0])):
            Z[0][i][j] = Gaussian2D([X[0][i][j], Y[0][i][j]], [3, 4], [1, 0.2])

    fig = figure()
    ax = Axes3D(fig)
##ax = fig.add_subplot(111)

    ax.plot_surface(X[0], Y[0], Z[0], rstride=2, cstride=2, cmap=cm.jet)
##ax.plot(X[0], Y[0], 'r-')
##ax.plot(X[1], Y[1], 'g-')
##ax.plot(X[2], Y[2], 'b-')

    show()

if __name__ == "__main__":
    main()
