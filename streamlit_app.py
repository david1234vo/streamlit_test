import streamlit as st
from collections import namedtuple
import math
import pandas as pd
import numpy as np
import plost                # this package is used to create plots/charts within streamlit
from PIL import Image       # this package is used to put images within streamlit
from file_connection import get_data_from_file
#from streamlit_autorefresh import st_autorefresh
import glob


#from api_connection import get_data_from_api       # keep this commented if not using it otherwise brakes the app

print("starting app")

# Page setting
st.set_page_config(layout="wide")

#st_autorefresh(interval=5000, limit=100)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

print("printing now??")

# import requests library
import requests 
import json
# import plotting library
import matplotlib
import matplotlib.pyplot as plt 
from datetime import date, datetime, timedelta
import pprint

print("and now?")

print("lof1", glob.glob("/"))
print("lof2", glob.glob("./"))
print("lof3", glob.glob("."))

chart_data = pd.DataFrame(
    get_data_from_file().rename(columns={'time':'index'}).set_index('index'),
    columns=['temperature', 'controlSignal', 'heater'])

st.markdown("<h1 style='text-align: center; color: grey;'>SMART AQUARIUM DATA</h1>", unsafe_allow_html=True)
st.line_chart(chart_data)
