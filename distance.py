#!/usr/bin/python
'''
Filename: 		distance.py
Contributors:	Todd Boone II, Jackson Brietzke, Jonah Woods, Andrew Zolintakis, Frank Longo, Peter Awori
Description:	Enables the CanCan application to retrieve distance 
				information from Google's Distance Matrix API.

Modules 
Imported:		requests
				difflib
				creating_materials (created by us)

Imported By:	gui.py

References:		https://developers.google.com/maps/documentation/distance-matrix/intro
				http://docs.python-requests.org/en/latest/api/
'''
import requests
import difflib
import creating_materials

GOOGLE_DISTANCE_API_URL = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
API_KEY = 'AIzaSyC6ELq9yvgnhnmnnMhfmfPHRBQ6KVjSfMY'

# Initialize recycling locations
recyclingLocations = creating_materials.create_locations_df()

# Map GUI category names to creating_materials material name
def categorySwitcher(category):
	switcher={
		'Aluminum':'Scrap Metals',
		'Battery':'Batteries',
		'Computers':'Computers',
		'E-Cycling':'Electronics',
		'Glass':'Construction',
		'Mobile':'Mobile Phones',
		'Paper':'Household',
		'Plastic':'Plastic',
		'Tires':'Tires',
		'Waste':'Construction'
	}
	return switcher.get(category,"")

# Retrieve full Google Distance Matrix API Response
def getDistanceInfo(origin, destination):
	'''
	Add necessary params to params dict
		Paramters:
			{origin} - starting point for calculating travel distance and time
			{destination} - finishing point for calculating travel distance and time
			{units} - specify unit system, options: 'imperial' or 'metric'(default) 
			{key} - API_KEY
	'''
	params = {
		'origins': origin,
		'destinations': destination,
		'units': 'imperial',
		'key': API_KEY
	}

	# Make the API request and store response, else print error and exit
	try:
		response = requests.get(GOOGLE_DISTANCE_API_URL, params=params)
		distanceResponse = response.json()
	except requests.exceptions.RequestException as e:
		print(e)
		sys.exit(1)

	return distanceResponse

# Retrieve the list of destination addresses
def getAddress(distanceResponse):
	address = []
	
	# Retrieve miles from response
	try:
		for currentAddress in distanceResponse['destination_addresses']:
			address.append(currentAddress)
	except:
		if distanceResponse['status'] == 'ZERO_RESULTS':
			error = 'The distance could not be calculated. Try a different address.'
			return error

	return address

# Retrieve the list of miles in between origin and destination
def getMiles(distanceResponse):
	distance = []
	
	# Retrieve miles from response
	try:
		for element in distanceResponse['rows'][0]['elements']:
			for key, val in element['distance'].items():
				if key == 'text':
					distance.append(val)
	except:
		if distanceResponse['rows'][0]['elements'][0]['status'] == 'ZERO_RESULTS':
			error = 'The miles could not be calculated. Try a different address.'
			return error

	return distance

# Retrieve the list of duration times in between origin and destination
def getDuration(distanceResponse):
	duration = []

	# Retrieve duration from response
	try:
		for element in distanceResponse['rows'][0]['elements']:
			for key, val in element['duration'].items():
				if key == 'text':
					duration.append(val)
	except:
		if distanceResponse['rows'][0]['elements'][0]['status'] == 'ZERO_RESULTS':
			error = 'The duration could not be calculated. Try a different address.'
			return error

	return duration

# Retrieve the list of duration values in between origin and destination
def getDurationValue(distanceResponse):
	durationValue = []

	# Retrieve duration from response
	try:
		for element in distanceResponse['rows'][0]['elements']:
			for key, val in element['duration'].items():
				if key == 'value':
					durationValue.append(val)
	except:
		if distanceResponse['rows'][0]['elements'][0]['status'] == 'ZERO_RESULTS':
			error = 'The duration value could not be calculated. Try a different address.'
			return error

	return durationValue

# Get a dictionary of closest location
def getClosestLocation(origin, destination):
	closestIndex = ''

	# Retrieve Distance Response
	distanceResponse = getDistanceInfo(origin, destination)

	# Get lists of corresponding addresses, miles, duration, and duration values
	address = getAddress(distanceResponse)
	miles = getMiles(distanceResponse)
	duration = getDuration(distanceResponse)
	durationValue = getDurationValue(distanceResponse)

	# Find the index of closest address
	closestIndex = durationValue.index(min(durationValue))
	
	# Create a dictionary that holds informatiion about the closest location
	closestLocation = {
		'address': address[closestIndex],
		'miles': miles[closestIndex],
		'duration': duration[closestIndex]
	}

	return closestLocation

# Get a full dictionary that represents closest info to display on application
def getClosestAppropriateLocation(origin='Heinz College', material = ''):
	'''
	Retrieve closest location that can accept specified material
	'''
	# Map GUI category names to creating_materials material name
	material = categorySwitcher(material)

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
	closestAppropriateLocationDict = getClosestLocation(origin, formattedListOfAddresses)
	
	# Append the name of the place at appropriate address
	for place in appropriateLocations:
		if place['location_address'] == difflib.get_close_matches(closestAppropriateLocationDict['address'], listOfAddresses)[0]:
			closestAppropriateLocationDict['name'] = place['location_name']

	return closestAppropriateLocationDict

if __name__ == "__main__":
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
