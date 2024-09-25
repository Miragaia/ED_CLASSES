import time
import requests

API_KEY = "740b3c7f06c686f5332bd67edab24109"
part = "minutely,hourly,alerts"

def get_weather(lat, lon):
    url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data

def kelvin_to_celsius(temp_kelvin):
    return temp_kelvin - 273.15

def main():
    data = get_weather("40.6412", "-8.65362")

    current = data['current']
    #get the data for current weather
    timestamp = time.ctime(current['dt'])
    temp = current['temp']
    temp_celsius = kelvin_to_celsius(current['temp'])
    description = current['weather'][0]['description']
    wind_speed = current['wind_speed']
    humidity = current['humidity']

    print(f"Time: {timestamp}")
    print(f"Temperature: {temp:.2f} °K")
    print(f"Temperature: {temp_celsius:.2f} °C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Weather Description: {description}")
    print("-" * 30)

    data_daily = data['daily'][1:6]
    for day in data_daily:
        timestamp = time.ctime(day['dt'])
        temp = day['temp']['day']
        temp_celsius = kelvin_to_celsius(day['temp']['day'])
        description = day['weather'][0]['description']
        wind_speed = day['wind_speed']
        humidity = day['humidity']

        print(f"Time: {timestamp}")
        print(f"Temperature: {temp:.2f} °K")
        print(f"Temperature: {temp_celsius:.2f} °C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Weather Description: {description}")
        print("-" * 30)



if __name__ == "__main__":
    main()
