import csv
import numpy as np
import pandas as pd
import glob
import os

def get_data_from_file():
    

    list_of_files = glob.glob('C:\\Users\\Tester\\Documents\\upc\\efficient use\\10_11\\*')
    latest_file = "current"
    while "current" in latest_file:
        latest_file = max(list_of_files, key=os.path.getctime)
        list_of_files.pop(list_of_files.index(latest_file))
    
    with open(latest_file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        time = []
        temp = []
        ctrl = []
        heater = []

        for element in list(spamreader):
            
            d = element[0].split(",")
            if 'Irms' not in d:
                time.append(float(d[0])) 
                temp.append(float(d[2])) 
                ctrl.append(float(d[4])) 
                heater.append(float(d[6])) 
    df = pd.DataFrame({
        'time': time,
        'temperature': temp,
        "controlSignal": ctrl,
        "heater": heater
        })


    return df

#get_data_from_file()
#print("")