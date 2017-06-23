# Distance between two locations
Little python program that calculates the distance, in the specified unit of distance, of two locations.

## Overview
This python program calculates the distance between two locations. You can specify the unit of distance as an argument or it would return the distance, by default, in metres. It uses the geocoding api from Google to obtain the coordinates from the address or name of the location and then uses the [Haversine formula](https://en.wikipedia.org/wiki/Haversine_formula) to calculate the distance from the coordinates.
- #### Why use it?
  I am sure there will be better libraries or packages that will achieve the same goal better (or not), but I wanted to write this program because I was inspired to do so 😊, but the program works well so that's a very good reason to use it, why not?

## Examples
```
> python main.py
Name of the first city: Madrid
Name of the second city: Paris
1052897m
```

```
> python main.py -u km
Name of the first city: Paris
Name of the second city: Madrid
1053km
```
## Usage
```
python main.py [-h] [-u {m,km,mi}]

optional arguments:
  -h, --help    show this help message and exit
  -u {m,km,mi}  Select the unit of distance of the output
```
Just run the program and you will be prompted the name of the locations you want to get the distance of. If you want to get the result in diferent units you can choose between metres, kilometres and miles by using the -u [unit abbr] argument.

## Requirements
- Requests: HTTP for Humans [Website](http://python-requests.org/) [Github](https://github.com/requests/requests)

## Credits
- [Google Geocoding API](https://developers.google.com/maps/documentation/geocoding/start) for providing the data needed for this program to run.

## References
- [Haversine formula](https://en.wikipedia.org/wiki/Haversine_formula), the program uses this formula to calculate the distance (in metres, then converted if necessary) from location coordinates.

## Contributing
Just open a pull request.

## License
Licensed under [MIT](https://github.com/mrluissan/Distance-between-2-locations/blob/master/LICENSE).
