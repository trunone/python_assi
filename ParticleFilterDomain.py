from pylab import *
import math
import random

squares = [np.zeros((5, 2)) for i in range(100)]

for i in range(len(squares)):
   squares[i][0][0] = i%10
   squares[i][0][1] = int(i/10)
   squares[i][1][0] = i%10
   squares[i][1][1] = int(i/10)+1
   squares[i][2][0] = i%10+1
   squares[i][2][1] = int(i/10)+1
   squares[i][3][0] = i%10+1
   squares[i][3][1] = int(i/10)
   squares[i][4][0] = i%10
   squares[i][4][1] = int(i/10)

N = 500
particles = np.zeros((N, 2))
for i in range(len(particles)):
    particles[i][0] = random.uniform(0, 10)
    particles[i][1] = random.uniform(0, 10)


fig, ax = plt.subplots()
plt.title("Particle Filter Domain")

for s in squares:
    plt.plot(s[:,0], s[:,1], "b-")

plt.plot(particles[:,0], particles[:,1], "r.")

ax.autoscale_view()
plt.show()
