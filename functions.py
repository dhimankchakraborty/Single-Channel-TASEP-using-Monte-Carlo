import numpy as np
import numpy.random as rn
import matplotlib.pyplot as plt
from numba import jit, njit, prange


@njit
def initial_state_generator(L, initial_filling):
    state = np.zeros((L), dtype=np.uint8)

    filled_sites = np.uintc(np.round(L * initial_filling))

    filled_sites_arr = np.arange(0, L)
    rn.shuffle(filled_sites_arr)

    for i in prange(filled_sites):
        state[filled_sites_arr[i]] = 1
    
    return state


@njit
def thermalization_random_update(therm_step_no, L, state, alpha, beta):
    for i in prange(therm_step_no):
        for j in prange(L):
            selected_site = rn.randint(L)

            if selected_site == 0:

                if state[selected_site] == 0:
                    insert_rn = rn.rand()
                    if insert_rn <= alpha:
                        state[selected_site] = 1

                elif state[selected_site] == 1 and state[selected_site + 1] == 0:
                    state[selected_site] = 0
                    state[selected_site + 1] = 1
            
            elif selected_site == L - 1 and state[selected_site] == 1:

                exit_rn = rn.rand()
                if exit_rn <= beta:
                    state[selected_site] = 0
            
            else:
                if state[selected_site] == 1 and state[selected_site + 1] == 0:

                    state[selected_site] = 0
                    state[selected_site + 1] = 1
        
        # print(f'{i + 1} ---- {state} ---- {state.mean()}')

    return state


@njit
def simulation_random_update(mc_step_no, L, state, alpha, beta):
    total_no_density = 0
    site_av_no_density_arr = np.zeros((L))

    av_current = 0

    for i in prange(mc_step_no):
        for j in prange(L):
            selected_site = rn.randint(L)

            if selected_site == 0 and state[selected_site] == 0:
                    
                insert_rn = rn.rand()
                if insert_rn <= alpha:
                    state[selected_site] = 1
            
            elif selected_site == L - 1 and state[selected_site] == 1:

                exit_rn = rn.rand()
                if exit_rn <= beta:
                    state[selected_site] = 0
            
            elif state[selected_site] == 1 and state[selected_site + 1] == 0:

                    state[selected_site] = 0
                    state[selected_site + 1] = 1

                    av_current += 1 / (L - 1)
        
        if (i + 1) % 10 == 0:
            total_no_density += state.mean()
            site_av_no_density_arr += state

    return total_no_density * 10 / mc_step_no, site_av_no_density_arr * 10 / mc_step_no, av_current / mc_step_no


@njit
def density_current_calculation(therm_step_no, mc_step_no, L, parameters_arr, initial_filling_factor):
    total_no_density_arr = np.zeros((len(parameters_arr)))
    av_current_arr = np.zeros((len(parameters_arr)))

    for i, parameters in enumerate(parameters_arr):
        alpha = parameters[0]
        beta = parameters[1]

        state = initial_state_generator(L, initial_filling_factor)

        state = thermalization_random_update(therm_step_no, L, state, alpha, beta)

        total_no_density_arr[i], _, av_current_arr[i] = simulation_random_update(mc_step_no, L, state, alpha, beta)

        print(f"Run {i+1}")
    
    return total_no_density_arr, av_current_arr


