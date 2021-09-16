import matplotlib.pyplot as plt
import pandas as pd

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
plt.scatter(all_dfs['Tm_Score'], all_dfs['PassYds'], color = 'red')
plt.title('Team Scores Vs. Passing Yards', fontsize= 14)
plt.xlabel ('Team Score', fontsize = 14)
plt.ylabel('Passing Yards', fontsize = 14)
plt.grid(True)
plt.show()

plt.scatter(all_dfs['Tm_Score'], all_dfs['RushYds'], color = 'blue')
plt.title('Team Scores Vs. Rushing Yards', fontsize= 14)
plt.xlabel ('Team Score', fontsize = 14)
plt.ylabel('Rushing Yards', fontsize = 14)
plt.grid(True)
plt.show()

plt.scatter(all_dfs['Tm_Score'], all_dfs['3DConv'], color = 'green')
plt.title('Team Scores Vs. 3rd Down Conversions', fontsize= 14)
plt.xlabel ('Team Score', fontsize = 14)
plt.ylabel('3rd Down Conversions', fontsize = 14)
plt.grid(True)
plt.show()


plt.scatter(all_dfs['Tm_Score'], all_dfs['Pnt'], color = 'orange')
plt.title('Team Scores Vs. Punts', fontsize= 14)
plt.xlabel ('Team Score', fontsize = 14)
plt.ylabel('Punts', fontsize = 14)
plt.grid(True)
plt.show()

plt.scatter(all_dfs['Tm_Score'], all_dfs['PasserRate'], color = 'cyan')
plt.title('Team Scores Vs. Passer Rating', fontsize= 14)
plt.xlabel ('Team Score', fontsize = 14)
plt.ylabel('Passer Rating', fontsize = 14)
plt.grid(True)
plt.show()
# Figure out how to deal with time data
# plt.scatter(all_dfs['Tm_Score'], all_dfs['ToP'], color = 'pink')
# plt.title('Team Scores Vs. Time of Possession', fontsize= 14)
# plt.xlabel ('Team Score', fontsize = 14)
# plt.ylabel('Time of Possession', fontsize = 14)
# plt.grid(True)
# plt.show()


