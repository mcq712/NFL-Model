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
team_abbreviations = ['buf', 'mia', 'nwe', 'nyj', 'htx', 'clt', 'jax', 'oti', 'cin', 'pit',
                      'cle', 'rav', 'den', 'kan', 'rai', 'sdg', 'phi', 'dal', 'nyg', 'was',
                      'car', 'nor', 'tam', 'atl', 'chi', 'det', 'gnb', 'min', 'crd', 'ram', 'sea', 'sfo']
df_holder = []
df_holder_2021 = []

for i in team_abbreviations:
    url_main = 'https://www.pro-football-reference.com/teams/{0}/2020/gamelog/'.format(i)

    data = pd.read_html(url_main)[0]

    data.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
    data.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
    data.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
    data.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
    data.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
                    'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
                    'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
                    'XPA', 'Pnt', 'PntYds', 'ThirdConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
    data = data[pd.notnull(data['Opp_Score'])]

    data.insert(0, 'Team', i)
    data.insert(11, 'Total Score', data['Tm_Score'] + data['Opp_Score'])
    df_holder.append(data)
for i in team_abbreviations:
    url_main_2021 = 'https://www.pro-football-reference.com/teams/{0}/2021/gamelog/'.format(i)
    data_extra = pd.read_html(url_main_2021)[0]
    data_extra.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
    data_extra.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
    data_extra.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
    data_extra.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
    data_extra.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
                          'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
                          'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA',
                          'XPM',
                          'XPA', 'Pnt', 'PntYds', 'ThirdConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
    data_extra = data_extra[pd.notnull(data_extra['Opp_Score'])]

    data_extra.insert(0, 'Team', i)
    data_extra.insert(11, 'Total Score', data_extra['Tm_Score'] + data_extra['Opp_Score'])
    df_holder_2021.append(data_extra)

df_2020 = pd.concat(df_holder)
df_2021 = pd.concat(df_holder_2021)

all_dfs = pd.concat([df_2020, df_2021], axis=0)

# print(all_dfs)

# url_extra = 'https://www.pro-football-reference.com/teams/buf/2020.htm'
# data_extra = pd.read_html(url_extra)[1]

# print(per_game_o)
# print(per_game_d)


# here we have 2 variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets

x = all_dfs[['PassYds', 'PasserRate', 'RushYds', 'ThirdConv']]
y = all_dfs['Tm_Score']
print(all_dfs)
regr = linear_model.LinearRegression()
regr.fit(x, y)
# print('Intercept: \n', regr.intercept_)
# print('Coefficients: \n', regr.coef_)
#
# # url_second = 'https://www.pro-football-reference.com/years/2021/#team_stats'
#
# team_averages = pd.read_html(url_second)

# print(team_averages)

#
# spread = predicted_team_1 - predicted_team_2
#
# print(spread)

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
#
# model = LinearRegression()
#
# model.fit(x_train, y_train)
# print(model.coef_)
# print(model.intercept_)
#
# coeff_df = pd.DataFrame(model.coef_, x.columns, columns=['Coeff'])
#
# print(coeff_df)


# predictions = model.predict(x_test)
#
# plt.scatter(y_test, predictions)
# plt.show()
#
# plt.hist(y_test - predictions)
# plt.show()
#
# absolute_error = metrics.mean_absolute_error(y_test, predictions)
# mse = metrics.mean_squared_error(y_test, predictions)
# rmse = np.sqrt(metrics.mean_squared_error(y_test, predictions))
# print(rmse)
# print(mse)
# print(absolute_error)

d_pass_yards_avg = df_2021.groupby('Opp_Team').PassYds.mean()
print(d_pass_yards_avg)
o_pass_yards_avg = df_2021.groupby('Team').PassYds.mean()
print(o_pass_yards_avg)
d_rush_yards_avg = df_2021.groupby('Opp_Team').RushYds.mean()
print(d_rush_yards_avg)
o_rush_yards_avg = df_2021.groupby('Team').RushYds.mean()
print(o_rush_yards_avg)
o_3dwn_avg = df_2021.groupby('Team').ThirdConv.mean()
print(o_3dwn_avg)
d_3dwn_avg = df_2021.groupby('Opp_Team').ThirdConv.mean()
print(o_3dwn_avg)

d_against_qbr = df_2021.groupby('Opp_Team').PasserRate.mean()
print(d_against_qbr)
o_qbr = df_2021.groupby('Team').PasserRate.mean()
print(o_qbr)


def score_prediction(team_name1, opp_team_name1, team_name2, opp_team_name2):
    tnf_passyd_avg_tm1 = (d_pass_yards_avg[opp_team_name1] + o_pass_yards_avg[team_name1]) / 2

    tnf_passerrate_tm1 = (d_against_qbr[opp_team_name1] + o_qbr[team_name1]) / 2

    tnf_rushyd_avg_tm1 = (d_rush_yards_avg[opp_team_name1] + o_rush_yards_avg[team_name1]) / 2

    tnf_thirdconv_tm1 = (d_3dwn_avg[opp_team_name1] + o_3dwn_avg[team_name1]) / 2

    predicted_team_1 = regr.predict([[tnf_passyd_avg_tm1, tnf_passerrate_tm1, tnf_rushyd_avg_tm1, tnf_thirdconv_tm1]])

    print(opp_team_name2 + ' predicted points: \n' + str(predicted_team_1))

    tnf_passyd_avg_tm2 = (d_pass_yards_avg[opp_team_name2] + o_pass_yards_avg[team_name2]) / 2

    tnf_passerrate_tm2 = (d_against_qbr[opp_team_name2] + o_qbr[team_name2]) / 2

    tnf_rushyd_avg_tm2 = (d_rush_yards_avg[opp_team_name2] + o_rush_yards_avg[team_name2]) / 2

    tnf_thirdconv_tm2 = (d_3dwn_avg[opp_team_name2] + o_3dwn_avg[team_name2]) / 2

    predicted_team_2 = regr.predict([[tnf_passyd_avg_tm2, tnf_passerrate_tm2, tnf_rushyd_avg_tm2, tnf_thirdconv_tm2]])
    print(opp_team_name1 + ' predicted points: \n' + str(predicted_team_2))

    print('Total Points: \n' + str(predicted_team_2 + predicted_team_1))

    if predicted_team_1 > predicted_team_2:
        spread = (predicted_team_1 - predicted_team_2)
        print(opp_team_name2 + ' predicted win margin: \n' + str(spread))
    else:
        spread = (predicted_team_2 - predicted_team_1)
        print(opp_team_name1 + ' predicted win margin: \n' + str(spread))
    print('-' * 25)
    return


score_prediction('cin', 'Jacksonville Jaguars', 'jax', 'Cincinnati Bengals')

score_prediction('nor', 'New York Giants', 'nyg', 'New Orleans Saints')

score_prediction('cle', 'Minnesota Vikings', 'min', 'Cleveland Browns')

score_prediction('dal', 'Carolina Panthers', 'car', 'Dallas Cowboys')

score_prediction('htx', 'Buffalo Bills', 'buf', 'Houston Texans')

score_prediction('oti', 'New York Jets', 'nyj', 'Tennessee Titans')

score_prediction('clt', 'Miami Dolphins', 'mia', 'Indianapolis Colts')

score_prediction('kan', 'Philadelphia Eagles', 'phi', 'Kansas City Chiefs')

score_prediction('was', 'Atlanta Falcons', 'atl', 'Washington Football Team')

score_prediction('chi', 'Detroit Lions', 'det', 'Chicago Bears')

score_prediction('crd', 'Los Angeles Rams', 'ram', 'Arizona Cardinals')

score_prediction('sea', 'San Francisco 49ers', 'sfo', 'Seattle Seahawks')

score_prediction('den', 'Baltimore Ravens', 'rav', 'Denver Broncos')

score_prediction('pit', 'Green Bay Packers', 'gnb', 'Pittsburgh Steelers')

score_prediction('tam', 'New England Patriots', 'nwe', 'Tampa Bay Buccaneers')

score_prediction('sdg', 'Las Vegas Raiders', 'rai', 'Los Angeles Chargers')
