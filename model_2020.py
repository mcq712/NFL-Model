import numpy as np
import pandas as pd
import seaborn as sns
# from urllib.request import urlopen

# from joblib.numpy_pickle_utils import xrange
# from lxml.html import fromstring
# import requests
# display entire table
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn import metrics
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
    url_main = 'https://www.pro-football-reference.com/teams/{0}/2020/gamelog/'.format(i)
    url_extra = 'https://www.pro-football-reference.com/teams/{0}/2020.htm'.format(i)
    data = pd.read_html(url_main)[0]
    data_extra = pd.read_html(url_extra)[1]
    data.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
    data.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
    data.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
    data.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
    data.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
                    'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
                    'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
                    'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
    data = data[pd.notnull(data['Opp_Score'])]

    data.insert(0, 'Team', i)
    data.insert(11, 'Total Score', data['Tm_Score'] + data['Opp_Score'])
    df_holder.append(data)

all_dfs = pd.concat(df_holder)

# print(all_dfs)

# url_extra = 'https://www.pro-football-reference.com/teams/buf/2020.htm'
# data_extra = pd.read_html(url_extra)[1]

url_per_game_o = 'https://www.espn.com/nfl/stats/team'
url_per_game_d = 'https://www.espn.com/nfl/stats/team/_/view/defense'
per_game_o = pd.read_html(url_per_game_o)
per_game_d = pd.read_html(url_per_game_d)

# print(per_game_o)
# print(per_game_d)




# here we have 2 variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets

x = all_dfs[['PassYds','PasserRate', 'RushYds', '3DConv']]
y = all_dfs['Tm_Score']

regr = linear_model.LinearRegression()
regr.fit(x,y)
# print('Intercept: \n', regr.intercept_)
# print('Coefficients: \n', regr.coef_)
#
# # url_second = 'https://www.pro-football-reference.com/years/2021/#team_stats'
#
# team_averages = pd.read_html(url_second)

# print(team_averages)
predicted_team_1 = regr.predict([[194, 107.3, 145.5, 5]])
predicted_team_2 = regr.predict([[294,87.05,75, 10]])

# print('WFT: ' + str(predicted_team_1))
#
# print('NYG: ' + str(predicted_team_2))
# total_points = predicted_team_1 + predicted_team_2
# print('Total Points: ' + str(total_points))
#
# spread = predicted_team_1 - predicted_team_2
#
# print(spread)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

model = LinearRegression()

model.fit(x_train, y_train)
print(model.coef_)
print(model.intercept_)

coeff_df = pd.DataFrame(model.coef_, x.columns, columns=['Coeff'])

print(coeff_df)


predictions = model.predict(x_test)

plt.scatter(y_test, predictions)
plt.show()

plt.hist(y_test - predictions)
plt.show()

absolute_error = metrics.mean_absolute_error(y_test, predictions)
mse = metrics.mean_squared_error(y_test, predictions)
rmse = np.sqrt(metrics.mean_squared_error(y_test, predictions))
print(rmse)
print(mse)
print(absolute_error)