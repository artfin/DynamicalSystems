# integrator 
from scipy.integrate import odeint
# fancy 3D plotting
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# defining constants
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

def Lorenz(state, t):
    # unpack the state vector
    x = state[0]
    y = state[1]
    z = state[2]
    
    # computing state derivatives
    x_derivative = sigma * (y - x)
    y_derivative = (rho - z) * x - y
    z_derivative = x * y - beta * z
    
    return [x_derivative, y_derivative, z_derivative]

t = np.arange(0.0, 30.0, 0.01)

init = [2.0, 3.0, 4.0]

state = odeint(Lorenz, init, t)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(state[:,0], state[:, 1], state[:, 2])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
