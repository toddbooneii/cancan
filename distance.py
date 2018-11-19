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

def getMiles(origin, destination):
	# Retrieve Distance Response
	distanceResponse = getDistanceInfo(origin, destination)
	# Retrieve miles from response
	miles = distanceResponse['rows'][0]['elements'][0]['distance']['text']

	return miles

def getDuration(origin, destination):
	# Retrieve Distance Response
	distanceResponse = getDistanceInfo(origin, destination)
	# Retrieve duration from response
	duration = distanceResponse['rows'][0]['elements'][0]['duration']['text']

	return duration

if __name__ == "__main__":
	# Prompt user to enter origin and destination
	print("Enables the CanCan application to retrieve distance information from Google's Distance Matrix API.\n")

	origin = input('Enter an origin address: ')
	destination = input('Enter a destination address: ')

	print('\n')

	print('Miles between: ' + getMiles(origin, destination))
	print('Duration between: ' + getDuration(origin, destination) + '\n')
