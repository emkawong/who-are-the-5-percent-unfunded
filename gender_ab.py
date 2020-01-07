import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
plt.style.use('ggplot')


def plot_with_fill(x, y, label):
    lines = plt.plot(x, y, label=label, lw=2)
    plt.fill_between(x, 0, y, alpha=0.2, color=lines[0].get_c())

def get_pdf(x, result):
    ''' The function will return the pdf for a given beta distribution

    Parameters
    -----------
    x : Array of x values
    site : Array cooresponding to the site in question

    Returns
    --------
    numpy array
    '''
    alpha = result[result['GENDER_GROUPS'] == 'female']['LOAN_ID'].count()
    beta = result[(result['GENDER_GROUPS'] == 'female') | (result['GENDER_GROUPS'] == 'male')] - alpha
    
    return stats.beta(a=alpha, b=beta).pdf(x)