import pywapi
import string

weather_com_result = pywapi.get_weather_from_weather_com('92120')
noaa_result = pywapi.get_weather_from_noaa('KSAN')

print "Weather.com says: It is " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in San Diego.\n\n"

print "NOAA says: It is " + string.lower(noaa_result['weather']) + " and " + noaa_result['temp_f'] + "F now at Lindberg Field.\n" 
