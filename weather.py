import requests
import os
apikey=os.environ['current_weather_data']
option=int(input("if you want the information of the weather by the country name then enter 1 and if you want the information by zip code then enter any number: "))
if option == 1:
    location=input("enter the name of the city : ")
    complete_link=f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={apikey}"
else:
    zip_code=(input("enter the zip code of any city: "))
    country_code=(input("enter the country code: "))
    complete_link=f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={apikey}&units=metric"
api_link=requests.get(complete_link)
api_data=api_link.json()
if option ==1:
    if api_data['cod']=='404':
        print("Invalid city name: {}".format(location))
    else:
        temperature=api_data['main']['temp']-273.15
        humidity=api_data['main']['humidity']
        weather_description=api_data['weather'][0]['description']
        print("Today the temperature is: ",temperature)
        print("Description: ",weather_description)
        print("Today the humidity is: ",humidity)

else:
    if api_data['cod']=='404':
        print("Invalid zip code or country code")
    else:
        temperature=api_data['main']['temp']-273.15
        humidity=api_data['main']['humidity']
        weather_description=api_data['weather'][0]['description']
        print("Today the temperature is: ",temperature)
        print("Description: ",weather_description)
        print("Today the humidity is: ",humidity)