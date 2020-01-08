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

#sector

exp_over_total = expired['LOAN_ID'].count()/(funded['LOAN_ID'].count()+expired['LOAN_ID'].count())
sector_pivot = df.pivot_table(values = 'LOAN_ID', index = 'SECTOR_NAME', columns = 'STATUS', aggfunc = 'count')
sector_pivot['funded_expired_total'] = sector_pivot['expired']+ sector_pivot['funded']
sector_pivot['expected'] = (sector_pivot['funded_expired_total']*exp_over_total).astype(int)

sector_expired = sector_pivot['expired'].reset_index()
sector_funded = sector_pivot['funded'].reset_index()
sector_expected = sector_pivot['expected'].reset_index()

#gender 

gender_pivot = df.pivot_table(values = 'LOAN_ID', index = 'GENDER_GROUPS', columns = 'STATUS', aggfunc = 'count')
gender_pivot['funded_expired_total'] = gender_pivot['expired']+ gender_pivot['funded']
gender_pivot['funded_rate'] = gender_pivot['funded']/gender_pivot['funded_expired_total']

female_funded_rate = gender_pivot['funded_rate']['female']
male_funded_rate = gender_pivot['funded_rate']['male']

female_beta = stats.beta(female_funded, female_total-female_funded).pdf(x)
male_beta = stats.beta(male_funded, male_total-male_funded).pdf(x)
female_beta_rvs = stats.beta(female_funded, female_total-female_funded).rvs(10000)
male_beta_rvs = stats.beta(male_funded, male_total-male_funded).rvs(10000)

x = np.arange(0,1,.001)
plot_with_fill(x,female_beta,'expired')
plot_with_fill(x,male_beta,'funded')
plt.xlim(0.875, .98)

prob1 = (female_beta_rvs > male_beta_rvs + .075).mean() * 100
prob2 = (female_beta_rvs > male_beta_rvs + .0775).mean() * 100
prob3 = (female_beta_rvs > male_beta_rvs + .080).mean() * 100
print('There is a {:.2f}% probability that a single female asking for a loan has a 7.5% better chance than a single male to have the loan successfully funded\n'.format(prob1))
print('There is a {:.2f}% probability that a single female asking for a loan has a 7.75% better chance than a single male to have the loan succesfully funded\n'.format(prob2))
print('There is a {:.2f}% probability that a single female asking for a loan has a 8.0% better chance than a single male to have the loan successfully funded\n'.format(prob3))