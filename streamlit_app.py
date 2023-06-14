#import libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
#import plotly.figure_factory as ff

#look for more information here https://docs.streamlit.io/library/cheatsheet

#adding title
st.title("Cameron is a superstar Basketball player!")

#adding discription to your website
st.text('eastliverpool potters')



#SHOWING THE DATA
#dataset Header
st.header('Dataset')

#add your dataset (delete dataset this is an example)
df = pd.read_csv("cbb.csv")

#showing dataset
st.table(df.head())


## Data Description


st.write("""1. CONF : The Athletic Conference in which the school participates in 
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
st.header('Cleaning and Pre-processing the data')

st.table(df.info())
#Adding 3-6 Visualizations using photos collected and made from your graph
#adding images
#adding graphs by images
st.header('Gemma Question : How many games have Gonzaga won over different seasons? ')

## Filtering out the team gonzaga from our dataset 
df_plot=df[df['TEAM']=='Gonzaga']
## We want to Sum the number of wins by the team gonzaga for each year.
count = df_plot.groupby("YEAR")[["W"]].sum().reset_index()
count = count.sort_values(by="W", ascending=False).head(15)
fig = px.bar(count, x="YEAR", y="W")
fig.update_layout(xaxis_tickangle=-90)
st.plotly_chart(fig)

st.header("Gemma Question : what was North Carolina's power rating in 2016?? ")

df_plot=df[df['TEAM']=='North Carolina']
pr = df_plot.groupby("YEAR")[["BARTHAG"]].sum().reset_index()
pr.sort_values(by="BARTHAG", ascending=False).head(15)
fig = px.bar(count, x="YEAR", y="BARTHAG")
fig.update_layout(xaxis_tickangle=-90)
st.plotly_chart(fig)

st.header('Cameron Conley Question : How many freethrows have the lakers made? ')
st.header('Melanie Question : what was texas tech free throw rate in 2019 ')

st.header('Livia Question : how many games has the wissconson played in the year of 2015?')
st.header('Cameron Estell : what was the point shooting percentage last season for the wisconsin')
st.header('Natalia Question : what was gonzas turn over percentage commited in 2017')
#adding graphs by making plotly_Chart
# Plot!
#st.plotly_chart(BostonHousing, use_container_width=True)
#st.text('Discription')


#adding conclusions
st.header('Conclusion')
st.text('add your conclusion here')