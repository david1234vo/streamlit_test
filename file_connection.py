import csv
import numpy as np
import pandas as pd
import glob
import os

"""
def get_data_from_file():
    

    #list_of_files = glob.glob('C:\\Users\\Tester\\Documents\\upc\\efficient use\\10_11\\*')
    
    #list_of_files = glob.glob('.\\csv_data\\data_11_1_16_21.csv')
    #latest_file = "current"
    #while "current" in latest_file:
    #    latest_file = max(list_of_files, key=os.path.getctime)
    #    list_of_files.pop(list_of_files.index(latest_file))
    print("why is this not printing")
    print("lof1", glob.glob("\\"))
    print("lof2", glob.glob(".\\"))
    print("lof3", glob.glob("."))
    latest_file = '\\csv_data\\data_11_1_16_21.csv'
    
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
    """

def get_data_from_file():
    df = pd.DataFrame({
        'time': [1,2,3],
        'temperature': [1,2,3],
        "controlSignal": [1,0.5,0],
        "heater": [1,1,0]
        })

#get_data_from_file()
#print("")
