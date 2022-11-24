import streamlit as st
from collections import namedtuple
import math
import pandas as pd
import numpy as np
import plost                # this package is used to create plots/charts within streamlit
from PIL import Image       # this package is used to put images within streamlit

#from api_connection import get_data_from_api       # keep this commented if not using it otherwise brakes the app

# Page setting
st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Data
seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')
# replace the previous data with your own streamed data from API

# import requests library
import requests 
import json
# import plotting library
import matplotlib
import matplotlib.pyplot as plt 
from datetime import date, datetime, timedelta
import pprint


wind = []
solar = []
combined = []
co = []

for j in range(11,12):
    for i in range(1,24):
        
        month = str(j)
        date = str(i)
        print("retrieving: "+date+"/"+month)
        if month == 11 and date == 17:
            break
        endpoint = 'https://apidatos.ree.es'
        #real time market price
        #get_archives = '/en/datos/mercados/precios-mercados-tiempo-real'
        get_archives = '/en/datos/generacion/estructura-generacion'
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json',
                   'Host': 'apidatos.ree.es'}
        params = {'start_date': '2022-'+month+'-'+date+'T00:00', 'end_date': '2022-'+month+'-'+date+'T23:00', 'time_trunc':'year'}

        response = requests.get(endpoint+get_archives, headers=headers, params=params)
        json = response.json()

        total_percentage = 0
        titles = []
        percentages = []
        comb = 0
        for i in range(len(json["included"])):
            
            t = json["included"][i]['attributes']['title']
            if t != 'Total generation':
                titles.append(t)
                p = json["included"][i]['attributes']['values'][0]['percentage']
                percentages.append(float(p)*100)
                #print(t,":",p)
                total_percentage += p
                if t == "Wind":
                    wind.append(p)
                    comb += float(p)
                if t == "Solar photovoltaic":
                    solar.append(p)
                    comb += float(p)
                if t == "Combined cycle":
                    combined.append(p)
                    comb += float(p)
        co.append(comb)
                
        #print(total_percentage)

import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.array([wind, solar, combined, co]).transpose(),
    columns=['wind', 'solar', 'gas', 'total'])

st.line_chart(chart_data)


"""
### Here starts the web app design
# Row A
a1, a2, a3, a4 = st.columns(4)
a1.image(Image.open('streamlit-logo-secondary-colormark-darktext.png'))
a2.metric("Wind", "9 mph", "-8%")
a3.metric("Humidity", "86%", "4%")
a4.metric("Humidity", "2%", "40%")

# Row B
b1, b2, b3, b4 = st.columns(4)
b1.metric("Temperature", "70 °F", "1.2 °F")
b2.metric("Wind", "9 mph", "-8%")
b3.metric("Humidity", "86%", "4%")
b4.metric("Humidity", "86%", "4%")

# Row C
c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Heatmap')              # text is created with markdown
    plost.time_hist(                        # histogram
    data=seattle_weather,
    date='date',
    x_unit='week',
    y_unit='day',
    color='temp_max',
    aggregate='median',
    legend=None)
with c2:
    st.markdown('### Bar chart')
    plost.donut_chart(                      # donut charts
        data=stocks,
        theta='q2',
        color='company')
"""