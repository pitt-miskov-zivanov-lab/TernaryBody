#General imports
import random
import numpy as np

#Scipy specific imports
from scipy.stats import entropy

    
def sum_sq_error(a,b):
    #calculates the sum of squared errors (SSE) for two arrays a and b
    res = a - b
    ssq = np.sum(res**2)
    return ssq


def random_initialization():
    #creates a list of 5 random coefficients 
    # to be used as initial values for optimization (no longer in use)
    random_start_coefficients = []
    while len(random_start_coefficients) < 5:
        init_coef = round(random.random(),1)
        if init_coef < 0.1: continue
        else: random_start_coefficients.append(init_coef)

    return random_start_coefficients


def write_me_up(namer,actual,sim,fit,fitted,error,save=False):
    #Calculates the error before and after optimization
    error_before = '{:1.2f}'.format(sum_sq_error(actual,sim))
    error_after = '{:1.2f}'.format(sum_sq_error(actual,fit))
    if save:
        file_name = namer + '.txt'
        file = open(file_name, "w") 
        file.write('Fit = ' + str(fitted) + '\n')
        file.write('Error = ' + str(error)+ '\n')
        file.write('Error before (SSE) = ' + str(error_before) + '\n')
        file.write('Error after (SSE) = ' + str(error_after) + '\n')
        file.close()
    return error_before, error_after