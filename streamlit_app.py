import streamlit as st
from collections import namedtuple
import math
import pandas as pd
import numpy as np
import plost                # this package is used to create plots/charts within streamlit
from PIL import Image       # this package is used to put images within streamlit
from file_connection import get_data_from_file
#from streamlit_autorefresh import st_autorefresh


#from api_connection import get_data_from_api       # keep this commented if not using it otherwise brakes the app



# Page setting
st.set_page_config(layout="wide")

#st_autorefresh(interval=5000, limit=100)

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



chart_data = pd.DataFrame(
    get_data_from_file().rename(columns={'time':'index'}).set_index('index'),
    columns=['temperature', 'controlSignal', 'heater'])

st.markdown("<h1 style='text-align: center; color: grey;'>SMART AQUARIUM DATA</h1>", unsafe_allow_html=True)
st.line_chart(chart_data)
