import numpy as np
import numpy.random as rn
import matplotlib.pyplot as plt
from functions import *


L = 500
initial_filling_factor = 0.1
alpha = 0.2
beta = 0.7

mc_step_no = 500000
therm_step_no = mc_step_no
steps_skip = 10

state = initial_state_generator(L, initial_filling_factor)

state = thermalization_random_update(therm_step_no, L, state, alpha, beta)

total_no_density, site_av_no_density_arr = simulation_random_update(mc_step_no, L, state, alpha, beta)

site_pos = np.arange(0, L)

plt.plot(site_pos, site_av_no_density_arr, label=f"Average Particle Density: {np.around(total_no_density, decimals=3)}")
plt.ylim(0, 1)
plt.title(f"Particle Density vs Site Number \n $\\alpha$: {alpha} & $\\beta$: {beta} \n Monte-Carlo Step: {mc_step_no}")
plt.xlabel("Site Number")
plt.ylabel("Particle Density")
plt.legend()
plt.grid()
plt.show()
