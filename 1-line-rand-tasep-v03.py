import numpy as np
import matplotlib.pyplot as plt
from functions import *


L = 500
initial_filling_factor = 0.1

mc_step_no = 500000
therm_step_no = 5000
parameters_arr = np.array([
    [0.01, 0.7],
    [0.1, 0.7],
    [0.15, 0.7],
    [0.2, 0.7],
    [0.25, 0.7],
    [0.3, 0.7],
    [0.35, 0.7],
    [0.4, 0.7],
    [0.45, 0.7],
    [0.8, 0.6],
    [0.8, 0.45],
    [0.8, 0.4],
    [0.8, 0.35],
    [0.8, 0.3],
    [0.8, 0.25],
    [0.8, 0.2],
    [0.8, 0.15],
    [0.8, 0.1],
    [0.8, 0.01]
])


total_no_density_arr, av_current_arr = density_current_calculation(therm_step_no, mc_step_no, L, parameters_arr, initial_filling_factor)

# for i in range(len(parameters_arr)):
#     print(f"Run {i+1}----------- \nAlpha: {parameters_arr[i][0]} \nBeta: {parameters_arr[i][1]} \nAverage Number Density: {total_no_density_arr[i]} \nAverage Current: {av_current_arr[i]}")


plt.plot(total_no_density_arr, av_current_arr, marker='o')
plt.ylim(0, 0.3)
plt.xlim(0, 1)
plt.title(f"Current vs Particle Density")
plt.ylabel("Current ($J$)")
plt.xlabel("Particle Density ($\\rho$)")
plt.grid()
plt.show()