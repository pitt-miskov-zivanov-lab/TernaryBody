#General imports
import numpy as np

#Scipy specific imports
from scipy.stats import entropy


def r_squared(a,b):
    ybar = np.sum(a)/len(a)          
    ssreg = np.sum((b-ybar)**2)   
    sstot = np.sum((a - ybar)**2)    
    r_squared = 1 - (ssreg / sstot)
    return r_squared

    
def sum_sq_error(a,b):
    res = a - b
    ssq = np.sum(res**2)
    return ssq


def KL_div(a,b):
    res = entropy(a, b)
    return res


def calculate_errors(namer,booler,actual,sim):
    SSE = sum_sq_error(actual,sim)
    Rsq = r_squared(actual,sim)
    KLd = KL_div(actual,sim)
    if booler:
        results = 'Results for ' + str(namer) + ': \n'
        results = results + 'UNFIT SIMULATION \n'
        results = results + '     SSE = %1.3f \n' % SSE
        results = results + '     Rsq = %1.3f \n' % Rsq
        results = results + '     KLd = %1.3f \n \n' % KLd
    else:
        results = 'Results for ' + str(namer) + ': \n'
        results = results + 'FITTED SIMULATION \n'
        results = results + '     SSE = %1.3f \n' % SSE
        results = results + '     Rsq = %1.3f \n' % Rsq
        results = results + '     KLd = %1.3f \n \n' % KLd
    return results


def write_me_up(namer,actual,sim,fit,fitted,error,save=False):
    results1 = calculate_errors(namer,1,actual,sim)
    error_before = '{:1.2f}'.format(sum_sq_error(actual,sim))
    results2 = calculate_errors(namer,0,actual,fit)
    error_after = '{:1.2f}'.format(sum_sq_error(actual,fit))
    if save:
        file_name = namer + '.txt'
        file = open(file_name, "w") 
        file.write(results1) 
        file.write(results2)
        file.write('Fit = ' + str(fitted) + '\n')
        file.write('Error = ' + str(error)+ '\n')
        file.close()
    return error_before, error_after