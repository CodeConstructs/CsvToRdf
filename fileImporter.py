from glob import glob
import pandas as pd

dict = {'':''}

def importFiles ():
    csvs = glob('./Files/*.csv')
    for csv in csvs:
        name = csv[8:-4]
        values = pd.read_csv(csv, sep="|")
        dict[name] = values

    return dict
   
