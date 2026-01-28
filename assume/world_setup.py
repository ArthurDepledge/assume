# Import necessary packages
import logging
import os

import numpy as np
import pandas as pd
import yaml

# import the main World class and the load_scenario_folder functions from assume
from assume import World
from assume.scenario.loader_csv import load_scenario_folder
from data_formatting import auto_timeslices

# Set up logging
log = logging.getLogger(__name__)

# Define paths for input and output data
csv_path = "outputs"
input_path = "inputs/example_01"

# Create directories if they don't exist
os.makedirs("local_db", exist_ok=True)

# Set the random seed for reproducibility
np.random.seed(0)

# define the database uri. In this case we are using a local sqlite database
db_uri = "sqlite:///local_db/assume_db1.db"


# Generate random demand values around 2000
#demand_values = np.random.normal(loc=2000, scale=200, size=8 * 24)


#availability_profile = pd.DataFrame({"datetime": date_range, "Unit 1": 0})
#availability_profile.to_csv(f"{input_path}/availability_df.csv", index=False)

auto_timeslices(file_name="demand_df.csv", input_path=input_path)

# create world instance
world = World(database_uri=db_uri, export_csv_path=csv_path)

# load scenario by providing the world instance
# the path to the inputs folder and the scenario name (subfolder in inputs)
# and the study case name (which config to use for the simulation)
load_scenario_folder(
    world,
    inputs_path="inputs", # not the variable input_path - defining the name of the folder in ASSUME to get the input data from
    scenario="example_01", # specifies the subfolder within inputs
    study_case="daily_market",
)

# run the simulation
world.run()