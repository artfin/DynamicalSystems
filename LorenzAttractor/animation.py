# integrator 
from scipy.integrate import odeint
# fancy 3D plotting
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
# specifying path to ffmpeg
plt.rcParams['animation.ffmpeg_path'] = u'/usr/bin/ffmpeg'

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

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

trace_length = 30

def animate(i):
    i += 1500
    ax.clear()
    ax.plot(state1[:,0], state1[:,1], state1[:,2], alpha=0.2)
    
    # tracing
    ax.plot(state1[(i-trace_length):i,0], state1[(i-trace_length):i,1], state1[(i-trace_length):i,2], 'blue', alpha=0.3)
    ax.plot(state2[(i-trace_length) : i,0], state2[(i-trace_length):i,1], state2[(i-trace_length):i,2], 'red', alpha=0.3)

    ax.plot(np.array([state1[i,0]]), state1[i,1], state1[i,2], 'b.', markersize=10)
    ax.plot(np.array([state2[i,0]]), state2[i,1], state2[i,2], 'r.', markersize=10)

t = np.arange(0.0, 30.0, 0.01)

# rerun simulation with very small change in initial conditions
delta = 1e-4
init1 = [2.0, 3.0, 4.0]
init2 = [2.0 + delta, 3.0, 4.0]

state1 = odeint(Lorenz, init1, t)
state2 = odeint(Lorenz, init2, t)

ani = animation.FuncAnimation(fig, animate, interval = 1)
#ani.save('lorenz.mpeg', writer='ffmpeg', extra_args=['-vcodec', 'libx264'], fps = 15, bitrate=-1)

plt.show()
