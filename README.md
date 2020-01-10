# Who are the 5% Unfunded on Kiva?

![alt text](https://github.com/emkawong/capstone1-kiva/blob/master/images/donationpage.png "taken from kiva.org")

## Microloans! An Introduction

Kiva is a nonprofit company that provides microloans (typically defined as a small loan provided by individuals instead of banks) to people that otherwise might not have access to loans because of a lack of credit or bank accessibility. 97% of the time lenders get their money back but they never receive interest on their loans. 

Approximately 10% of the world's population (or approximately 700 million) lives in "extreme poverty" which is described as living on less than about $2 a day. Initially microfunding was hailed as this potential silver bullet that would lead to substantial development and lift communities out of poverty. The thoery goes like this - let's say fertilizer increases a farm's output by 20%. If a borrower receives $1000 to purchase that fertilizer, they will be able to increase their profits and then use those profits to buy more fertilizer in the next year and that $1000 will snowball. 

However, numerous studies conducted around the world have shown that currently, it does not lead to a much higher future income growth than those who did not receive loans. Perhaps with more finagling of how the loans are structured, who the loans are given to, and the amount that is given, there could be positive long term effects on economic growth. On the other hand, if we look at other factors besides long-term growth, it does improve the lives of the borrowers in the short term in that it gives them more options - especially in times of sudden economic stress.

With all of that in mind, Kiva has an incredibly high fund rate - about 95% of loans posted on Kiva are funded. Which led me to the question, who are the 5%? And are there any stark differences in their characteristics?

## Data Analysis

### First Impressions

The Kiva dataset is available to the public as multiple csvs on their website. It provides extensive information on both individual loans and the lenders who are financing each loan. When I initially looked at this dataset, my main hurdle was figuring out my scope. I eventually decided that Country, Gender, and Hashtags (posted on each loan), would be a good place to start.

So, my three main question (that have some of my assumptions baked in):
1. Does the country you're from even make a small difference in getting a loan?
2. Do females achieve a higher successful fund rate? 
3. Do loans with hashtags featuring words like #Schooling and #WomenBiz fair better than others? 

### Methodology

As I looked at the data, I realized that for each of my questions, I was essentially asking the same question. What was the probability that a certain subpopulation had a higher proportion of successfully getting funded over the other subpopulation? I considered using a frequentist approach and using the chi-squared distribution but decided on a bayesian analysis since the data looked like a good fit for this kind of analysis. 

In order to do so, I created a number of helped functions that would:
 1. Take my main Kiva dataframe and pivot on the data(column) I was interested in studying.
 2. Clean up that data so I that I would only be dealing with the funded loans and the unfunded loans and their totals. 
 3. Create a dictionary of variables and their beta probability density functions.
 4. Repeat the process above for random sampling. 
 5. Graph the distributions on the same axis to compare. 

### Question 1: Country Matters

First I wanted to discover who in the world was getting funded, and which countries were receiving the most loans so I graphed the top 25 countries that were requesting loans (out of a total of about 100). 

![alt text](https://github.com/emkawong/capstone1-kiva/blob/master/images/country-top.png "Top 25 Countries Requesting Loans from Kiva")

So borrowers in the Philippines are asking for subtantially more loans, interesting! But that doesn't tell me anything about if being in a country matters in terms of getting more loans funded. So now we use the beta distribution to compare the probability of getting funded between two countries. Here's what that graph looks like. 

![alt text](https://github.com/emkawong/capstone1-kiva/blob/master/images/country-analysis.png "Which Country is Getting Funded?")

What does this tell us? Well as the beta distribution gets higher values of alpha and beta (number of funded loans and number of unfunded loans, respectively) the probability gets more concentrated around a certain value. So for example the Philippines has a high value of certainty because we have so much data surrounding that proportion. In basically all of these cases, because we have so much data, we can say that if you compare any of the countries here - say the Philippines against Peru, there is essentially 100% probability that the Phillipines is getting a higher proportion of successfully funded loans. Even if we look at countries with clearly overlapping distributions, because we have so much data, there is still about 96.95% probability that Uganda is getting a higher proportion of successfully funded loans than Tajikistan.

### Question 2: Gender Matters

Next, the question of gender, in order to look at this variable. I needed to create a column that would group any amount of people (male or female) into a separate "group" category. Otherwise any different combination of males and females would make my graphs hard to read and hard to analyze. 

And here's what the gender analysis looks like.

![alt text](https://github.com/emkawong/capstone1-kiva/blob/master/images/gender-analysis.png "Who is Getting Funded?")

In this case, it does look like gender matters. For females, there's about a 100% probabilty of getting a higher proportion of successfully funded loans over males. On the Kiva website, the first category shown on the website is "Women" so it makes sense that the most heavily advertised category (and I'm sure a variety of other reasons) gives females a leg up in funding. 

### Question 3: Hashtags Might Matter, Types Definitely Matter

The journey through this question was long for I started in the wrong place. I decided that hashtags were the best place to start in terms of looking at category and compiled and created a dictionary that looked at the total amount of hashtags attached to successful loans versus unsuccessful loans. The problem here being that the hashtags seemed to be placed somewhat arbitrarily and not every loan had a hashtag. Luckily, Kiva also has data on the type of loan for each loan.

Below is a graph depicting the total amount of unfunded loans versus the expected amount of unfunded loans. This expected amount is based on the average rate of failure over all categories multiplied by the total amount of loans. Anytime the Expected bar is higher than the Actual bar can be thought of a type of loan that failed more than we would expect. 

![alt text](https://github.com/emkawong/capstone1-kiva/blob/master/images/failed-loan.png "Failed Loan")

But we need more analysis to figure out the explicit probabilities of each category. And that graph is below.

![alt text](https://github.com/emkawong/capstone1-kiva/blob/master/images/type-analysis.png "Which Types of Loans are Getting Funding")

First of all, type of loan definitely matters. Similar to the country analysis above, if the beta distribution looks like it's centered at a higher proportion, there's so much data that there's pretty much 100% probability of that type of loan is getting a higher proportion of successfully funded loan. Interestingly enough, it looks like a lot of the types that we would expect to be higher, like Housing and Transportation - necessities, aren't quite as successful as say Art or Manufacturing. I have some thoughts that this might happen because the type of person to donate to Kiva wants to see economic growth - and Housing doesn't necessarily provide that. 

## Conclusion

A female in the Philippines asking for a loan to provide funds for Manufacturing has a higher probability of getting funded than a male in El Salvador asking for a loan to provide funds for Housing. Country matters, gender matters, type of loan matters. Do some of those variables matter more than others? Probably. Next steps for me would be to look at all of this data at an even more granular level.  


