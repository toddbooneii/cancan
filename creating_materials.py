import pandas as pd


def create_materials_df():  # this function creates our materials DF
    # This takes our custom types and puts it into a DF
    adding_types_df = pd.read_csv('mat_list_csv.csv', delimiter=',')
    # This takes the current JSON file from the web
    materials_df = pd.read_json('https://data.edmonton.ca/resource/kx42-g5ky.json')
    materials_df['Location Category'] = 'None'  # adding custom category column to JSON data
    materials_df['Type'] = 'None'  # adding custom category column to JSON data

    for rows, columns in adding_types_df.iterrows():
        try:
            for x, y in materials_df.iterrows():  # if there is a match of material titles add the custom categories to them
                if(adding_types_df.loc[rows]['Material Title'] == materials_df.loc[x]['material_title']):
                    materials_df.loc[x]['Location Category'] = adding_types_df.loc[rows]['Location Category']
                    materials_df.loc[x]['Type'] = adding_types_df.loc[rows]['Type']
                    break
        except UnicodeEncodeError:  # There is a UnicodeEncodeError when parsing file for some rows
            print('ERROR\n\nERROR\n\nERROR\n\nERROR\n\nERROR\n\n')
    return materials_df


def change_names(location_df):  # changing column names of Locations DF
    change_names = {
        "accepts_alkaline_batteries": "Batteries",
        "accepts_cfl_lightbulbs": "Lightbulbs",
        "accepts_clothing": "Clothing",
        "accepts_computers_and_peripherals": "Computers",
        "accepts_construction_and_demolition_waste": "Construction",
        "accepts_household_chemicals_and_waste": "Chemicals",
        "accepts_household_recyclables": "Household",
        "accepts_plastic_bags_and_films": "Plastic",
        "accepts_prescription_medication": "prescription_medication",
        "accepts_scrap_metal": "Scrap Metals",
        "accepts_tires": "Tires",
        "accepts_tvs_and_monitors": "tv",
        "accepts_yard_debris": "Yard",
        "accepts_general_electronics": "Electronics",
        "accepts_ink_and_toner": "Ink",
        "accepts_motor_oil": "motor oil"
    }
    location_df.rename(columns=change_names, inplace=True)
    return location_df


def create_locations_df():
    excess_columns = ['inactive', 'neighborhood', 'council_district', 'ward',
                      'tract', 'public_works_division', 'pli_division',
                      'police_zone', 'fire_zone', 'latitude', 'longitude']  # These columns are not needed for our app

    # reading stored Allegheny Recyclable Locations file
    location_df = pd.read_csv('allegheny_locations.csv', delimiter=',')
    location_df = location_df.drop(excess_columns, axis=1)  # dropping extra columns
    location_df = change_names(location_df)
    return location_df


# Find all of the locations that takes this material
def find_locations_that_accept_material(location_df, material):
    location_matches = []
    for x, y in location_df.iterrows():
        if(y[material] == 't'):
            location_info = {
                "name": y["name"],
                "address_number": y["address_number"],
                "street":  y["street"],
                "city": y["city"]
            }
            location_matches.append(location_info)
    return location_matches  # list of location dicts
