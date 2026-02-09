API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data["cod"] != 200:
        print("City not found ❌")
        return

    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    print("\n--- Weather Report ---")
    print("City:", city)
    print("Temperature:", temp, "°C")
    print("Weather:", weather)
    print("Humidity:", humidity, "%")
    print("Wind Speed:", wind, "m/s")

def main():
    print("=== Weather App ===")
    city = input("Enter city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
