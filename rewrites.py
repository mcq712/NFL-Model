import numpy as np
import pandas as pd

# from urllib.request import urlopen

# from joblib.numpy_pickle_utils import xrange
# from lxml.html import fromstring
# import requests
# display entire table
import matplotlib.pyplot as plt


import statsmodels.api as sm
# from pandas import DataFrame
from statsmodels.regression import linear_model
import statsmodels.api as sm
from sklearn import linear_model
pd.set_option('display.max_rows', None, 'display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


# Call URL
# team = input('Please use team abbreviation: ')
team_abbreviations = ['buf','mia','nwe','nyj','htx','clt','jax','oti','cin','pit',
                      'cle','rav','den','kan','rai','sdg','phi','dal','nyg','was',
                      'car','nor','tam','atl','chi','det','gnb','min','crd','ram','sea','sfo']
df_holder = []

for i in team_abbreviations:
    url_main = 'https://www.pro-football-reference.com/teams/{0}/2021/gamelog/'.format(i)
    data = pd.read_html(url_main)[0]
    data.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
    data.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
    data.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
    data.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
    data.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
                    'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
                    'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
                    'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
    data = data[pd.notnull(data['Opp_Score'])]
    data.insert(6, 'Team', i)
    data.insert(11, 'Total Score', data['Tm_Score'] + data['Opp_Score'])
    df_holder.append(data)

all_dfs = pd.concat(df_holder)
print(all_dfs)

# here we have 2 variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets

x = all_dfs[['PassYds','PasserRate', 'RushYds']]
y = all_dfs['Tm_Score']

regr = linear_model.LinearRegression()
regr.fit(x,y)
print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)

url_second = 'https://www.pro-football-reference.com/years/2021/#team_stats'

team_averages = pd.read_html(url_second)

# print(team_averages)
