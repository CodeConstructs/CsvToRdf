from glob import glob
import os
import pandas as pd


def import_files():
    data_dict = {}
    csvs = glob("./Files/*.csv")
    for csv_file in csvs:
        name = os.path.basename(csv_file)[:-4]

        values = pd.read_csv(csv_file, sep=",")

        values.columns = [col.replace(" ", "_") for col in values.columns]

        data_dict[name] = values

    return data_dict
