""" This script store the function required to stream data from the API of your choice"""

import requests
import json
import pandas as pd
import numpy as np

import pandas as pd
import numpy as np

# create GET request

def get_data_from_api():
    
    wind = []
    solar = []
    combined = []
    co = []

    for j in range(11,12):
        for i in range(1,24):
            
            month = str(j)
            date = str(i)
            print("retrieving: "+date+"/"+month)
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

    return np.array([wind, solar, combined, co]).transpose()

