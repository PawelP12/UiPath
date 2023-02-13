import requests
import json

def evaluate_temperature(city_id,API_key):
	
	
	
	base_url = "http://api.openweathermap.org/data/2.5/weather?"
	

	Final_url = base_url + "appid=" + API_key + "&q=" + city_id + "&units=metric"
	
	weather_data = requests.get(Final_url).json()

	if(weather_data["cod"]!=200):
		return ("Temperature Retrevial unsucessful. Code:"+weather_data["cod"]+". "+weather_data["message"])

	else:
	
		actual_temp=weather_data["main"]["temp"]

		local_average_temp=(weather_data["main"]["temp_min"]+weather_data["main"]["temp_max"])/2

	

		if(actual_temp>local_average_temp):
			return "Above"
		else:
			return "Below"