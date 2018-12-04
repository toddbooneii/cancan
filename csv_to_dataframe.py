'''
Filename:       csv_to_dataframe.py
Group Members:  Andrew Zolintakis, Frank Longo, Jonah Woods, Peter Awori, Todd Boone, Jackson Brietke
Description:    Two methods return one or two dataframes from csv files
Imported By:    gui.py 
Imports:        Pandas
'''

import pandas as pd

# Create a recyclable materials dataframe and lcoations dataframe
def get_dataframes(materials_filename, locations_filename):
    materials_df = pd.read_csv(materials_filename, index_col="Material Name")
    locations_df = pd.read_csv(locations_filename, index_col = "name")
    return materials_df.iloc[:,:3], locations_df

def get_dataframe(materials_filename):
    materials_df = pd.read_csv(materials_filename, index_col="Material Name")
    return materials_df.iloc[:,:3]


# Test module
if(__name__ == '__main__'):
    materials_filename = "Waste_Recycling.csv"
    locations_filename = "Locations.csv"
    mats, locs = get_dataframes(materials_filename, locations_filename)
    # print(mats.shape)
    print(locs.shape)
    # print(mats.head())
    print(locs.head())
