import requests

api_key = "187443dac35b96bc652640afcea3cca2"
base_url = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{base_url}?appid={api_key}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()

    weather = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"] - 273.15, 2)
    feels_like = round(data["main"]["feels_like"] - 273.15, 2)
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]


    print(f"""
    
    Weather: {weather}

    Temperature: {temperature} degrees celsius
    
    Pressure: {pressure} hPA

    Humidity: {humidity}%
        """)


else:
    print("An error occured.")