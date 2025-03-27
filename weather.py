import requests

API_KEY = "your_api_key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            print("City not found! Please try again.")
            return
        weather = data["weather"][0]["description"].title()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        print(f"\n Weather in {city}:")
        print(f" Condition: {weather}")
        print(f" Temperature: {temp}°C")
        print(f" Humidity: {humidity}%")
        print(f" Wind Speed: {wind_speed} m/s")
    except Exception as e:
        print("An error occurred. Please try again.")

#user input
city = input("Enter the city Name: ")
get_weather(city)
