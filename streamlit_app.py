#import libraries
import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
#import numpy as np
#import plotly.figure_factory as ff

#look for more information here https://docs.streamlit.io/library/cheatsheet

#adding title
st.title("Cameron is a superstar Basketball player!")

#adding discription to your website
st.text('eastliverpool potters')

#Thesis here
st.header('Thesis')
st.text('Add your Thesis here')


#SHOWING THE DATA
#dataset Header
st.header('Dataset')

#add your dataset (delete dataset this is an example)
BostonHousing = pd.read_csv("BostonHousing.csv")


#adding graphs by making plotly_Chart
# Plot!
#st.plotly_chart(BostonHousing, use_container_width=True)
#st.text('Discription')


#adding conclusions
st.header('Conclusion')
st.text('add your conclusion here')