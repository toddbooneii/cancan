import pandas as pd


def create_materials_df():
    adding_types_df = pd.read_csv('mat_list_csv.csv', delimiter=',')
    materials_df = pd.read_json('https://data.edmonton.ca/resource/kx42-g5ky.json')
    materials_df['Location Category'] = 'None'
    materials_df['Type'] = 'None'

    for rows, columns in adding_types_df.iterrows():
        try:
            for x, y in materials_df.iterrows():
                if(adding_types_df.loc[rows]['Material Title'] == materials_df.loc[x]['material_title']):
                    materials_df.loc[x]['Location Category'] = adding_types_df.loc[rows]['Location Category']
                    materials_df.loc[x]['Type'] = adding_types_df.loc[rows]['Type']
                    break
        except UnicodeEncodeError:
            print('ERROR\n\nERROR\n\nERROR\n\nERROR\n\nERROR\n\n')
    return materials_df


# create_materials_df().to_csv('blah.txt')
temp_materials = pd.read_csv('blah.txt', delimiter=',')


def create_locations_df():
    excess_columns = ['inactive', 'neighborhood', 'council_district', 'ward',
                      'tract', 'public_works_division', 'pli_division',
                      'police_zone', 'fire_zone', 'latitude', 'longitude']
    location_df = pd.read_csv('allegheny_locations.csv', delimiter=',')
    location_df = location_df.drop(excess_columns, axis=1)
    return location_df


temp_locations = create_locations_df()
# for x, y in temp_materials.iterrows():
# print(x)
# print(y)
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
temp_locations.rename(columns=change_names, inplace=True)


def find_locations_that_accept_material(location_df, material):
    location_matches = []
    for x, y in location_df.iterrows():
        if(y[material] == 't'):
            location_matches.append(y)
        # print(y[material])
    return location_matches


blub = find_locations_that_accept_material(temp_locations, "Batteries")
print(blub)
