import argparse, requests, math

API_ENDPOINT = "https://maps.googleapis.com/maps/api/geocode/json?address="

# Earth radius in metres
R = 6371000

def getCoords(city_name):
	r = requests.get(API_ENDPOINT + city_name)
	return r.json()['results'][0]['geometry']['location']

def distance(c1, c2):
	# Convert latitutes to radians
	l1 = math.radians(c1['lat'])
	l2 = math.radians(c2['lat'])
	# Convert to radians the difference of latitutes
	dlt = math.radians(c2['lat'] - c1['lat'])
	dln = math.radians(c2['lng'] - c1['lng'])

	a = math.sin(dlt * 0.5) * math.sin(dlt * 0.5) + math.cos(l1) * math.cos(l2) * math.sin(dln * 0.5) * math.sin(dln * 0.5)
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
	d = R * c
	return toUnit(d)

def toUnit(metres):
	return {
		'm': metres,
		'km': toKm(metres),
		'mi': toMile(metres)
	}[args.u]

def toKm(metres):
	return metres/1000

def toMile(metres):
	# 1m is equal to 6.21371e-4 miles
	return metres * 6.21371e-4

def main():
	city_name_1 = input("Name of the first city: ")
	c1 = getCoords(city_name_1)
	city_name_2 = input("Name of the second city: ")
	c2 = getCoords(city_name_2)
	print(str(round((distance(c1, c2)))) + args.u)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-u', choices=['m', 'km', 'mi'], default="m", help="Select the unit of distance of the output")
	args = parser.parse_args()
	main()