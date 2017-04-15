from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# alpha is the natural growth rate of prey in the absence of predation
# beta is the (natural) death rate of prey 
# sigma -- (related to) growth rate of predators
# gamss - natural death rate of predators

alpha = 0.1
beta = 0.1
sigma = 0.1
gamma = 0.1

def simulation(state, t):
    x = state[0]
    y = state[1]
    
    x_derivative = x * (alpha - beta * y)
    y_derivative = - y * (gamma - sigma * x)

    return [x_derivative, y_derivative]

t = np.arange(0, 500, 1)

init = [0.5, 0.5]
state = odeint(simulation, init, t)

fig = plt.figure()
ax = fig.gca()

ax.set_xlabel('Time')
ax.set_ylabel('Population')

ax.set_title('Lotka-Volterra equation')

ax.set_ylim([0, 8])

plt.plot(t, state)

red_patch = mpatches.Patch(color = 'blue', label = 'prey')
green_patch = mpatches.Patch(color = 'orange', label = 'predator')
plt.legend(handles = [red_patch, green_patch])

plt.show()

