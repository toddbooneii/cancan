#!/usr/bin/python
'''
distance.py

Enables the CanCan application to retrieve distance 
information from Google's Distance Matrix API.

References:
	https://developers.google.com/maps/documentation/distance-matrix/intro
	http://docs.python-requests.org/en/latest/api/
'''
import requests

GOOGLE_DISTANCE_API_URL = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
API_KEY = 'AIzaSyC6ELq9yvgnhnmnnMhfmfPHRBQ6KVjSfMY'

def getDistanceInfo(origin, destination):
	'''
	Add paramters to params dict
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

if __name__ == "__main__":
	miles = ''
	duration = ''

	# Prompt user to enter origin and destination
	print("Enables the CanCan application to retrieve distance information from Google's Distance Matrix API.\n")

	origin = input('Enter an origin address: ')
	destination = input('Enter a destination address: ')

	print('\n')

	miles = getMiles(origin, destination)
	duration = getDuration(origin, destination)

	if 'Try a different address.' in miles or 'Try a different address.' in duration:
		print('This route could not be calculated. Please try a different address.\n')
	else:
		print('Miles between: ' + miles)
		print('Duration between: ' + duration + '\n')
