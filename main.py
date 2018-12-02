#!/usr/bin/python
'''
main.py

Serves as the central hub for the CanCan application.

References:
	https://github.com/toddbooneii/cancan
'''
import distance
import creating_materials
import difflib

# Initialize recycling locations
recyclingLocations = creating_materials.create_locations_df()

# Retrieve closest location that can accept specified material
def getClosestAppropriateLocation(origin='Heinz College', material = ''):
	# Get origin from GUI
	'''
	if GUI_ORIGIN != None:
		origin = GUI_ORIGIN
	'''

	# Get material from GUI
	'''
	material = GUI_MATERIAL
	'''

	# Retrieve and format list of all approriate locations
	appropriateLocations = creating_materials.find_locations_that_accept_material(recyclingLocations, material)
	listOfAddresses = []
	for locations in appropriateLocations:
		listOfAddresses.append(locations['location_address'])
	formattedListOfAddresses = "|".join(listOfAddresses) # format for Google Distance Matrix API

	'''
	Get the closest appropriate location in the following format:
		closestAppropriateLocationDict = {
			'address': address[closestIndex],
			'miles': miles[closestIndex],
			'duration': duration[closestIndex]
		}
	'''
	closestAppropriateLocationDict = distance.getClosestLocation(origin, formattedListOfAddresses)
	
	# Append the name of the place at appropriate address
	for place in appropriateLocations:
		if place['location_address'] == difflib.get_close_matches(closestAppropriateLocationDict['address'], listOfAddresses)[0]:
			closestAppropriateLocationDict['name'] = place['location_name']

	return closestAppropriateLocationDict

if __name__ == '__main__':
	# Test code goes here:
	
	'''
	Testing getClosestAppropriateLocation() functionality
	'''
	print("Enter an address. We will find the closest facility to you that can accept Batteries.\n")
	
	origin = input('Enter an origin address: ')
	material = "Batteries"

	closestAppropriateLocationDict = getClosestAppropriateLocation(origin, material)

	print("Name: " + str(closestAppropriateLocationDict.get('name')))
	print("Address: " + str(closestAppropriateLocationDict.get('address')))
	print("Miles: " + str(closestAppropriateLocationDict.get('miles')))
	print("Duration: " + str(closestAppropriateLocationDict.get('duration')))

	# End Testing getClosestAppropriateLocation() functionality
