import streamlit as st
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, date

st.title('Betsting')
st.text('backtesting sport betting app, beta version 3.1')


def nba_data():
    df=pd.read_excel('NBA odds database_app_Betsting.xlsx')
    return df
df = nba_data()

st.sidebar.header('Select Options')

unique_league = df.League.unique()
selected_league = st.sidebar.selectbox('League', unique_league)

unique_season = df.Season.unique()
selected_season = st.sidebar.selectbox('Season', list(reversed(unique_season)))

#bet_type = st.sidebar.selectbox('Bet type', ('Spread','Under/Over'))
if selected_league == "NBA":
    bet_type = st.sidebar.selectbox('Bet type', ('Spread','Under/Over'))
    if bet_type == 'Spread':
        played_team = st.sidebar.selectbox('Team played', ('Home','Away'))
        open_or_close = st.sidebar.selectbox('Based on Open Odds or Close Odds?', ('Open','Close'))
        unique_line_movement = df.Spread_Open_to_Close_Home.unique()
        selected_line_movement = st.sidebar.selectbox('Is open spread line bigger than close spread line?', unique_line_movement)
        min_range, max_range = st.sidebar.select_slider(
            'Spread Range',
            options=list(range(-30,31)),
            value=(-30,30))
    else:
        played_UO = st.sidebar.selectbox('Under or Over?', ('Under','Over'))
        open_or_close = st.sidebar.selectbox('Based on Open Odds or Close Odds?', ('Open','Close'))
        unique_line_movement_UO = df.UO_Open_to_Close_Home.unique()
        selected_line_movement_UO = st.sidebar.selectbox('Is open Under/Over line bigger than close Under/Over line?', unique_line_movement_UO)
        min_range, max_range = st.sidebar.select_slider(
            'Under/Over Range',
            options=list(range(150,251)),
            value=(150,250))
else:
    bet_type = st.sidebar.selectbox('Bet type', ('Under/Over',''))
    played_UO = st.sidebar.selectbox('Under or Over?', ('Under','Over'))
    open_or_close = st.sidebar.selectbox('Based on Open Odds or Close Odds?', ('Open','Close'))
    unique_line_movement_UO = df.UO_Open_to_Close_Home.unique()
    selected_line_movement_UO = st.sidebar.selectbox('Is open Under/Over line bigger than close Under/Over line?', unique_line_movement_UO)
    min_range, max_range = st.sidebar.select_slider(
        'Under/Over Range',
        options=list(range(4,21)),
        value=(4,20))


st.markdown('___')

#Chart display
if selected_league  == "NBA":
    if bet_type == "Spread":
        if played_team == "Home":
            if open_or_close == "Open":
                df_selected_data = df[(df.Season == selected_season) & (df.Spread_Open_to_Close_Home == selected_line_movement) & (df.League == "NBA")]
                df_selected_data_spread = df_selected_data[(df_selected_data.Home_Spread_Open >= min_range) & (df_selected_data.Home_Spread_Open <= max_range)]
                chart_data = df_selected_data_spread.Spread_bet_home_open.cumsum()
                st.line_chart(chart_data)
                nuber_of_games = df_selected_data_spread.Spread_bet_home_open.count()
                number_of_wins = nuber_of_games - (np.sum(df_selected_data_spread.Spread_bet_home_open == -1))
                effectiveness = (number_of_wins / nuber_of_games) * 100
                roi = np.average(df_selected_data_spread.Spread_bet_home_open) * 100
                result_100_usd = np.sum(df_selected_data_spread.Spread_bet_home_open) * 100
                if st.checkbox('Display selected data'):
                    df_selected_data_spread[['data', 'Season' , 'Home_Team' , 'Away_Team' ,'Home_Score' , 'Away_Score' ,'Home_Spread_Open', 'Spread_bet_home_open_Win']]
            else:
                df_selected_data = df[(df.Season == selected_season) & (df.Spread_Open_to_Close_Home == selected_line_movement) & (df.League == "NBA")]
                df_selected_data_spread = df_selected_data[(df_selected_data.Home_Spread_Close >= min_range) & (df_selected_data.Home_Spread_Close <= max_range)]
                chart_data = df_selected_data_spread.Spread_bet_home_close.cumsum()
                st.line_chart(chart_data)
                nuber_of_games = df_selected_data_spread.Spread_bet_home_close.count()
                number_of_wins = nuber_of_games - (np.sum(df_selected_data_spread.Spread_bet_home_close == -1))
                effectiveness = (number_of_wins / nuber_of_games) * 100
                roi = np.average(df_selected_data_spread.Spread_bet_home_close) * 100
                result_100_usd = np.sum(df_selected_data_spread.Spread_bet_home_close) * 100
                if st.checkbox('Display selected data'):
                    df_selected_data_spread[['data', 'Season' , 'Home_Team' , 'Away_Team' ,'Home_Score' , 'Away_Score' ,'Home_Spread_Close', 'Spread_bet_home_close_Win']]
        else:
            if open_or_close == "Open":
                df_selected_data = df[(df.Season == selected_season) & (df.Spread_Open_to_Close_Home != selected_line_movement) & (df.League == "NBA")]
                df_selected_data_spread = df_selected_data[(df_selected_data.Away_Spread_Open >= min_range) & (df_selected_data.Away_Spread_Open <= max_range)]
                chart_data = df_selected_data_spread.Spread_bet_away_open.cumsum()
                st.line_chart(chart_data)
                nuber_of_games = df_selected_data_spread.Spread_bet_away_open.count()
                number_of_wins = nuber_of_games - (np.sum(df_selected_data_spread.Spread_bet_away_open == -1))
                effectiveness = (number_of_wins / nuber_of_games) * 100
                roi = np.average(df_selected_data_spread.Spread_bet_away_open) *100
                result_100_usd = np.sum(df_selected_data_spread.Spread_bet_away_open) * 100
                if st.checkbox('Display selected data'):
                    df_selected_data_spread[['data', 'Season' , 'Home_Team' , 'Away_Team' ,'Home_Score' , 'Away_Score' ,'Away_Spread_Open', 'Spread_bet_away_open_Win']]
            else:
                df_selected_data = df[(df.Season == selected_season) & (df.Spread_Open_to_Close_Home != selected_line_movement) & (df.League == "NBA")]
                df_selected_data_spread = df_selected_data[(df_selected_data.Away_Spread_Close >= min_range) & (df_selected_data.Away_Spread_Close <= max_range)]
                chart_data = df_selected_data_spread.Spread_bet_away_close.cumsum()
                st.line_chart(chart_data)
                nuber_of_games = df_selected_data_spread.Spread_bet_away_close.count()
                number_of_wins = nuber_of_games - (np.sum(df_selected_data_spread.Spread_bet_away_close == -1))
                effectiveness = (number_of_wins / nuber_of_games) * 100
                roi = np.average(df_selected_data_spread.Spread_bet_away_close) *100
                result_100_usd = np.sum(df_selected_data_spread.Spread_bet_away_close) * 100
                if st.checkbox('Display selected data'):
                    df_selected_data_spread[['data', 'Season' , 'Home_Team' , 'Away_Team' ,'Home_Score' , 'Away_Score' ,'Away_Spread_Close', 'Spread_bet_away_close_Win']]
    else:
        if played_UO == "Under":
            if open_or_close == "Open":
                df_selected_data = df[(df.Season == selected_season) & (df.UO_Open_to_Close_Home == selected_line_movement_UO) & (df.League == "NBA")]
                df_selected_data_spread = df_selected_data[(df_selected_data.Under_Over_Open >= min_range) & (df_selected_data.Under_Over_Open <= max_range)]
                chart_data = df_selected_data_spread.Under_bet_open.cumsum()
                st.line_chart(chart_data)
                nuber_of_games = df_selected_data_spread.Under_bet_open.count()
                number_of_wins = nuber_of_games - (np.sum(df_selected_data_spread.Under_bet_open == -1))
                effectiveness = (number_of_wins / nuber_of_games) * 100
                roi = np.average(df_selected_data_spread.Under_bet_open) * 100
                result_100_usd = np.sum(df_selected_data_spread.Under_bet_open) * 100
                if st.checkbox('Display selected data'):
                    df_selected_data_spread[['data', 'Season' , 'Home_Team' , 'Away_Team' ,'Home_Score' , 'Away_Score' ,'Under_Over_Open', 'Under_bet_open_Win']]
            else:
                df_selected_data = df[(df.Season == selected_season) & (df.UO_Open_to_Close_Home == selected_line_movement_UO) & (df.League == "NBA")]
                df_selected_data_spread = df_selected_data[(df_selected_data.Under_Over_Close >= min_range) & (df_selected_data.Under_Over_Close <= max_range)]
                chart_data = df_selected_data_spread.Under_bet_close.cumsum()
                st.line_chart(chart_data)
                nuber_of_games = df_selected_data_spread.Under_bet_close.count()
                number_of_wins = nuber_of_games - (np.sum(df_selected_data_spread.Under_bet_close == -1))
                effectiveness = (number_of_wins / nuber_of_games) * 100
                roi = np.average(df_selected_data_spread.Under_bet_close) * 100
                result_100_usd = np.sum(df_selected_data_spread.Under_bet_close) * 100
                if st.checkbox('Display selected data'):
                    df_selected_data_spread[['data', 'Season' , 'Home_Team' , 'Away_Team' ,'Home_Score' , 'Away_Score' ,'Under_Over_Open', 'Under_bet_close_Win']]
        else:
            if open_or_close == "Open":
                df_selected_data = df[(df.Season == selected_season) & (df.UO_Open_to_Close_Home == selected_line_movement_UO) & (df.League == "NBA")]
                df_selected_data_spread = df_selected_data[(df_selected_data.Under_Over_Open >= min_range) & (df_selected_data.Under_Over_Open <= max_range)]
                chart_data = df_selected_data_spread.Over_bet_open.cumsum()
                st.line_chart(chart_data)
                nuber_of_games = df_selected_data_spread.Over_bet_open.count()
                number_of_wins = nuber_of_games - (np.sum(df_selected_data_spread.Over_bet_open == -1))
                effectiveness = (number_of_wins / nuber_of_games) * 100
                roi = np.average(df_selected_data_spread.Over_bet_open) * 100
                result_100_usd = np.sum(df_selected_data_spread.Over_bet_open) * 100
                if st.checkbox('Display selected data'):
                    df_selected_data_spread[['data', 'Season' , 'Home_Team' , 'Away_Team' ,'Home_Score' , 'Away_Score' ,'Under_Over_Open', 'Over_bet_open_Win']]
            else:
                df_selected_data = df[(df.Season == selected_season) & (df.UO_Open_to_Close_Home == selected_line_movement_UO) & (df.League == "NBA")]
                df_selected_data_spread = df_selected_data[(df_selected_data.Under_Over_Open >= min_range) & (df_selected_data.Under_Over_Open <= max_range)]
                chart_data = df_selected_data_spread.Over_bet_close.cumsum()
                st.line_chart(chart_data)
                nuber_of_games = df_selected_data_spread.Over_bet_close.count()
                number_of_wins = nuber_of_games - (np.sum(df_selected_data_spread.Over_bet_close == -1))
                effectiveness = (number_of_wins / nuber_of_games) * 100
                roi = np.average(df_selected_data_spread.Over_bet_close) * 100
                result_100_usd = np.sum(df_selected_data_spread.Over_bet_close) * 100
                if st.checkbox('Display selected data'):
                    df_selected_data_spread[['data', 'Season' , 'Home_Team' , 'Away_Team' ,'Home_Score' , 'Away_Score' ,'Under_Over_Open', 'Over_bet_close_Win']]
else:
    if played_UO == "Under":
        if open_or_close == "Open":
            df_selected_data = df[(df.Season == selected_season) & (df.UO_Open_to_Close_Home == selected_line_movement_UO)]
            df_selected_data_spread = df_selected_data[(df_selected_data.Under_Over_Open >= min_range) & (df_selected_data.Under_Over_Open <= max_range) & (df.League == "NHL")]
            chart_data = df_selected_data_spread.Under_bet_open.cumsum()
            st.line_chart(chart_data)
            nuber_of_games = df_selected_data_spread.Under_bet_open.count()
            number_of_wins = nuber_of_games - (np.sum(df_selected_data_spread.Under_bet_open == -1))
            effectiveness = (number_of_wins / nuber_of_games) * 100
            roi = np.average(df_selected_data_spread.Under_bet_open) * 100
            result_100_usd = np.sum(df_selected_data_spread.Under_bet_open) * 100
            if st.checkbox('Display selected data'):
                df_selected_data_spread[['data', 'Season' , 'Home_Team' , 'Away_Team' ,'Home_Score' , 'Away_Score' ,'Under_Over_Open', 'Under_bet_open_Win']]
        else:
            df_selected_data = df[(df.Season == selected_season) & (df.UO_Open_to_Close_Home == selected_line_movement_UO)]
            df_selected_data_spread = df_selected_data[(df_selected_data.Under_Over_Close >= min_range) & (df_selected_data.Under_Over_Close <= max_range) & (df.League == "NHL")]
            chart_data = df_selected_data_spread.Under_bet_close.cumsum()
            st.line_chart(chart_data)
            nuber_of_games = df_selected_data_spread.Under_bet_close.count()
            number_of_wins = nuber_of_games - (np.sum(df_selected_data_spread.Under_bet_close == -1))
            effectiveness = (number_of_wins / nuber_of_games) * 100
            roi = np.average(df_selected_data_spread.Under_bet_close) * 100
            result_100_usd = np.sum(df_selected_data_spread.Under_bet_close) * 100
            if st.checkbox('Display selected data'):
                df_selected_data_spread[['data', 'Season' , 'Home_Team' , 'Away_Team' ,'Home_Score' , 'Away_Score' ,'Under_Over_Close', 'Under_bet_close_Win']]
    else:
        if open_or_close == "Open":
            df_selected_data = df[(df.Season == selected_season) & (df.UO_Open_to_Close_Home == selected_line_movement_UO)]
            df_selected_data_spread = df_selected_data[(df_selected_data.Under_Over_Open >= min_range) & (df_selected_data.Under_Over_Open <= max_range) & (df.League == "NHL")]
            chart_data = df_selected_data_spread.Over_bet_open.cumsum()
            st.line_chart(chart_data)
            nuber_of_games = df_selected_data_spread.Over_bet_open.count()
            number_of_wins = nuber_of_games - (np.sum(df_selected_data_spread.Over_bet_open == -1))
            effectiveness = (number_of_wins / nuber_of_games) * 100
            roi = np.average(df_selected_data_spread.Over_bet_open) * 100
            result_100_usd = np.sum(df_selected_data_spread.Over_bet_open) * 100
            if st.checkbox('Display selected data'):
                df_selected_data_spread[['data', 'Season' , 'Home_Team' , 'Away_Team' ,'Home_Score' , 'Away_Score' ,'Under_Over_Open', 'Over_bet_open_Win']]
        else:
            df_selected_data = df[(df.Season == selected_season) & (df.UO_Open_to_Close_Home == selected_line_movement_UO)]
            df_selected_data_spread = df_selected_data[(df_selected_data.Under_Over_Close >= min_range) & (df_selected_data.Under_Over_Close <= max_range) & (df.League == "NHL")]
            chart_data = df_selected_data_spread.Over_bet_close.cumsum()
            st.line_chart(chart_data)
            nuber_of_games = df_selected_data_spread.Over_bet_close.count()
            number_of_wins = nuber_of_games - (np.sum(df_selected_data_spread.Over_bet_close == -1))
            effectiveness = (number_of_wins / nuber_of_games) * 100
            roi = np.average(df_selected_data_spread.Over_bet_close) * 100
            result_100_usd = np.sum(df_selected_data_spread.Over_bet_close) * 100
            if st.checkbox('Display selected data'):
                df_selected_data_spread[['data', 'Season' , 'Home_Team' , 'Away_Team' ,'Home_Score' , 'Away_Score' ,'Under_Over_Close', 'Over_bet_close_Win']]


effectiveness_display = round(effectiveness, 2)
roi_display = round(roi, 2) 
result_100_usd_display = round(result_100_usd, 2)

st.header("**Statistics**")

statistics_table = pd.DataFrame({'*Result based on selected options*': 
                                    [nuber_of_games,number_of_wins,effectiveness_display,roi_display,result_100_usd_display]}, 
                                    index = ['Number of games:',
                                    'Number of wins:',
                                    'Percentage of winning bets (%):',
                                    'ROI (%):',
                                    'Result at 100$ per bet:'])
statistics_table

st.markdown('___')

how_to_use = st.expander('How to use Betsing app?')
with how_to_use:
    
    st.text(''' 
    To analyse the betting market you have to choose the conditions which you like to check.
    
      *League: in beta version 3.1 only leagues available are NBA and NHL
      *Season: select one of the seasons which you want to analyse - new season will be add 
      in production version of Betsting
      *Bet type: in beta version 3.1 only markets available are Spread and Under/Over
      *Team played: available for Spread bet type. Choose if you wan to bet on Home or
      Away team
      *Under or Over?: available for Under/Over bet type. Choose if you wan to bet on Under or
      Over bet
      *Based on Open Odds or Close Odds?: Choose if you want to see the result of the anaylysis 
       based of open or close odds
      *Is open odds line bigger than close odds?: this option shows whether the opening price 
       was higher than the closing price. It shows in which direction the market is going
      *Spread Range: available for Spread bet type. Choose what range of spread you 
      want to anaylse
      *Under/Over Range: vailable for Under/Over bet type. Choose what range of spread 
      you want to anaylse
    ''')
        

interpretation = st.expander('How to interpret the result?')
with interpretation:
    st.text(''' 

    Betsting will not built betting model for you. Betsting will present market trends, 
    dependencies and present to you new way of looking into the betting market. 
    Based on information and analysis made on Betsting you can build and optimaze 
    your own model. Use your creativity to find your edge.

    The result are presented like you will play on every match based of 
    option you choose. You can change the filter to see all result 
    based of different approaches.

    The Chart of the top will show you result of the betting based of your 
    selected result. Find out more about all options on "How to use Betsting app" section. 

    Clisk Checkbox "Display selected data" to see and analyse all match witch 
    matched your filers. You can see information and statisctics like: 
    Home and away team, date, points, spread, result based of choosen options and more. 

    The Statisctics table present main statistics about selected bets like: 
    number of games, number of wins, prercentage of winning bets (efficiency) and 
    simulate how much will you win or loose if you will play
    based of your selected optoons 100$ on every game. 
    ROI (return of investment) present how much will you 
    earn/loose on avrage on every game.

    ''')

about = st.expander('About Betsting')
with about:
    st.text(''' 
    
    Betsting is a backtesting sport betting app that allow you to test 
    your betting idea and help you work on your betting models.

    You see beta version 3.1 of our app, 
    if you like the idea or have any comments drop us email at contact.betsting@gmail.com. 
    We still work on other sports, leagues, markets and functionalities.
    ''')
    st.write('Find out more about Betsting on [www.betsting.com](https://betsting.com/)')
    st.write('Follow us on [Twitter](https://twitter.com/betsting)')

