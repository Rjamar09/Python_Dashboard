import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from PIL import Image


df=pd.read_csv("covid_data.csv")
df.sort_values(by="Confirmed Cases",ascending=False,inplace=True)
cured_discharged=df.sort_values(by="Cured/Discharged",ascending=False)
Active_cases=df.sort_values(by="Active Cases",ascending=False)
Death_cases=df.sort_values(by="Death",ascending=False)


st.title("Covid-19 Dashboard For India")
st.subheader('The dashboard will visualize the Covid-19 Situation in India')
st.markdown('Coronavirus disease 2019 (COVID-19) is a contagious disease caused by a virus, the severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The first known case was identified in Wuhan, China, in December 2019. The disease quickly spread worldwide, resulting in the COVID-19 pandemic.')
st.markdown('COVID‑19 transmits when people breathe air contaminated by droplets and small airborne particles containing the virus. The risk of breathing these is highest when people are in close proximity, but they can be inhaled over longer distances, particularly indoors.')
st.markdown('Symptoms of COVID‑19 are variable, but often include fever, cough, headache, fatigue, breathing difficulties, loss of smell, and loss of taste. Symptoms may begin one to fourteen days after exposure to the virus.')
st.sidebar.title("Visualization Selector")
st.sidebar.markdown("Select the Charts/Plots accordingly:")

image = Image.open('india_map.jpg')
st.image(image,caption='Map of India')





select = st.sidebar.selectbox('Visualization type', ['Area chart','Pie chart','Bar plot',], key='0')
if not st.sidebar.checkbox("Hide", True, key='1'):
    if select == 'Pie chart':
        st.title("Top 10 States with most Confirmed Covid Cases")
        fig = px.pie(df, values=df['Confirmed Cases'][:10], names=df['State/UT'][:10], title='Total Confirmed Cases')
        st.plotly_chart(fig)

        st.title("Top 10 States with most Active Cases")
        fig = px.pie(Active_cases, values=Active_cases['Active Cases'][:10], names=Active_cases['State/UT'][:10], title='Total Active Cases')
        st.plotly_chart(fig)

        st.title("Top 10 States with most Recovered Cases")
        fig = px.pie(cured_discharged,values=cured_discharged['Cured/Discharged'][:10], names=cured_discharged['State/UT'][:10], title='Total Cured/Discharged')
        st.plotly_chart(fig)

        st.title("Top 10 States with most Covid Deaths")
        fig = px.pie(Death_cases,values=Death_cases['Death'][:10],names=Death_cases['State/UT'][:10],title="Total Deaths")
        st.plotly_chart(fig)

    if select == 'Area chart':
        st.title("States with most Confirmed Covid Cases")
        fig=px.area(df,x='State/UT',y='Confirmed Cases')
        st.plotly_chart(fig)

        st.title("States with most Active Cases")
        fig=px.area(df,x='State/UT',y='Active Cases')
        st.plotly_chart(fig)

        st.title("State with most Recovered Cases")
        fig = px.area(df,x='State/UT',y='Cured/Discharged')
        st.plotly_chart(fig)

        st.title("State with most Covid Deaths")
        fig = px.area(df, x='State/UT', y='Death')
        st.plotly_chart(fig)


    if select == 'Bar plot':
        st.title("Top 10 States with most Confirmed and Rescovered cases")
        fig = go.Figure(data=[
            go.Bar(name='Confirmed Cases', x=df['State/UT'][:10], y=df['Confirmed Cases'][:10]),
            go.Bar(name='Cured/Discharged', x=df['State/UT'][:10], y=df['Cured/Discharged'][:10])])
        st.plotly_chart(fig)

        st.title('Top 10 States with most Active and Death cases')
        fig = go.Figure(data=[
            go.Bar(name='Active Cases',x=df['State/UT'][:10],y=df['Active Cases'][:10]),
            go.Bar(name='Death',x=df['State/UT'][:10],y=df['Death'][:10])])
        st.plotly_chart(fig)


