import logging
import os

import numpy as np
import pandas as pd

input_path = "inputs/UK_basic"

def auto_timeslices(file_name, input_path):
    file = pd.read_csv(f"{input_path}/{file_name}")
    if (file["datetime"].iloc[1]).split()[0].isdigit():

        timeslice = (file["datetime"].iloc[1]).split()
        start_date = file["datetime"].iloc[0]
        data = file.drop(labels=["datetime"], axis="columns")

        if timeslice[1] in ["years", "year"]:
            date_range = pd.date_range(start=start_date, periods = len(data), freq=f"{timeslice[0]}y")
            

        elif timeslice[1] in ["months", "month"]:
            date_range = pd.date_range(start=start_date, periods = len(data), freq=f"{timeslice[0]}m")


        elif timeslice[1] in ["days","day"]:
            date_range = pd.date_range(start=start_date, periods = len(data), freq=f"{timeslice[0]}D")


        elif timeslice[1] in ["hours","hour"]:
            date_range = pd.date_range(start=start_date, periods = len(data), freq=f"{timeslice[0]}h")


        elif timeslice[1] in ["minutes", "minute"]:
            date_range = pd.date_range(start=start_date, periods = len(data), freq=f"{timeslice[0]}min")


        elif timeslice[1] in ["seconds", "second"]:
            date_range = pd.date_range(start=start_date, periods = len(data), freq=f"{timeslice[0]}s")
        
        else:
            raise Exception("Unrecognised time unit or incorrect date format")

        profile = pd.DataFrame({"datetime": date_range})
        profile = pd.concat([profile,data],axis=1)
        profile.to_csv(f"{input_path}/{file_name}", index=False)

auto_timeslices(file_name="demand_df.csv", input_path=input_path)