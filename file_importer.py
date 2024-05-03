from glob import glob
import pandas as pd
import os

def importFiles():
    data_dict = {}
    csvs = glob('./Files/*.csv')
    for csv_file in csvs:
        name = os.path.basename(csv_file)[:-4]

        values = pd.read_csv(csv_file, sep=",")
  
        values.columns = [col.replace(" ", "_") for col in values.columns]

        data_dict[name] = values

    return data_dict
   
