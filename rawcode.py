# https://www.pro-football-reference.com/teams/buf/2020/gamelog/
# xpath //*[@id="gamelog2020"]/thead/tr[1]/th[1]
# //*[@id="games"]/thead/tr[2]


# Read URL


#
# Replace Existing Column Names


#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(BuffaloBillsO.columns)):
#     ncols.append(BuffaloBillsO.columns[i][1])
#     cols=dict(zip(BuffaloBillsO.columns, ncols))
#     BuffaloBillsO.columns =BuffaloBillsO.columns.to_series().map(cols)
#Rename the headings and duplicates



# # populate Team Name
#
# data.insert(6, 'Team', 'Buffalo Bills')
#
# # Delete columns for events that have not happened
#

#
# print(data)
##################################
#
# # Get defensive and additional offensive data
#
# url1 = 'https://www.pro-football-reference.com/teams/buf/2020.htm'
# BuffaloBillsD = pd.read_html(url1)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(BuffaloBillsD.columns)):
#     ncols.append(BuffaloBillsD.columns[i][1])
# cols=dict(zip(BuffaloBillsD.columns, ncols))
# BuffaloBillsD.columns =BuffaloBillsD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# BuffaloBillsD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                     'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# BuffaloBillsD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                          'Exp_SpTms_Pts']
#
# BuffaloBillsD = BuffaloBillsD[pd.notnull(BuffaloBillsD['Off_1stD'])]
#
#
#
# frames = [BuffaloBillsO, BuffaloBillsD]
# BuffaloSet = pd.concat(frames, axis=1)
#
#
#
#
# ##################################################### NEW ENGLAND PATRIOTS
#
# # Call URL
#
# url2 = 'https://www.pro-football-reference.com/teams/nwe/2020/gamelog/'
#
# # Read URL
#
# NEPatsO = pd.read_html(url2)[0]
#
# # Replace Existing Column Names
#
# NEPatsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# NEPatsO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# NEPatsO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# NEPatsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(NEPatsO.columns)):
#     ncols.append(NEPatsO.columns[i][1])
# cols=dict(zip(NEPatsO.columns, ncols))
# NEPatsO.columns =NEPatsO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# NEPatsO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                    'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                    'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                    'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# NEPatsO.insert(6, 'Team', 'New England Patriots')
#
# # Delete columns for events that have not happened
#
# NEPatsO = NEPatsO[pd.notnull(NEPatsO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url3 = 'https://www.pro-football-reference.com/teams/nwe/2020.htm'
# NEPatsD = pd.read_html(url3)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(NEPatsD.columns)):
#     ncols.append(NEPatsD.columns[i][1])
# cols=dict(zip(NEPatsD.columns, ncols))
# NEPatsD.columns =NEPatsD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# NEPatsD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#               'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# NEPatsD.columns = ['Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                    'Exp_SpTms_Pts']
#
# NEPatsD = NEPatsD[pd.notnull(NEPatsD['Off_1stD'])]
#
#
#
# frames2 = [NEPatsO, NEPatsD]
# NewEnglandSet = pd.concat(frames2, axis=1)
#
#
#
# ##################################################### MIAMI DOLPHINS
#
# # Call URL
#
# url4 = 'https://www.pro-football-reference.com/teams/mia/2020/gamelog/'
#
# # Read URL
#
# MiaDolphinsO = pd.read_html(url4)[0]
#
# # Replace Existing Column Names
#
# MiaDolphinsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# MiaDolphinsO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# MiaDolphinsO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# MiaDolphinsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(MiaDolphinsO.columns)):
#     ncols.append(MiaDolphinsO.columns[i][1])
# cols=dict(zip(MiaDolphinsO.columns, ncols))
# MiaDolphinsO.columns =MiaDolphinsO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# MiaDolphinsO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                         'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                         'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                         'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# MiaDolphinsO.insert(6, 'Team', 'Miami Dolphins')
#
# # Delete columns for events that have not happened
#
# MiaDolphinsO = MiaDolphinsO[pd.notnull(MiaDolphinsO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url5 = 'https://www.pro-football-reference.com/teams/mia/2020.htm'
# MiaDolphinsD = pd.read_html(url5)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(MiaDolphinsD.columns)):
#     ncols.append(MiaDolphinsD.columns[i][1])
# cols=dict(zip(MiaDolphinsD.columns, ncols))
# MiaDolphinsD.columns =MiaDolphinsD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# MiaDolphinsD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                    'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# MiaDolphinsD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                         'Exp_SpTms_Pts']
#
# MiaDolphinsD = MiaDolphinsD[pd.notnull(MiaDolphinsD['Off_1stD'])]
#
#
#
# frames3 = [MiaDolphinsO, MiaDolphinsD]
# MiaDolphinsSet = pd.concat(frames3, axis=1)
#
#
#
# #####################################################  NEW YORK JETS
#
# # Call URL
#
# url6 = 'https://www.pro-football-reference.com/teams/nyj/2020/gamelog/'
#
# # Read URL
#
# NYJetsO = pd.read_html(url6)[0]
#
# # Replace Existing Column Names
#
# NYJetsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# NYJetsO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# NYJetsO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# NYJetsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(NYJetsO.columns)):
#     ncols.append(NYJetsO.columns[i][1])
# cols=dict(zip(NYJetsO.columns, ncols))
# NYJetsO.columns =NYJetsO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# NYJetsO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                    'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                    'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                    'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# NYJetsO.insert(6, 'Team', 'New York Jets')
#
# # Delete columns for events that have not happened
#
# NYJetsO = NYJetsO[pd.notnull(NYJetsO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url7 = 'https://www.pro-football-reference.com/teams/nyj/2020.htm'
# NYJetsD = pd.read_html(url7)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(NYJetsD.columns)):
#     ncols.append(NYJetsD.columns[i][1])
# cols=dict(zip(NYJetsD.columns, ncols))
# NYJetsD.columns =NYJetsD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# NYJetsD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#               'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# NYJetsD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                    'Exp_SpTms_Pts']
#
# NYJetsD = NYJetsD[pd.notnull(NYJetsD['Off_1stD'])]
#
#
#
# frames4 = [NYJetsO, NYJetsD]
# NYJetsSet = pd.concat(frames4, axis=1)
#
#
#
#
# #####################################################  PITTSBURGH STEELERS
#
# # Call URL
#
# url8 = 'https://www.pro-football-reference.com/teams/pit/2020/gamelog/'
#
# # Read URL
#
# PittSteelersO = pd.read_html(url8)[0]
#
# # Replace Existing Column Names
#
# PittSteelersO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# PittSteelersO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# PittSteelersO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# PittSteelersO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(PittSteelersO.columns)):
#     ncols.append(PittSteelersO.columns[i][1])
# cols=dict(zip(PittSteelersO.columns, ncols))
# PittSteelersO.columns =PittSteelersO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# PittSteelersO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                          'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                          'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                          'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# PittSteelersO.insert(6, 'Team', 'Pittsburgh Steelers')
#
# # Delete columns for events that have not happened
#
# PittSteelersO = PittSteelersO[pd.notnull(PittSteelersO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url9 = 'https://www.pro-football-reference.com/teams/pit/2020.htm'
# PittSteelersD = pd.read_html(url9)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(PittSteelersD.columns)):
#     ncols.append(PittSteelersD.columns[i][1])
# cols=dict(zip(PittSteelersD.columns, ncols))
# PittSteelersD.columns =PittSteelersD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# PittSteelersD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                     'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# PittSteelersD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                          'Exp_SpTms_Pts']
#
# PittSteelersD = PittSteelersD[pd.notnull(PittSteelersD['Off_1stD'])]
#
#
#
# frames5 = [PittSteelersO, PittSteelersD]
# PittSteelersSet = pd.concat(frames5, axis=1)
#
#
#
# #####################################################    CINCINNATI BENGALS
#
# # Call URL
#
# url12 = 'https://www.pro-football-reference.com/teams/cin/2020/gamelog/'
#
# # Read URL
#
# CinBengalsO = pd.read_html(url12)[0]
#
# # Replace Existing Column Names
#
# CinBengalsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# CinBengalsO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# CinBengalsO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# CinBengalsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(CinBengalsO.columns)):
#     ncols.append(CinBengalsO.columns[i][1])
# cols=dict(zip(CinBengalsO.columns, ncols))
# CinBengalsO.columns =CinBengalsO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# CinBengalsO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                        'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                        'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                        'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# CinBengalsO.insert(6, 'Team', 'Cincinnati Bengals')
#
# # Delete columns for events that have not happened
#
# CinBengalsO = CinBengalsO[pd.notnull(CinBengalsO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url13 = 'https://www.pro-football-reference.com/teams/cin/2020.htm'
# CinBengalsD = pd.read_html(url13)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(CinBengalsD.columns)):
#     ncols.append(CinBengalsD.columns[i][1])
# cols=dict(zip(CinBengalsD.columns, ncols))
# CinBengalsD.columns =CinBengalsD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# CinBengalsD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                   'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# CinBengalsD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                        'Exp_SpTms_Pts']
#
# CinBengalsD = CinBengalsD[pd.notnull(CinBengalsD['Off_1stD'])]
#
#
#
# frames7 = [CinBengalsO, CinBengalsD]
# CinBengalsSet = pd.concat(frames7, axis=1)
#
#
#
# ##################################### CLEVELAND BROWNS
#
# # Call URL
#
# url10 = 'https://www.pro-football-reference.com/teams/cle/2020/gamelog/'
#
# # Read URL
#
# CleBrownsO = pd.read_html(url10)[0]
#
# # Replace Existing Column Names
#
# CleBrownsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# CleBrownsO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# CleBrownsO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# CleBrownsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(CleBrownsO.columns)):
#     ncols.append(CleBrownsO.columns[i][1])
# cols=dict(zip(CleBrownsO.columns, ncols))
# CleBrownsO.columns =CleBrownsO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# CleBrownsO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                       'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                       'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                       'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# CleBrownsO.insert(6, 'Team', 'Cleveland Browns')
#
# # Delete columns for events that have not happened
#
# CleBrownsO = CleBrownsO[pd.notnull(CleBrownsO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url11 = 'https://www.pro-football-reference.com/teams/cle/2020.htm'
# CleBrownsD = pd.read_html(url11)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(CleBrownsD.columns)):
#     ncols.append(CleBrownsD.columns[i][1])
# cols=dict(zip(CleBrownsD.columns, ncols))
# CleBrownsD.columns =CleBrownsD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# CleBrownsD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                  'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# CleBrownsD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                       'Exp_SpTms_Pts']
#
# CleBrownsD = CleBrownsD[pd.notnull(CleBrownsD['Off_1stD'])]
#
#
#
# frames6 = [CleBrownsO, CleBrownsD]
# CleBrownsSet = pd.concat(frames6, axis=1)
#
#
# ##################################### BALTIMORE RAVENS
#
# # Call URL
#
# url14 = 'https://www.pro-football-reference.com/teams/rav/2020/gamelog/'
#
# # Read URL
#
# BalRavensO = pd.read_html(url14)[0]
#
# # Replace Existing Column Names
#
# BalRavensO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# BalRavensO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# BalRavensO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# BalRavensO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(BalRavensO.columns)):
#     ncols.append(BalRavensO.columns[i][1])
# cols=dict(zip(BalRavensO.columns, ncols))
# BalRavensO.columns =BalRavensO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# BalRavensO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                       'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                       'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                       'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# BalRavensO.insert(6, 'Team', 'Baltimore Ravens')
#
# # Delete columns for events that have not happened
#
# BalRavensO = BalRavensO[pd.notnull(BalRavensO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url15 = 'https://www.pro-football-reference.com/teams/rav/2020.htm'
# BalRavensD = pd.read_html(url15)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(BalRavensD.columns)):
#     ncols.append(BalRavensD.columns[i][1])
# cols=dict(zip(BalRavensD.columns, ncols))
# BalRavensD.columns =BalRavensD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# BalRavensD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                  'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# BalRavensD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                       'Exp_SpTms_Pts']
#
# BalRavensD = BalRavensD[pd.notnull(BalRavensD['Off_1stD'])]
#
#
#
# frames8 = [BalRavensO, BalRavensD]
# BalRavensSet = pd.concat(frames8, axis=1)
#
#
# ##################################### TENNESSEE TITANS
#
# # Call URL
#
# url15 = 'https://www.pro-football-reference.com/teams/oti/2020/gamelog/'
#
# # Read URL
#
# TenTitansO = pd.read_html(url15)[0]
#
# # Replace Existing Column Names
#
# TenTitansO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# TenTitansO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# TenTitansO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# TenTitansO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(TenTitansO.columns)):
#     ncols.append(TenTitansO.columns[i][1])
# cols=dict(zip(TenTitansO.columns, ncols))
# TenTitansO.columns =TenTitansO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# TenTitansO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                       'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                       'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                       'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# TenTitansO.insert(6, 'Team', 'Tennessee Titans')
#
# # Delete columns for events that have not happened
#
# TenTitansO = TenTitansO[pd.notnull(TenTitansO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url16 = 'https://www.pro-football-reference.com/teams/oti/2020.htm'
# TenTitansD = pd.read_html(url16)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(TenTitansD.columns)):
#     ncols.append(TenTitansD.columns[i][1])
# cols=dict(zip(TenTitansD.columns, ncols))
# TenTitansD.columns =TenTitansD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# TenTitansD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                  'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# TenTitansD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                       'Exp_SpTms_Pts']
#
# TenTitansD = TenTitansD[pd.notnull(TenTitansD['Off_1stD'])]
#
#
#
# frames9 = [TenTitansO, TenTitansD]
# TenTitansSet = pd.concat(frames9, axis=1)
#
#
#
# #####################################    INDIANAPOLIS COLTS
#
# # Call URL
#
# url16 = 'https://www.pro-football-reference.com/teams/clt/2020/gamelog/'
#
# # Read URL
#
# IndyColtsO = pd.read_html(url16)[0]
#
# # Replace Existing Column Names
#
# IndyColtsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# IndyColtsO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# IndyColtsO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# IndyColtsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(IndyColtsO.columns)):
#     ncols.append(IndyColtsO.columns[i][1])
# cols=dict(zip(IndyColtsO.columns, ncols))
# IndyColtsO.columns =IndyColtsO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# IndyColtsO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                       'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                       'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                       'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# IndyColtsO.insert(6, 'Team', 'Indianapolis Colts')
#
# # Delete columns for events that have not happened
#
# IndyColtsO = IndyColtsO[pd.notnull(IndyColtsO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url17 = 'https://www.pro-football-reference.com/teams/clt/2020.htm'
# IndyColtsD = pd.read_html(url17)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(IndyColtsD.columns)):
#     ncols.append(IndyColtsD.columns[i][1])
# cols=dict(zip(IndyColtsD.columns, ncols))
# IndyColtsD.columns =IndyColtsD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# IndyColtsD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                  'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# IndyColtsD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                       'Exp_SpTms_Pts']
#
# IndyColtsD = IndyColtsD[pd.notnull(IndyColtsD['Off_1stD'])]
#
#
#
# frames10 = [IndyColtsO, IndyColtsD]
# IndyColtsSet = pd.concat(frames10, axis=1)
#
#
#
# #####################################   Jacksonville Jaguars
#
# # Call URL
#
# url18 = 'https://www.pro-football-reference.com/teams/jax/2020/gamelog/'
#
# # Read URL
#
# JaxJaguarsO = pd.read_html(url18)[0]
#
# # Replace Existing Column Names
#
# JaxJaguarsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# JaxJaguarsO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# JaxJaguarsO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# JaxJaguarsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(JaxJaguarsO.columns)):
#     ncols.append(JaxJaguarsO.columns[i][1])
# cols=dict(zip(JaxJaguarsO.columns, ncols))
# JaxJaguarsO.columns =JaxJaguarsO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# JaxJaguarsO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                        'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                        'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                        'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# JaxJaguarsO.insert(6, 'Team', 'Jacksonville Jaguars')
#
# # Delete columns for events that have not happened
#
# JaxJaguarsO = JaxJaguarsO[pd.notnull(JaxJaguarsO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url19 = 'https://www.pro-football-reference.com/teams/jax/2020.htm'
# JaxJaguarsD = pd.read_html(url19)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(JaxJaguarsD.columns)):
#     ncols.append(JaxJaguarsD.columns[i][1])
# cols=dict(zip(JaxJaguarsD.columns, ncols))
# JaxJaguarsD.columns =JaxJaguarsD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# JaxJaguarsD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                   'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# JaxJaguarsD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                        'Exp_SpTms_Pts']
#
# JaxJaguarsD = JaxJaguarsD[pd.notnull(JaxJaguarsD['Off_1stD'])]
#
#
#
# frames11 = [JaxJaguarsO, JaxJaguarsD]
# JaxJaguarsSet = pd.concat(frames11, axis=1)
#
#
#
# #####################################   HOUSTON TEXANS
#
# # Call URL
#
# url20 = 'https://www.pro-football-reference.com/teams/htx/2020/gamelog/'
#
# # Read URL
#
# HouTexansO = pd.read_html(url20)[0]
#
# # Replace Existing Column Names
#
# HouTexansO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# HouTexansO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# HouTexansO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# HouTexansO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(HouTexansO.columns)):
#     ncols.append(HouTexansO.columns[i][1])
# cols=dict(zip(HouTexansO.columns, ncols))
# HouTexansO.columns =HouTexansO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# HouTexansO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                       'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                       'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                       'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# HouTexansO.insert(6, 'Team', 'Houston Texans')
#
# # Delete columns for events that have not happened
#
# HouTexansO = HouTexansO[pd.notnull(HouTexansO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url21 = 'https://www.pro-football-reference.com/teams/htx/2020.htm'
# HouTexansD = pd.read_html(url21)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(HouTexansD.columns)):
#     ncols.append(HouTexansD.columns[i][1])
# cols=dict(zip(HouTexansD.columns, ncols))
# HouTexansD.columns =HouTexansD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# HouTexansD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                  'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# HouTexansD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                       'Exp_SpTms_Pts']
#
# HouTexansD = HouTexansD[pd.notnull(HouTexansD['Off_1stD'])]
#
#
#
# frames12 = [HouTexansO, HouTexansD]
# HouTexansSet = pd.concat(frames12, axis=1)
#
#
#
# #####################################   KANSAS CITY CHIEF
#
# # Call URL
#
# url22 = 'https://www.pro-football-reference.com/teams/kan/2020/gamelog/'
#
# # Read URL
#
# KCChiefsO = pd.read_html(url22)[0]
#
# # Replace Existing Column Names
#
# KCChiefsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# KCChiefsO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# KCChiefsO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# KCChiefsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(KCChiefsO.columns)):
#     ncols.append(KCChiefsO.columns[i][1])
# cols=dict(zip(KCChiefsO.columns, ncols))
# KCChiefsO.columns =KCChiefsO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# KCChiefsO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                      'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                      'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                      'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# KCChiefsO.insert(6, 'Team', 'Kansas City Chiefs')
#
# # Delete columns for events that have not happened
#
# KCChiefsO = KCChiefsO[pd.notnull(KCChiefsO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url23 = 'https://www.pro-football-reference.com/teams/kan/2020.htm'
# KCChiefsD = pd.read_html(url23)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(KCChiefsD.columns)):
#     ncols.append(KCChiefsD.columns[i][1])
# cols=dict(zip(KCChiefsD.columns, ncols))
# KCChiefsD.columns =KCChiefsD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# KCChiefsD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                 'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# KCChiefsD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                      'Exp_SpTms_Pts']
#
# KCChiefsD = HouTexansD[pd.notnull(HouTexansD['Off_1stD'])]
#
#
#
# frames13 = [KCChiefsO, KCChiefsD]
# KCChiefsSet = pd.concat(frames13, axis=1)
#
#
#
#
#
#
# #####################################  LAS VEGAS RAIDERS
#
# # Call URL
#
# url24 = 'https://www.pro-football-reference.com/teams/rai/2020/gamelog/'
#
# # Read URL
#
# LVRaidersO = pd.read_html(url24)[0]
#
# # Replace Existing Column Names
#
# LVRaidersO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# LVRaidersO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# LVRaidersO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# LVRaidersO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(LVRaidersO.columns)):
#     ncols.append(LVRaidersO.columns[i][1])
# cols=dict(zip(LVRaidersO.columns, ncols))
# LVRaidersO.columns =LVRaidersO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# LVRaidersO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                       'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                       'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                       'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# LVRaidersO.insert(6, 'Team', 'Las Vegas Raiders')
#
# # Delete columns for events that have not happened
#
# LVRaidersO = LVRaidersO[pd.notnull(LVRaidersO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url25 = 'https://www.pro-football-reference.com/teams/rai/2020.htm'
# LVRaidersD = pd.read_html(url25)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(LVRaidersD.columns)):
#     ncols.append(LVRaidersD.columns[i][1])
# cols=dict(zip(LVRaidersD.columns, ncols))
# LVRaidersD.columns =LVRaidersD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# LVRaidersD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                  'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# LVRaidersD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                       'Exp_SpTms_Pts']
#
# LVRaidersD = LVRaidersD[pd.notnull(LVRaidersD['Off_1stD'])]
#
#
#
# frames14 = [LVRaidersO, LVRaidersD]
# LVRaidersSet = pd.concat(frames14, axis=1)
#
#
#
#
# #####################################  LOS ANGELES CHARGERS
#
# # Call URL
#
# url26 = 'https://www.pro-football-reference.com/teams/sdg/2020/gamelog/'
#
# # Read URL
#
# LAChargersO = pd.read_html(url26)[0]
#
# # Replace Existing Column Names
#
# LAChargersO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# LAChargersO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# LAChargersO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# LAChargersO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(LAChargersO.columns)):
#     ncols.append(LAChargersO.columns[i][1])
# cols=dict(zip(LAChargersO.columns, ncols))
# LAChargersO.columns =LAChargersO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# LAChargersO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                        'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                        'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                        'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# LAChargersO.insert(6, 'Team', 'Los Angeles Chargers')
#
# # Delete columns for events that have not happened
#
# LAChargersO = LAChargersO[pd.notnull(LAChargersO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url27 = 'https://www.pro-football-reference.com/teams/sdg/2020.htm'
# LAChargersD = pd.read_html(url27)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(LAChargersD.columns)):
#     ncols.append(LAChargersD.columns[i][1])
# cols=dict(zip(LAChargersD.columns, ncols))
# LAChargersD.columns =LAChargersD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# LAChargersD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                   'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# LAChargersD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                        'Exp_SpTms_Pts']
#
# LAChargersD = LAChargersD[pd.notnull(LAChargersD['Off_1stD'])]
#
#
#
# frames15 = [LAChargersO, LAChargersD]
# LAChargersSet = pd.concat(frames15, axis=1)
#
#
#
#
# #####################################  DENVER BRONCOS
#
# # Call URL
#
# url28 = 'https://www.pro-football-reference.com/teams/den/2020/gamelog/'
#
# # Read URL
#
# DenBroncosO = pd.read_html(url28)[0]
#
# # Replace Existing Column Names
#
# DenBroncosO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# DenBroncosO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# DenBroncosO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# DenBroncosO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(DenBroncosO.columns)):
#     ncols.append(DenBroncosO.columns[i][1])
# cols=dict(zip(DenBroncosO.columns, ncols))
# DenBroncosO.columns =DenBroncosO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# DenBroncosO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                        'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                        'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                        'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# DenBroncosO.insert(6, 'Team', 'Denver Broncos')
#
# # Delete columns for events that have not happened
#
# DenBroncosO = DenBroncosO[pd.notnull(DenBroncosO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url29 = 'https://www.pro-football-reference.com/teams/den/2020.htm'
# DenBroncosD = pd.read_html(url29)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(DenBroncosD.columns)):
#     ncols.append(DenBroncosD.columns[i][1])
# cols=dict(zip(DenBroncosD.columns, ncols))
# DenBroncosD.columns =DenBroncosD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# DenBroncosD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                   'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# DenBroncosD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                        'Exp_SpTms_Pts']
#
# DenBroncosD = DenBroncosD[pd.notnull(DenBroncosD['Off_1stD'])]
#
#
#
# frames16 = [DenBroncosO, DenBroncosD]
# DenBroncosSet = pd.concat(frames16, axis=1)
#
#
#
#
# #####################################    THE WASHINGTON FOOTBALL TEAM
#
# # Call URL
#
# url30 = 'https://www.pro-football-reference.com/teams/was/2020/gamelog/'
#
# # Read URL
#
# WashingtonO = pd.read_html(url30)[0]
#
# # Replace Existing Column Names
#
# WashingtonO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# WashingtonO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# WashingtonO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# WashingtonO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(WashingtonO.columns)):
#     ncols.append(WashingtonO.columns[i][1])
# cols=dict(zip(WashingtonO.columns, ncols))
# WashingtonO.columns =WashingtonO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# WashingtonO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                        'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                        'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                        'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# WashingtonO.insert(6, 'Team', 'Washington Football Team')
#
# # Delete columns for events that have not happened
#
# WashingtonO = WashingtonO[pd.notnull(WashingtonO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url31 = 'https://www.pro-football-reference.com/teams/was/2020.htm'
# WashingtonD = pd.read_html(url31)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(WashingtonD.columns)):
#     ncols.append(WashingtonD.columns[i][1])
# cols=dict(zip(WashingtonD.columns, ncols))
# WashingtonD.columns =WashingtonD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# WashingtonD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                   'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# WashingtonD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                        'Exp_SpTms_Pts']
#
# WashingtonD = WashingtonD[pd.notnull(WashingtonD['Off_1stD'])]
#
#
#
# frames17 = [WashingtonO, WashingtonD]
# WashingtonSet = pd.concat(frames17, axis=1)
#
#
#
# #####################################    DALLAS COWBOYS
#
# # Call URL
#
# url32 = 'https://www.pro-football-reference.com/teams/dal/2020/gamelog/'
#
# # Read URL
#
# DalCowboysO = pd.read_html(url32)[0]
#
# # Replace Existing Column Names
#
# DalCowboysO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# DalCowboysO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# DalCowboysO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# DalCowboysO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(DalCowboysO.columns)):
#     ncols.append(DalCowboysO.columns[i][1])
# cols=dict(zip(DalCowboysO.columns, ncols))
# DalCowboysO.columns =DalCowboysO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# DalCowboysO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                        'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                        'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                        'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# DalCowboysO.insert(6, 'Team', 'Dallas Cowboys')
#
# # Delete columns for events that have not happened
#
# DalCowboysO = DalCowboysO[pd.notnull(DalCowboysO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url33 = 'https://www.pro-football-reference.com/teams/dal/2020.htm'
# DalCowboysD = pd.read_html(url33)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(DalCowboysD.columns)):
#     ncols.append(DalCowboysD.columns[i][1])
# cols=dict(zip(DalCowboysD.columns, ncols))
# DalCowboysD.columns =DalCowboysD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# DalCowboysD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                   'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# DalCowboysD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                        'Exp_SpTms_Pts']
#
# DalCowboysD = DalCowboysD[pd.notnull(DalCowboysD['Off_1stD'])]
#
#
#
# frames18 = [DalCowboysO, DalCowboysD]
# DalCowboysSet = pd.concat(frames18, axis=1)
#
#
#
#
# #####################################   PHILIDELPHIA EAGLES
#
#
# # Call URL
#
# url34 = 'https://www.pro-football-reference.com/teams/phi/2020/gamelog/'
#
# # Read URL
#
# PhiEaglesO = pd.read_html(url34)[0]
#
# # Replace Existing Column Names
#
# PhiEaglesO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# PhiEaglesO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# PhiEaglesO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# PhiEaglesO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(PhiEaglesO.columns)):
#     ncols.append(PhiEaglesO.columns[i][1])
# cols=dict(zip(PhiEaglesO.columns, ncols))
# PhiEaglesO.columns =PhiEaglesO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# PhiEaglesO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                       'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                       'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                       'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# PhiEaglesO.insert(6, 'Team', 'Philadelphia Eagles')
#
# # Delete columns for events that have not happened
#
# PhiEaglesO = PhiEaglesO[pd.notnull(PhiEaglesO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url35 = 'https://www.pro-football-reference.com/teams/phi/2020.htm'
# PhiEaglesD = pd.read_html(url35)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(PhiEaglesD.columns)):
#     ncols.append(PhiEaglesD.columns[i][1])
# cols=dict(zip(PhiEaglesD.columns, ncols))
# PhiEaglesD.columns =PhiEaglesD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# PhiEaglesD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                  'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# PhiEaglesD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                       'Exp_SpTms_Pts']
#
# PhiEaglesD = PhiEaglesD[pd.notnull(PhiEaglesD['Off_1stD'])]
#
#
#
# frames18 = [PhiEaglesO, PhiEaglesD]
# PhiEaglesSet = pd.concat(frames18, axis=1)
#
#
# #####################################   NEW YORK GIANTS
#
#
# # Call URL
#
# url36 = 'https://www.pro-football-reference.com/teams/nyg/2020/gamelog/'
#
# # Read URL
#
# NYGiantsO = pd.read_html(url36)[0]
#
# # Replace Existing Column Names
#
# NYGiantsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# NYGiantsO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# NYGiantsO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# NYGiantsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(NYGiantsO.columns)):
#     ncols.append(NYGiantsO.columns[i][1])
# cols=dict(zip(NYGiantsO.columns, ncols))
# NYGiantsO.columns =NYGiantsO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# NYGiantsO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                      'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                      'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                      'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# NYGiantsO.insert(6, 'Team', 'New York Giants')
#
# # Delete columns for events that have not happened
#
# NYGiantsO = NYGiantsO[pd.notnull(NYGiantsO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url37 = 'https://www.pro-football-reference.com/teams/nyg/2020.htm'
# NYGiantsD = pd.read_html(url37)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(NYGiantsD.columns)):
#     ncols.append(NYGiantsD.columns[i][1])
# cols=dict(zip(NYGiantsD.columns, ncols))
# NYGiantsD.columns =NYGiantsD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# NYGiantsD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                 'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# NYGiantsD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                      'Exp_SpTms_Pts']
#
# NYGiantsD = NYGiantsD[pd.notnull(NYGiantsD['Off_1stD'])]
#
#
#
# frames19 = [NYGiantsO, NYGiantsD]
# NYGiantsSet = pd.concat(frames19, axis=1)
#
#
# #####################################   CHICAGO BEARS
#
#
# # Call URL
#
# url40 = 'https://www.pro-football-reference.com/teams/chi/2020/gamelog/'
#
# # Read URL
#
# ChiBearsO = pd.read_html(url40)[0]
#
# # Replace Existing Column Names
#
# ChiBearsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# ChiBearsO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# ChiBearsO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# ChiBearsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(ChiBearsO.columns)):
#     ncols.append(ChiBearsO.columns[i][1])
# cols=dict(zip(ChiBearsO.columns, ncols))
# ChiBearsO.columns =ChiBearsO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# ChiBearsO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                      'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                      'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                      'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# ChiBearsO.insert(6, 'Team', 'Chicago Bears')
#
# # Delete columns for events that have not happened
#
# ChiBearsO = ChiBearsO[pd.notnull(ChiBearsO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url41 = 'https://www.pro-football-reference.com/teams/chi/2020.htm'
# ChiBearsD = pd.read_html(url41)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(ChiBearsD.columns)):
#     ncols.append(ChiBearsD.columns[i][1])
# cols=dict(zip(ChiBearsD.columns, ncols))
# ChiBearsD.columns =ChiBearsD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# ChiBearsD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                 'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# ChiBearsD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                      'Exp_SpTms_Pts']
#
# ChiBearsD = ChiBearsD[pd.notnull(ChiBearsD['Off_1stD'])]
#
#
#
# frames21 = [ChiBearsO, ChiBearsD]
# ChiBearsSet = pd.concat(frames21, axis=1)
#
#
#
#
# #####################################   DETROIT LIONS
#
#
# # Call URL
#
# url42 = 'https://www.pro-football-reference.com/teams/det/2020/gamelog/'
#
# # Read URL
#
# DetLionsO = pd.read_html(url42)[0]
#
# # Replace Existing Column Names
#
# DetLionsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# DetLionsO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# DetLionsO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# DetLionsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(DetLionsO.columns)):
#     ncols.append(DetLionsO.columns[i][1])
# cols=dict(zip(DetLionsO.columns, ncols))
# DetLionsO.columns =DetLionsO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# DetLionsO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                      'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                      'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                      'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# DetLionsO.insert(6, 'Team', 'Detroit Lions')
#
# # Delete columns for events that have not happened
#
# DetLionsO = DetLionsO[pd.notnull(DetLionsO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url43 = 'https://www.pro-football-reference.com/teams/det/2020.htm'
# DetLionsD = pd.read_html(url43)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(DetLionsD.columns)):
#     ncols.append(DetLionsD.columns[i][1])
# cols=dict(zip(DetLionsD.columns, ncols))
# DetLionsD.columns =DetLionsD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# DetLionsD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                 'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# DetLionsD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                      'Exp_SpTms_Pts']
#
# DetLionsD = DetLionsD[pd.notnull(DetLionsD['Off_1stD'])]
#
#
#
# frames22 = [DetLionsO, DetLionsD]
# DetLionsSet = pd.concat(frames22, axis=1)
#
#
#
#
#
# #####################################  MINNESOTA VIKINGS
#
#
# # Call URL
#
# url44 = 'https://www.pro-football-reference.com/teams/min/2020/gamelog/'
#
# # Read URL
#
# MinnVikingsO = pd.read_html(url44)[0]
#
# # Replace Existing Column Names
#
# MinnVikingsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# MinnVikingsO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# MinnVikingsO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# MinnVikingsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(MinnVikingsO.columns)):
#     ncols.append(MinnVikingsO.columns[i][1])
# cols=dict(zip(MinnVikingsO.columns, ncols))
# MinnVikingsO.columns =MinnVikingsO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# MinnVikingsO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                         'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                         'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                         'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# MinnVikingsO.insert(6, 'Team', 'Minnesota Vikings')
#
# # Delete columns for events that have not happened
#
# MinnVikingsO = MinnVikingsO[pd.notnull(MinnVikingsO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url45 = 'https://www.pro-football-reference.com/teams/min/2020.htm'
# MinnVikingsD = pd.read_html(url45)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(MinnVikingsD.columns)):
#     ncols.append(MinnVikingsD.columns[i][1])
# cols=dict(zip(MinnVikingsD.columns, ncols))
# MinnVikingsD.columns =MinnVikingsD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# MinnVikingsD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                    'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# MinnVikingsD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                         'Exp_SpTms_Pts']
#
# MinnVikingsD = MinnVikingsD[pd.notnull(MinnVikingsD['Off_1stD'])]
#
#
#
# frames23 = [MinnVikingsO, MinnVikingsD]
# MinnVikingsSet = pd.concat(frames23, axis=1)
#
#
#
#
# ##################################### GREEN BAY PACKERS
#
#
# # Call URL
#
# url62 = 'https://www.pro-football-reference.com/teams/gnb/2020/gamelog/'
#
# # Read URL
#
# GBPackersO = pd.read_html(url62)[0]
#
# # Replace Existing Column Names
#
# GBPackersO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# GBPackersO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# GBPackersO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# GBPackersO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(GBPackersO.columns)):
#     ncols.append(GBPackersO.columns[i][1])
# cols=dict(zip(GBPackersO.columns, ncols))
# GBPackersO.columns =GBPackersO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# GBPackersO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                       'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                       'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                       'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# GBPackersO.insert(6, 'Team', 'Green Bay Packers')
#
# # Delete columns for events that have not happened
#
# GBPackersO = GBPackersO[pd.notnull(GBPackersO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url66 = 'https://www.pro-football-reference.com/teams/gnb/2020.htm'
# GBPackersD = pd.read_html(url66)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(GBPackersD.columns)):
#     ncols.append(GBPackersD.columns[i][1])
# cols=dict(zip(GBPackersD.columns, ncols))
# GBPackersD.columns =GBPackersD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# GBPackersD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                  'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# GBPackersD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                       'Exp_SpTms_Pts']
#
# GBPackersD = GBPackersD[pd.notnull(GBPackersD['Off_1stD'])]
#
#
#
# frames32 = [GBPackersO, GBPackersD]
# GBPackersSet = pd.concat(frames32, axis=1)
#
#
#
#
#
# #####################################  TAMPA BAY BUCCANEERS
#
#
# # Call URL
#
# url46 = 'https://www.pro-football-reference.com/teams/tam/2020/gamelog/'
#
# # Read URL
#
# TBBucsO = pd.read_html(url46)[0]
#
# # Replace Existing Column Names
#
# TBBucsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# TBBucsO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# TBBucsO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# TBBucsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(TBBucsO.columns)):
#     ncols.append(TBBucsO.columns[i][1])
# cols=dict(zip(TBBucsO.columns, ncols))
# TBBucsO.columns =TBBucsO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# TBBucsO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                    'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                    'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                    'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# TBBucsO.insert(6, 'Team', 'Tampa Bay Buccaneers')
#
# # Delete columns for events that have not happened
#
# TBBucsO = TBBucsO[pd.notnull(TBBucsO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url47 = 'https://www.pro-football-reference.com/teams/tam/2020.htm'
# TBBucsD = pd.read_html(url47)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(TBBucsD.columns)):
#     ncols.append(TBBucsD.columns[i][1])
# cols=dict(zip(TBBucsD.columns, ncols))
# TBBucsD.columns =TBBucsD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# TBBucsD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#               'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# TBBucsD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                    'Exp_SpTms_Pts']
#
# TBBucsD = TBBucsD[pd.notnull(TBBucsD['Off_1stD'])]
#
#
#
# frames24 = [TBBucsO, TBBucsD]
# TBBucsSet = pd.concat(frames24, axis=1)
#
#
#
#
# #####################################  CAROLINA PANTHERS
#
#
# # Call URL
#
# url48 = 'https://www.pro-football-reference.com/teams/car/2020/gamelog/'
#
# # Read URL
#
# CarPanthersO = pd.read_html(url48)[0]
#
# # Replace Existing Column Names
#
# CarPanthersO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# CarPanthersO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# CarPanthersO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# CarPanthersO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(CarPanthersO.columns)):
#     ncols.append(CarPanthersO.columns[i][1])
# cols=dict(zip(CarPanthersO.columns, ncols))
# CarPanthersO.columns =CarPanthersO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# CarPanthersO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                         'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                         'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                         'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# CarPanthersO.insert(6, 'Team', 'Carolina Panthers')
#
# # Delete columns for events that have not happened
#
# CarPanthersO = CarPanthersO[pd.notnull(CarPanthersO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url49 = 'https://www.pro-football-reference.com/teams/car/2020.htm'
# CarPanthersD = pd.read_html(url49)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(CarPanthersD.columns)):
#     ncols.append(CarPanthersD.columns[i][1])
# cols=dict(zip(CarPanthersD.columns, ncols))
# CarPanthersD.columns =CarPanthersD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# CarPanthersD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                    'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# CarPanthersD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                         'Exp_SpTms_Pts']
#
# CarPanthersD = CarPanthersD[pd.notnull(CarPanthersD['Off_1stD'])]
#
#
#
# frames25 = [CarPanthersO, CarPanthersD]
# CarPanthersSet = pd.concat(frames25, axis=1)
#
#
#
# #####################################  NEW ORLEANS SAINTS
#
#
# # Call URL
#
# url50 = 'https://www.pro-football-reference.com/teams/nor/2020/gamelog/'
#
# # Read URL
#
# NOSaintsO = pd.read_html(url50)[0]
#
# # Replace Existing Column Names
#
# NOSaintsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# NOSaintsO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# NOSaintsO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# NOSaintsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(NOSaintsO.columns)):
#     ncols.append(NOSaintsO.columns[i][1])
# cols=dict(zip(NOSaintsO.columns, ncols))
# NOSaintsO.columns =NOSaintsO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# NOSaintsO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                      'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                      'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                      'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# NOSaintsO.insert(6, 'Team', 'New Orleans Saints')
#
# # Delete columns for events that have not happened
#
# NOSaintsO = NOSaintsO[pd.notnull(NOSaintsO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url51 = 'https://www.pro-football-reference.com/teams/nor/2020.htm'
# NOSaintsD = pd.read_html(url51)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(NOSaintsD.columns)):
#     ncols.append(NOSaintsD.columns[i][1])
# cols=dict(zip(NOSaintsD.columns, ncols))
# NOSaintsD.columns =NOSaintsD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# NOSaintsD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                 'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# NOSaintsD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                      'Exp_SpTms_Pts']
#
# NOSaintsD = NOSaintsD[pd.notnull(NOSaintsD['Off_1stD'])]
#
#
#
# frames26 = [NOSaintsO, NOSaintsD]
# NOSaintsSet = pd.concat(frames26, axis=1)
#
#
#
# #####################################  ATLANTA FALCONS
#
#
# # Call URL
#
# url52 = 'https://www.pro-football-reference.com/teams/atl/2020/gamelog/'
#
# # Read URL
#
# AtlFalconsO = pd.read_html(url52)[0]
#
# # Replace Existing Column Names
#
# AtlFalconsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# AtlFalconsO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# AtlFalconsO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# AtlFalconsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(AtlFalconsO.columns)):
#     ncols.append(AtlFalconsO.columns[i][1])
# cols=dict(zip(AtlFalconsO.columns, ncols))
# AtlFalconsO.columns =AtlFalconsO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# AtlFalconsO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                        'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                        'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                        'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# AtlFalconsO.insert(6, 'Team', 'Atlanta Falcons')
#
# # Delete columns for events that have not happened
#
# AtlFalconsO = AtlFalconsO[pd.notnull(AtlFalconsO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url53 = 'https://www.pro-football-reference.com/teams/atl/2020.htm'
# AtlFalconsD = pd.read_html(url53)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(AtlFalconsD.columns)):
#     ncols.append(AtlFalconsD.columns[i][1])
# cols=dict(zip(AtlFalconsD.columns, ncols))
# AtlFalconsD.columns =AtlFalconsD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# AtlFalconsD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                   'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# AtlFalconsD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                        'Exp_SpTms_Pts']
#
# AtlFalconsD = AtlFalconsD[pd.notnull(AtlFalconsD['Off_1stD'])]
#
#
#
# frames27 = [AtlFalconsO, AtlFalconsD]
# AtlFalconsSet = pd.concat(frames27, axis=1)
#
#
#
#
# #####################################  SEATTLE SEAHAWKS
#
#
# # Call URL
#
# url54 = 'https://www.pro-football-reference.com/teams/sea/2020/gamelog/'
#
# # Read URL
#
# SeahawksO = pd.read_html(url54)[0]
#
# # Replace Existing Column Names
#
# SeahawksO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# SeahawksO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# SeahawksO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# SeahawksO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(SeahawksO.columns)):
#     ncols.append(SeahawksO.columns[i][1])
# cols=dict(zip(SeahawksO.columns, ncols))
# SeahawksO.columns =SeahawksO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# SeahawksO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                      'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                      'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                      'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# SeahawksO.insert(6, 'Team', 'Seattle Seahawks')
#
# # Delete columns for events that have not happened
#
# SeahawksO = SeahawksO[pd.notnull(SeahawksO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url55 = 'https://www.pro-football-reference.com/teams/sea/2020.htm'
# SeahawksD = pd.read_html(url55)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(SeahawksD.columns)):
#     ncols.append(SeahawksD.columns[i][1])
# cols=dict(zip(SeahawksD.columns, ncols))
# SeahawksD.columns =SeahawksD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# SeahawksD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                 'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# SeahawksD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                      'Exp_SpTms_Pts']
#
# SeahawksD = SeahawksD[pd.notnull(SeahawksD['Off_1stD'])]
#
#
#
# frames28 = [SeahawksO, SeahawksD]
# SeahawksSet = pd.concat(frames28, axis=1)
#
#
#
#
#
#
# ##################################### LOS ANGELES RAMS
#
#
# # Call URL
#
# url56 = 'https://www.pro-football-reference.com/teams/ram/2020/gamelog/'
#
# # Read URL
#
# LARamsO = pd.read_html(url56)[0]
#
# # Replace Existing Column Names
#
# LARamsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# LARamsO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# LARamsO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# LARamsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(LARamsO.columns)):
#     ncols.append(LARamsO.columns[i][1])
# cols=dict(zip(LARamsO.columns, ncols))
# LARamsO.columns =LARamsO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# LARamsO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                    'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                    'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                    'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# LARamsO.insert(6, 'Team', 'Los Angeles Rams')
#
# # Delete columns for events that have not happened
#
# LARamsO = LARamsO[pd.notnull(LARamsO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url57 = 'https://www.pro-football-reference.com/teams/ram/2020.htm'
# LARamsD = pd.read_html(url57)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(LARamsD.columns)):
#     ncols.append(LARamsD.columns[i][1])
# cols=dict(zip(LARamsD.columns, ncols))
# LARamsD.columns =LARamsD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# LARamsD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#               'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# LARamsD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                    'Exp_SpTms_Pts']
#
# LARamsD = LARamsD[pd.notnull(LARamsD['Off_1stD'])]
#
#
#
# frames29 = [LARamsO, LARamsD]
# LARamsSet = pd.concat(frames29, axis=1)
#
#
#
#
# ##################################### SAN FRANCISCO 49ERS
#
#
# # Call URL
#
# url58 = 'https://www.pro-football-reference.com/teams/sfo/2020/gamelog/'
#
# # Read URL
#
# SF49ersO = pd.read_html(url58)[0]
#
# # Replace Existing Column Names
#
# SF49ersO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# SF49ersO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# SF49ersO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# SF49ersO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(SF49ersO.columns)):
#     ncols.append(SF49ersO.columns[i][1])
# cols=dict(zip(SF49ersO.columns, ncols))
# SF49ersO.columns =SF49ersO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# SF49ersO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                     'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                     'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                     'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# SF49ersO.insert(6, 'Team', 'San Francisco 49ers')
#
# # Delete columns for events that have not happened
#
# SF49ersO = SF49ersO[pd.notnull(SF49ersO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url59 = 'https://www.pro-football-reference.com/teams/sfo/2020.htm'
# SF49ersD = pd.read_html(url59)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(SF49ersD.columns)):
#     ncols.append(SF49ersD.columns[i][1])
# cols=dict(zip(SF49ersD.columns, ncols))
# SF49ersD.columns =SF49ersD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# SF49ersD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# SF49ersD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                     'Exp_SpTms_Pts']
#
# SF49ersD = SF49ersD[pd.notnull(SF49ersD['Off_1stD'])]
#
#
#
# frames30 = [SF49ersO, SF49ersD]
# SF49ersSet = pd.concat(frames30, axis=1)
#
#
#
#
#
# ##################################### SAN FRANCISCO 49ERS
#
#
# # Call URL
#
# url60 = 'https://www.pro-football-reference.com/teams/crd/2020/gamelog/'
#
# # Read URL
#
# AriCardsO = pd.read_html(url60)[0]
#
# # Replace Existing Column Names
#
# AriCardsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
# AriCardsO.rename(columns={'Unnamed: 4_level_1': 'W/L'}, inplace=True)
# AriCardsO.rename(columns={'Unnamed: 6_level_1': '@'}, inplace=True)
# AriCardsO.rename(columns={'Unnamed: 3_level_1': 'Box_link'}, inplace=True)
#
# # Get rid of Top Row within table on Football Reference
#
# ncols=[]
# for i in range(len(AriCardsO.columns)):
#     ncols.append(AriCardsO.columns[i][1])
# cols=dict(zip(AriCardsO.columns, ncols))
# AriCardsO.columns =AriCardsO.columns.to_series().map(cols)
#
# # Rename the headings and duplicates
#
# AriCardsO.columns = ['Week', 'Day', 'Date', 'Box_link', 'W/L', 'OT', 'Home/Away', 'Opp_Team', 'Tm_Score',
#                      'Opp_Score', 'PassCmp', 'PassAtt', 'PassYds', 'PassTD', 'Int', 'Sk', 'YdsLost_Sk', 'PassY/A',
#                      'PassNY/A', 'Cmp%', 'PasserRate', 'RushAtt', 'RushYds', 'RushY/A', 'RushTD', 'FGM', 'FGA', 'XPM',
#                      'XPA', 'Pnt', 'PntYds', '3DConv', '3DAtt', '4DConv', '4DAtt', 'ToP']
#
# # populate Team Name
#
# AriCardsO.insert(6, 'Team', 'Arizona Cardinals')
#
# # Delete columns for events that have not happened
#
# AriCardsO = AriCardsO[pd.notnull(AriCardsO['Opp_Score'])]
#
#
# ##################################
#
# # Get defensive and additional offensive data
#
# url61 = 'https://www.pro-football-reference.com/teams/crd/2020.htm'
# AriCardsD = pd.read_html(url61)[1]
#
# # delete heading above true heading
#
# ncols=[]
# for i in range(len(AriCardsD.columns)):
#     ncols.append(AriCardsD.columns[i][1])
# cols=dict(zip(AriCardsD.columns, ncols))
# AriCardsD.columns =AriCardsD.columns.to_series().map(cols)
#
# # get rid of unnecessary columns
#
# AriCardsD.drop(['Week', 'Day', 'Date', 'Unnamed: 3_level_1', 'Unnamed: 4_level_1', 'Unnamed: 5_level_1', 'OT', 'Rec',
#                 'Unnamed: 8_level_1', 'Opp', 'Tm', 'Opp', 'PassY', 'RushY'], axis= 1, inplace=True)
#
# # Rename rest of the Columns
#
# AriCardsD.columns = ['Off_1stD', 'Off_TotYd', 'Off_TO', 'Def_1stD', 'Def_TotYd', 'Def_TO', 'Exp_OffPts', 'Exp_DefPts',
#                      'Exp_SpTms_Pts']
#
# AriCardsD = AriCardsD[pd.notnull(AriCardsD['Off_1stD'])]
#
#
#
# frames31 = [AriCardsO, AriCardsD]
# AriCardsSet = pd.concat(frames31, axis=1)
#
#
#
#
#
# FramesFinal = [KCChiefsSet, LAChargersSet, LVRaidersSet, DenBroncosSet, JaxJaguarsSet, IndyColtsSet, TenTitansSet, HouTexansSet, PittSteelersSet,
#                CinBengalsSet, BalRavensSet, CleBrownsSet, BuffaloSet, NYJetsSet, NewEnglandSet, MiaDolphinsSet, ChiBearsSet, GBPackersSet,
#                DetLionsSet, AtlFalconsSet, MinnVikingsSet, CarPanthersSet, NOSaintsSet, TBBucsSet, DalCowboysSet, NYGiantsSet, PhiEaglesSet,
#                WashingtonSet, AriCardsSet, LARamsSet, SeahawksSet, SF49ersSet]
#
#
# FinalSet = pd.concat(FramesFinal)
# print(FinalSet)
#
# FinalSet['Off_TO'].fillna(0, inplace=True)
#
# FinalSet.insert(0, 'Game_ID', range(880, 880 + len(FinalSet)))
#
# X = FinalSet[['PassYds', 'RushYds', "3DConv", 'Off_TO']]
# Y = FinalSet[['Tm_Score']]
# X = sm.add_constant(X)
#
#
#
#
# JetsAvgPassYds = NYJetsSet['PassYds'].mean(axis=0)
# JetsAvgRushYds = NYJetsSet['RushYds'].mean(axis=0)
# JetsAvgThird = NYJetsSet['3DConv'].mean(axis=0)
# JetsAvgSk = NYJetsSet['Off_TO'].mean(axis=0)
#
#
# BroncosAvgPassYds = DenBroncosSet['PassYds'].median(axis=0)
# BroncosAvgRushYds = DenBroncosSet['RushYds'].median(axis=0)
# BroncosAvgThird = DenBroncosSet['3DConv'].mean(axis=0)
# BroncosAvgSk = DenBroncosSet['Off_TO'].mean(axis=0)
#
#
# Const = 6.0757
# PassYdsCoef = 0.0555
# RushYdsCoef = 0.0697
# ThirdConvCoef = 0.2195
# SkCoef = -2.9360
#
#
#
#
# ############ SAINTS VS LIONS
# SaintsAvgPassYds = NOSaintsSet['PassYds'].median(axis=0)
# SaintsAvgRushYds = NOSaintsSet['RushYds'].median(axis=0)
# SaintsAvgThird = NOSaintsSet['3DConv'].median(axis=0)
# SaintsAvgTO = NOSaintsSet['Off_TO'].median(axis=0)
#
#
# LionsAvgPassYds = DetLionsSet['PassYds'].median(axis=0)
# LionsAvgRushYds = DetLionsSet['RushYds'].median(axis=0)
# LionsAvgThird = DetLionsSet['3DConv'].median(axis=0)
# LionsAvgTO = DetLionsSet['Off_TO'].median(axis=0)
#
#
# Const = 6.0757
# PassYdsCoef = 0.0555
# RushYdsCoef = 0.0697
# ThirdConvCoef = 0.2195
# TOCoef = -2.9360
#
# SaintsScore = Const + (PassYdsCoef * SaintsAvgPassYds) + (RushYdsCoef * SaintsAvgRushYds) + (ThirdConvCoef*SaintsAvgThird) + (TOCoef * SaintsAvgTO)
# LionsScore = Const + (PassYdsCoef * LionsAvgPassYds) + (RushYdsCoef * LionsAvgRushYds) + (ThirdConvCoef*LionsAvgThird) + (TOCoef*LionsAvgTO)
# print('SAINTS VS LIONS')
# print('The saints will score: ' + str(SaintsScore) + ' points. The Lions will score: ' + str(LionsScore) + ' points.')
# finalScore = LionsScore + SaintsScore
# print('The total will be: '+ str(finalScore))
#
#
# ############ CARDINALS VS PANTHERS
# CardsAvgPassYds = AriCardsSet['PassYds'].mean(axis=0)
# CardsAvgRushYds = AriCardsSet['RushYds'].mean(axis=0)
# CardsAvgThird = AriCardsSet['3DConv'].mean(axis=0)
# CardsAvgTO = AriCardsSet['Off_TO'].mean(axis=0)
#
#
# PanthersAvgPassYds = CarPanthersSet['PassYds'].mean(axis=0)
# PanthersAvgRushYds = CarPanthersSet['RushYds'].mean(axis=0)
# PanthersAvgThird = CarPanthersSet['3DConv'].mean(axis=0)
# PanthersAvgTO = CarPanthersSet['Off_TO'].mean(axis=0)
#
# CardsScore = Const + (PassYdsCoef * CardsAvgPassYds) + (RushYdsCoef * CardsAvgRushYds) + (ThirdConvCoef*CardsAvgThird) + (TOCoef * CardsAvgTO)
# PanthersScore = Const + (PassYdsCoef * PanthersAvgPassYds) + (RushYdsCoef * PanthersAvgRushYds) + (ThirdConvCoef*PanthersAvgThird) + (TOCoef*PanthersAvgTO)
# print('PANTHERS VS CARDINALS')
# print('The Cardinals will score: ' + str(CardsScore) + ' points. The Panthers will score: ' + str(PanthersScore) + ' points.')
# finalScore1 = PanthersScore + CardsScore
# print('The total will be: ' + str(finalScore1))
#
# ############ BENGALS VS JAGUARS
# BengalsAvgPassYds = CinBengalsSet['PassYds'].mean(axis=0)
# BengalsAvgRushYds = CinBengalsSet['RushYds'].mean(axis=0)
# BengalsAvgThird = CinBengalsSet['3DConv'].mean(axis=0)
# BengalsAvgTO = CinBengalsSet['Off_TO'].mean(axis=0)
#
#
# JagsAvgPassYds = JaxJaguarsSet['PassYds'].mean(axis=0)
# JagsAvgRushYds = JaxJaguarsSet['RushYds'].mean(axis=0)
# JagsAvgThird = JaxJaguarsSet['3DConv'].mean(axis=0)
# JagsAvgTO = JaxJaguarsSet['Off_TO'].mean(axis=0)
#
# BengalsScore = Const + (PassYdsCoef * BengalsAvgPassYds) + (RushYdsCoef * BengalsAvgRushYds) + (ThirdConvCoef*BengalsAvgThird) + (TOCoef * BengalsAvgTO)
# JagsScore = Const + (PassYdsCoef * JagsAvgPassYds) + (RushYdsCoef * JagsAvgRushYds) + (ThirdConvCoef*JagsAvgThird) + (TOCoef*JagsAvgTO)
# print('BENGALS VS JAGUARS')
# print('The Bengals will score: ' + str(BengalsScore) + ' points. The Jaguars will score: ' + str(JagsScore) + ' points.')
# finalScore2 = BengalsScore + JagsScore
# print('The total will be: ' + str(finalScore2))
#
#
# ############ BROWNS VS COWBOYS
# BrownsAvgPassYds = CleBrownsSet['PassYds'].mean(axis=0)
# BrownsAvgRushYds = CleBrownsSet['RushYds'].mean(axis=0)
# BrownsAvgThird = CleBrownsSet['3DConv'].mean(axis=0)
# BrownsAvgTO = CleBrownsSet['Off_TO'].mean(axis=0)
#
#
# CowboysAvgPassYds = DalCowboysSet['PassYds'].mean(axis=0)
# CowboysAvgRushYds = DalCowboysSet['RushYds'].mean(axis=0)
# CowboysAvgThird = DalCowboysSet['3DConv'].mean(axis=0)
# CowboysAvgTO = DalCowboysSet['Off_TO'].mean(axis=0)
#
# BrownsScore = Const + (PassYdsCoef * BrownsAvgPassYds) + (RushYdsCoef * BrownsAvgRushYds) + (ThirdConvCoef*BrownsAvgThird) + (TOCoef * BrownsAvgTO)
# CowboysScore = Const + (PassYdsCoef * CowboysAvgPassYds) + (RushYdsCoef * CowboysAvgRushYds) + (ThirdConvCoef*CowboysAvgThird) + (TOCoef*CowboysAvgTO)
# print('BROWNS VS COWBOYS')
# print('The Browns will score: ' + str(BrownsScore) + ' points. The Cowboys will score: ' + str(CowboysScore) + ' points.')
# finalScore3 = BrownsScore + CowboysScore
# print('The total will be: ' + str(finalScore2))
#
#
# ############ VIKINGS VS TEXANS
# TexansAvgPassYds = HouTexansSet['PassYds'].mean(axis=0)
# TexansAvgRushYds = HouTexansSet['RushYds'].mean(axis=0)
# TexansAvgThird = HouTexansSet['3DConv'].mean(axis=0)
# TexansAvgTO = HouTexansSet['Off_TO'].mean(axis=0)
#
#
# VikingsAvgPassYDs = MinnVikingsSet['PassYds'].mean(axis=0)
# VikingsAvgRushYds = MinnVikingsSet['RushYds'].mean(axis=0)
# VikingsAvgThird = MinnVikingsSet['3DConv'].mean(axis=0)
# VikingsAvgTO = MinnVikingsSet['Off_TO'].mean(axis=0)
#
# TexansScore = Const + (PassYdsCoef * TexansAvgPassYds) + (RushYdsCoef * TexansAvgRushYds) + (ThirdConvCoef*TexansAvgThird) + (TOCoef * TexansAvgTO)
# VikingsScore = Const + (PassYdsCoef * VikingsAvgPassYDs) + (RushYdsCoef * VikingsAvgRushYds) + (ThirdConvCoef*VikingsAvgThird) + (TOCoef*VikingsAvgTO)
# print('TEXANS VS VIKINGS')
# print('The Texans will score: ' + str(TexansScore) + ' points. The Vikings will score: ' + str(VikingsScore) + ' points.')
# finalScore4 = TexansScore + VikingsScore
# print('The total will be: ' + str(finalScore4))
#
#
# ############ SEAHAWKS VS DOLPHINS
# SeahawksAvgPassYds = SeahawksSet['PassYds'].mean(axis=0)
# SeahawksAvgRushYds = SeahawksSet['RushYds'].mean(axis=0)
# SeahawksAvgThird = SeahawksSet['3DConv'].mean(axis=0)
# SeahawksAvgTO = SeahawksSet['Off_TO'].mean(axis=0)
#
#
# DolphinsAvgPassYds = MiaDolphinsSet['PassYds'].mean(axis=0)
# DolphinsAvgRushYds = MiaDolphinsSet['RushYds'].mean(axis=0)
# DolphinsAvgThird = MiaDolphinsSet['3DConv'].mean(axis=0)
# DolphinsAvgTO = MiaDolphinsSet['Off_TO'].mean(axis=0)
#
# DolphinsScore = Const + (PassYdsCoef * DolphinsAvgPassYds) + (RushYdsCoef * DolphinsAvgRushYds) + (ThirdConvCoef*DolphinsAvgThird) + (TOCoef * SeahawksAvgTO)
# SeahawksScore = Const + (PassYdsCoef * SeahawksAvgPassYds) + (RushYdsCoef * SeahawksAvgRushYds) + (ThirdConvCoef*SeahawksAvgThird) + (TOCoef*SeahawksAvgTO)
# print('SEAHAWKS VS DOLPHINS')
# print('The Seahawks will score: ' + str(SeahawksScore) + ' points. The Dolphins will score: ' + str(DolphinsScore) + ' points.')
# finalScore5 = SeahawksScore + DolphinsScore
# print('The total will be: ' + str(finalScore5))
#
#
# ############ CHARGERS VS BUCCANEERS
# ChargersAvgPassYds = LAChargersSet['PassYds'].mean(axis=0)
# ChargersAvgRushYds = LAChargersSet['RushYds'].mean(axis=0)
# ChargersAvgThird = LAChargersSet['3DConv'].mean(axis=0)
# ChargersAvgTO = LAChargersSet['Off_TO'].mean(axis=0)
#
#
# BucsAvgPassYds = TBBucsSet['PassYds'].mean(axis=0)
# BucsAvgRushYds = TBBucsSet['RushYds'].mean(axis=0)
# BucsAvgThird = TBBucsSet['3DConv'].mean(axis=0)
# BucsAvgTO = TBBucsSet['Off_TO'].mean(axis=0)
#
# BucsScore = Const + (PassYdsCoef * BucsAvgPassYds) + (RushYdsCoef * BucsAvgRushYds) + (ThirdConvCoef*BucsAvgThird) + (TOCoef * BucsAvgTO)
# ChargersScore = Const + (PassYdsCoef * ChargersAvgPassYds) + (RushYdsCoef * ChargersAvgRushYds) + (ThirdConvCoef*ChargersAvgThird) + (TOCoef*ChargersAvgTO)
# print('BUCCANEERS VS CHARGERS')
# print('The Chargers will score: ' + str(ChargersScore) + ' points. The Buccaneers will score: ' + str(BucsScore) + ' points.')
# finalScore6 = ChargersScore + BucsScore
# print('The total will be: ' + str(finalScore6))
#
# ############ RAVENS VS WASHINGTON
# RavensAvgPassYds = BalRavensSet['PassYds'].mean(axis=0)
# RavensAvgRushYds = BalRavensSet['RushYds'].mean(axis=0)
# RavensAvgThird = BalRavensSet['3DConv'].mean(axis=0)
# RavensAvgTO = BalRavensSet['Off_TO'].mean(axis=0)
#
#
# WashAvgPassYDs = WashingtonSet['PassYds'].mean(axis=0)
# WashAvgRushYds = WashingtonSet['RushYds'].mean(axis=0)
# WashAvgThird = WashingtonSet['3DConv'].mean(axis=0)
# WashAvgTO = WashingtonSet['Off_TO'].mean(axis=0)
#
# WashScore = Const + (PassYdsCoef * WashAvgPassYDs) + (RushYdsCoef * WashAvgRushYds) + (ThirdConvCoef*WashAvgThird) + (TOCoef * WashAvgTO)
# RavensScore = Const + (PassYdsCoef * RavensAvgPassYds) + (RushYdsCoef * RavensAvgRushYds) + (ThirdConvCoef*RavensAvgThird) + (TOCoef*RavensAvgTO)
# print('RAVENS VS WASHINGTON')
# print('The Ravens will score: ' + str(RavensScore) + ' points. Washington will score: ' + str(WashScore) + ' points.')
# finalScore7 = WashScore + RavensScore
# print('The total will be: ' + str(finalScore7))
#
#
#
#
# TeamAvgRushYdsAll = FinalSet.groupby('Opp_Team')['RushYds'].median()
# print(TeamAvgRushYdsAll)
#
# TeamAvgThirdAll = FinalSet.groupby('Opp_Team')['3DConv'].median()
# print(TeamAvgThirdAll)
#
# TeamAvgTO = FinalSet.groupby('Opp_Team')['Off_TO'].median()
# print(TeamAvgTO)
#
# TeamAvgPassYdsAll = FinalSet.groupby('Team')['PassYds'].median()
# print(TeamAvgPassYdsAll)
#
# TeamAvgRushYdsAll = FinalSet.groupby('Team')['RushYds'].median()
# print(TeamAvgRushYdsAll)
#
# TeamAvgThirdAll = FinalSet.groupby('Team')['3DConv'].median()
# print(TeamAvgThirdAll)
#
# TeamAvgTO = FinalSet.groupby('Opp_Team')['Off_TO'].median()
# print(TeamAvgTO)
#
#
#
#
# st_dev_passyardsall = np.std(TeamAvgPassYdsAll)
# print(st_dev_passyardsall)
#
# st_dev_rushyardsall = np.std(TeamAvgRushYdsAll)
# print(st_dev_rushyardsall)
#
# st_dev_thirdall = np.std(TeamAvgThirdAll)
# print(st_dev_thirdall)
#
# st_dev_DTO = np.std(TeamAvgTO)
# print(st_dev_DTO)
#
#
#
#
#
#
# OppTeamAvgPassYdsAll = FinalSet.groupby('Opp_Team')['RushYds'].mean()
# print(OppTeamAvgPassYdsAll)
#
# OppTeamAvgRushYdsAll = FinalSet.groupby('Opp_Team')['RushYds'].mean()
# print(OppTeamAvgRushYdsAll)
#
# OppTeamAvgThirdAll = FinalSet.groupby('Opp_Team')['3DConv'].mean()
# print(OppTeamAvgThirdAll)
#
# OppTeamAvgTO = FinalSet.groupby('Opp_Team')['Off_TO'].mean()
# print(OppTeamAvgTO)
#
# TeamAvgPassYds= FinalSet.groupby('Team')['PassYds'].mean()
# print(TeamAvgPassYds)
#
# TeamAvgRushYds = FinalSet.groupby('Team')['RushYds'].mean()
# print(TeamAvgRushYds)
#
# TeamAvgThird = FinalSet.groupby('Team')['3DConv'].mean()
# print(TeamAvgThird)
#
# TeamAvgTO = FinalSet.groupby('Team')['Off_TO'].mean()
# print(TeamAvgTO)
#
# print('Steelers ML and under')
