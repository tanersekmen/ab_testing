import pandas as pd
from scipy.stats import shapiro
from scipy.stats import levene
from scipy.stats import ttest_ind
from scipy.stats import mannwhitneyu

ab_control = pd.read_excel("ab_testing.xlsx", sheet_name='Control Group')
ab_test = pd.read_excel("ab_testing.xlsx", sheet_name='Test Group')
print(ab_control)
print(ab_test)


control = ab_control.copy()
test = ab_test.copy()

control.head()
test.head()

len(control)
len(test)

control.isnull().any() # there is no missing value
test.isnull().any() # there is no missing value

pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 500)

control.describe().T
test.describe().T
# Data distribution looks like normal.


# COLUMNS
# Impression: The number of views to ads
# Click: The number of clicks on ads
# Purchase: The number of product that bought after clicking ads
# Earning: The amount of profit obtained as a result of the products sold

test['Purchase']

# The purpose of company is to maximize of conversation ratio. Then, it means conversion rate = purchase/click.
# Generally, the target of companpanies is to increase profit when they spend money to improve their quality.
# Above line explains 'return on investment'.
# My assumption:
#   The long-term return of the expenditures has a positive correlation with the short-term return.


# I will test two hypothesis in my project:
# 1. There is a significant difference in conversion rate.

# 1st Hypothesis
## Define hypothesis to test.
## μc: Mean conversion rate of the control group
## μt: Mean conversion rate of the test group

## H0: μc=μt (Zero hypothesis)
## H1: μc!=μt

test_conversion = test['Purchase']/test['Click'] # Find a conversion rate
control_conversion = control['Purchase']/control['Click'] # Find a conversion rate

## interpreting of the results of tests and recommendation

shapiro(test_conversion)
shapiro(control_conversion)
#The result of shapiro shows us to distrube as normal. Then, there is no conclude that to reject H0
#in test and control datasets.

levene(test_conversion, control_conversion)
# Variance homogeneity is ensured.
ttest_ind(test_conversion, control_conversion, equal_var=False)
# testing at 95% and p_value < 0.05 there is a significant difference in means of two samples.


test_conversion.mean() # 0.1566
control_conversion.mean() # 0.1159
# So, conversion rate of test data is different from control data.
# It done and conversion rate is increased.

## Which tests did you use and why?
# I tested with Shapiro cause want to understand distribution of datasets.
# Levene shows homogeneity of variance so I used it to see.
# I used the ttest_ind to test the significance of the hypothesis.
# When I changed equal_var = False, It turned into Welch's t-test.
