#****************************************************************
#Name: Wing Lok LO
#Link: https://replit.com/join/xspzgfrbub-lowinglokjason
#****************************************************************

#import requests and json packages
import requests
import json

#############
#Question #1
#############

#who is in space right now from within the function.
#define a function

def who_is_in_space_right_now():
  response = requests.get("http://api.open-notify.org/astros.json")
  data = response.json()
  people = data["people"]
  number_of_people = data["number"]
  
  #print the numnber of people in space now
  print(f"There are {number_of_people} people in space right now:")
  
  #list out the person's name and the spaceship they are living
  for person in people:
    print(f"- {person['name']} is on {person['craft']}.")

#call the function
who_is_in_space_right_now()

#############
#Question #2
#############

#the current weather in the city I was born - Hong Kong
#define weather

def hk_weather():
  
  #extract data of current Hong Kong weather from OpenWeatherMap API
  api_key = "fe8864f0805d25db6c7d08959d89dd60"
  city_name = "Hong Kong, HK"  
  url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&lang=en&&appid={api_key}&units=metric"
  response = requests.get(url)
  data = json.loads(response.text)
  
  #add weather details of current Hong Kong weather
  weather = data['weather'][0]['description']
  temperature = data['main']['temp']
  temperature_min = data['main']['temp_min']
  temperature_max = data['main']['temp_max']
  feels_like = data['main']['feels_like']
  humidity = data['main']['humidity']
  wind = data['wind']['speed']
  
  #print out the details
  print(f"The current weather in {city_name} is {weather}: \nTemperature: {temperature}°C \nMinimum Temperature: {temperature_min}°C \nMaximum Temperature: {temperature_max}°C \nFeels like: {feels_like}°C \nhumidity: {humidity}% \nWind speed: {wind} m/s")

#call the function
hk_weather()

#############
#Question #3
#############

#define the current space station location

def current_space_station_location():
 
  #extract data of ISS location from Open Notify API
  iss_url = "http://api.open-notify.org/iss-now.json"
  iss_response = requests.get(iss_url)
  iss_data = json.loads(iss_response.text)

  #extract latitude and longitude data
  latitude = iss_data['iss_position']['latitude']
  longitude = iss_data['iss_position']['longitude']

  #extract weather data from OpenWeatherMap API
  api_key = "fe8864f0805d25db6c7d08959d89dd60"
  weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
  weather_response = requests.get(weather_url)
  weather_data = json.loads(weather_response.text)

  #check whether ISS lcoation is currently above water or land
  if weather_data['id'] == 0:
    print("ISS is currently over water.")
  else:
    #extract weather and country name
    weather = weather_data['weather'][0]['description']
    country_name = weather_data['sys']['country']

    #return weather and country name
    return f"The country for the current ISS location is {country_name} where the weather is {weather}."

#print the function
print(current_space_station_location())

#############
#Question #4
#############

#define a list as an argument
def print_list(list):
  for item in list:
    print(item)

#call the function
list = [1, 2, 3]
print_list(list)

#############
#Question #5
#############

#define a function that takes arbitrary keyword arguments **kwargs
def my_function(**kwargs):
  for key, value in kwargs.items():
    print(key, value)

#call the function
my_function(name='Jason', age=22, location='Hong Kong')

#############
#Question #6
#############

#define *args & **kwargs
def test(*args, **kwargs):
  print("args:", args)
  print("kwargs:", kwargs)

#call the function
test(1, 2, 3, a=4, b=5)

#*args: 
##-enables you to pass a function a variable number of positional arguments or other non-keyword arguments. 
##-Any amount of arguments can be collected into a tuple using the * symbol. 
##-The function can then use the *args syntax to retrieve the tuple.

#**kwargs: 
##-enables you to call a function with a variable number of keyword arguments. 
##-Any number of keyword inputs can be gathered together into a dictionary using the ** symbol. 
##-The **kwargs syntax can then be used by the function to retrieve the dictionary.

#############
#Question #7
#############

#define function with keyword arguments (the opposite of positional arguments)
def calculate_total(price=100, tax_rate=0.2, discount=10):
  total = price * (1 + tax_rate) - discount
  return total

#call the function
print(calculate_total(price=100, tax_rate=0.2, discount=10))

#############
#Question #8
#############

#define a function that looks up information about India
def india():
  #extract data of India from REST Countries API
  response = requests.get("https://restcountries.com/v3.1/name/india")

  #extract details of India
  data = response.json()
  country_name = data[1]["name"]["common"]
  capital = data[1]["capital"][0]
  population = data[1]["population"]
  currency = data[1]["currencies"]["INR"]['name']
    
  #print the details of India
  print(f"{country_name} has a population of {population} and its capital is {capital} and its currency is {currency}.")

#call the function
india()
