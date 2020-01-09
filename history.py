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
    beta = result[(result['GENDER_GROUPS'] == 'female') | (result['GENDER_GROUPS'] == 'male')]['LOAN_ID'].count() - alpha
    
    return stats.beta(a=alpha, b=beta).pdf(x)

def get_tags_dict(df):

    '''Takes a Pandas DataFrame and creates a dict that contains the count of the tag'''

    tags_list = df.TAGS.str.replace(" ","").str.split(",")

    tags_dict = {}

    for loan in tags_list[tags_list.notnull()]:
        for hashtag in loan:
            if hashtag in tags_dict:
                tags_dict[hashtag] += 1
            else:
                tags_dict[hashtag] = 1
            
    return tags_dict

def create_df(df,category):
    '''
    Takes the Kiva loan df and creates a new df that pivots on the desired category and takes the count between expired 
    and funded loans. Then creates,removes,renames columns so that the df only contains the category values as rows names
    and funded/expired/total as columns headers. 
    '''
    pivot = df.pivot_table(values = 'LOAN_ID', index = category, columns = 'STATUS', aggfunc = 'count')
    pivot['total'] = pivot['expired']+ pivot['funded']
    pivot = pivot.drop(['fundRaising','refunded'],axis=1)
    
    return pivot

    