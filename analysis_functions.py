import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
plt.style.use('ggplot')


def get_funded_df(df,column_to_explore):
    '''
    Takes the Kiva loan df and creates a new df that pivots on the desired column to explore and takes the count between 
    expired and funded loans. Then creates,removes,renames columns so that the df only contains the category values as 
    rows names and funded/unfunded/total as columns headers. 
    '''
    pivot = df.pivot_table(values = 'LOAN_ID', index = column_to_explore, columns = 'STATUS', aggfunc = 'count')
    pivot['FUNDED'] = pivot['funded']
    pivot['UNFUNDED'] = pivot['expired']
    pivot['TOTAL'] = pivot['expired']+ pivot['funded']
    pivot = pivot.drop(['fundRaising','refunded','expired','funded'],axis=1)
    
    return pivot

def beta_distributions(df,x):
    
    '''
    Takes the funded DataFrame and returns a dict that contains the beta probability density function for 
    total amount of funded and unfunded loans based on each variable
    '''

    beta_functions = {}

    for row in df.reset_index().iloc[:,0]:
        alpha = df.loc[row,'FUNDED']
        beta = df.loc[row,'UNFUNDED']
        beta_functions[row] = stats.beta(alpha,beta).pdf(x)
        
    return beta_functions

def beta_rvs(df,samples):
    
    '''
    Takes the funded DataFrame and returns a dict that contains random samples based on the beta distribution for 
    total amount of funded and unfunded loans based on each variable
    '''

    beta_rvs = {}

    for row in df.reset_index().iloc[:,0]:
        alpha = df.loc[row,'FUNDED']
        beta = df.loc[row,'UNFUNDED']
        beta_rvs[row] = stats.beta(alpha,beta).rvs(samples)
        
    return beta_rvs

def graph_beta(function_dict,x,ax):

    for label,function in function_dict.items(): 
        plot_with_fill(x,function,label)
        ax.annotate(label,rotation=0,xy=((function.argmax()/10000),function.max()),
                    xytext=((function.argmax()/10000)+0.003,(function.max())+50),
                    arrowprops=dict(arrowstyle="simple",fc="0.5", ec="none",connectionstyle="arc3,rad=0.3"))
        ax.annotate('Average Funded Rate',xy=(0.954122810959807,1600),xytext=(0.955,1450),)
        ax.axvline(0.954122810959807, color='b', linestyle=':')
        
    return

def plot_with_fill(x, y, label):
    lines = plt.plot(x, y, label=label, lw=2)
    plt.fill_between(x, 0, y, alpha=0.2, color=lines[0].get_c())
    plt.legend(loc='best')

    