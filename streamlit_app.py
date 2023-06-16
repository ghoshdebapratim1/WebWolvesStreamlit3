#import libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
#import plotly.figure_factory as ff

#look for more information here https://docs.streamlit.io/library/cheatsheet
#adding title
st.title("Basketball over the years")

#adding discription to your website
st.write('All about basketball')


st.header('Team Members')

st.markdown("- Gemma")
st.markdown("- Cameron Estell")
st.markdown("- Cameron Conely")
st.markdown("- Livia")
st.markdown("- Natalia")
st.markdown("- Melanie")

#SHOWING THE DATA
#dataset Header
st.header('Dataset')

#add your dataset (delete dataset this is an example)
df = pd.read_csv("cbb.csv")

#showing dataset
st.table(df.head())


## Data Description

st.header('Dataset Column Description')

st.write("""
0. TEAM : Team Name 
1. CONF : The Athletic Conference in which the school participates in 
2.G : Number of Games playesd
3.W :  Number of Games Won 
4. ADJOE : Points scored per 100 possessions 
5. ADJDE : Adjusted Defensive Efficiency 
6. BARTHAG : Power Rating 
7. EFG_O : Effective Field Goal Percentage Shot
8. EFG_D : Effective Field Goal Percentage Allowed
9.TOR : Turnover Percentage Allowed
10. TORD : Turnover Percentage Committed
11. ORB : Offensive Rebound Rate 
12. DRB : Defensive Rebound Rate 
13. FTR : Free Throw Rate 
14. FTRD : Free throw Rate Allowed 
15. 2P_O : Two Point Shooting Percentage 
16. 2P_D : Two Point Shooting Percentage allowed 
17. 3P_O: 3 Point shooting percentage 
18. 3P_D: 3 point shooting perecentage allowed 
19. ADJ_T : Adjusted Tempo 
20. WAB : Wins above bubble 
21. POSTSEASON : Round where the given team was eliminated or where their season ended
22. SEED : Seed in the NCAA Tournament
23. Year : Season """)
#Adding images to make your streamlit look visually better!
# st.image('pro.png')
# st.text('You can add photos with descriptions')


st.table(df.info())
#Adding 3-6 Visualizations using photos collected and made from your graph
#adding images
#adding graphs by images

st.header('How are the number of games won distributed? ')

## Box Plot 
df_plot=df['G']

fig = px.box(df_plot, y="G")
 
fig.update_layout(xaxis_tickangle=-90)
st.plotly_chart(fig)

st.write('The 75th percentile (or upper quantile) is 37 , the median is 31 and the lower quantile is 26.')
## Histogram 
#df.hist(bin=5)

fig=px.histogram(df_plot,'G')

st.plotly_chart(fig)

st.write(" Most teams have played games between 24 and 40 games")

###### Scatter Plot 
st.header('Relationship between games won and ADJOE')

df_plot=df[['W','ADJOE']]
fig=px.scatter(df_plot,x='W',y='ADJOE')
fig.update_layout(xaxis_tickangle=-90)
st.plotly_chart(fig)

st.write('If in a game a team have a higher amount of points scored it is highly likely that team will win the game. ')


###### Bar Chart Plot 
st.header('Defensive Rebound rate of the top 15 teams')

df_plot=df[['TEAM','DRB']]
## We want to Sum the number of wins by the team gonzaga for each year.
avgdrb = df_plot.groupby("TEAM")[["DRB"]].mean().reset_index()
avgdrb = avgdrb.sort_values(by="DRB", ascending=False).head(15)
fig = px.bar(avgdrb, x="TEAM", y="DRB")
fig.update_layout(xaxis_tickangle=-90)
st.plotly_chart(fig)

st.write("Fairleigh Dicknson is the most defensive team.")


#### Pie Chart 

st.header('Which conference has the highest number of games?')

df_plot=df[['CONF','G']]

totConf=df_plot.groupby("CONF")[['G']].sum().reset_index()
fig = px.pie(totConf,values="G",names="CONF")
st.plotly_chart(fig)


st.write('The three conferences with the highest games played is ACC, SEC, and A10')


### Heatmap 

# st.header('Team vs Conference Games Won Heatmap ')

# df_plot=df[['TEAM','CONF','W']]

# gamesWon=df_plot.groupby(['TEAM','CONF'])[['W']].sum().reset_index()

# gamesWon=pd.pivot_table(gamesWon, values = 'W', index=['TEAM'], columns = 'CONF').reset_index()

# fig = px.imshow(gamesWon)
# st.plotly_chart(fig)


st.header('How many games have Gonzaga won over different seasons? ')

## Filtering out the team gonzaga from our dataset 
df_plot=df[df['TEAM']=='Gonzaga']
## We want to Sum the number of wins by the team gonzaga for each year.
count = df_plot.groupby("YEAR")[["W"]].sum().reset_index()
count = count.sort_values(by="W", ascending=False).head(15)
fig = px.bar(count, x="YEAR", y="W")
fig.update_layout(xaxis_tickangle=-90)
st.plotly_chart(fig)

st.markdown("- The most games Gonzaga have won in a season is 37. ")
st.markdown("- the least amount of games they have won is 27 ")
st.markdown("- the season they won the most was 2017")

st.header("what was North Carolina's power rating in 2016?? ")

df_plot=df[df['TEAM']=='North Carolina']
pr = df_plot.groupby("YEAR")[["BARTHAG"]].sum().reset_index()
pr.sort_values(by="BARTHAG", ascending=False).head(15)
fig = px.bar(pr, x="YEAR", y="BARTHAG")
fig.update_layout(xaxis_tickangle=-90)
st.plotly_chart(fig)

st.header('what was the point shooting percentage last season for the wisconsin')

df_plot=df[df['TEAM']=='Wisconsin']

df_plot=df_plot[['YEAR','2P_O']]

twopo=df_plot.groupby('YEAR')[['2P_O']].mean().reset_index()

fig=px.bar(twopo,x="YEAR",y='2P_O')
st.plotly_chart(fig)

st.header('What is the relationship between offensive rebound rate and defensive rebound rate')

df_plot=df[['ORB','DRB']]
fig=px.scatter(df,x='ORB',y='DRB')
fig.update_layout(xaxis_tickangle=-90)
st.plotly_chart(fig)


st.header('Which team has the highest power rating in 2019?')

df_plot=df[df['YEAR']==2019]
power_rating=df_plot.groupby('TEAM')['BARTHAG'].max().reset_index()
power_rating=power_rating.sort_values(by='BARTHAG',ascending=False).head(15)
fig=px.bar(power_rating,x='TEAM',y='BARTHAG')
fig.update_layout(xaxis_tickangle=-90)
st.plotly_chart(fig)



#adding graphs by making plotly_Chart
# Plot!
#st.plotly_chart(BostonHousing, use_container_width=True)
#st.text('Discription')


#adding conclusions
st.header('Conclusion')
st.text('add your conclusion here')