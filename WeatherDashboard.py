import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# OpenWeatherMap API details
API_KEY = "a482f980da9e92e4fe3aaa9298e52732"
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

# Define the city and parameters
CITY = "Mumbai"
PARAMS = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"
}

# Fetch data from the API
response = requests.get(BASE_URL, params=PARAMS)
data = response.json()

if response.status_code == 200:
    # Parse the forecast data
    dates = []
    temperatures = []
    humidity = []
    
    for entry in data['list']:
        dates.append(datetime.datetime.fromtimestamp(entry['dt']))
        temperatures.append(entry['main']['temp'])
        humidity.append(entry['main']['humidity'])
    
    # Create visualizations
    sns.set(style="whitegrid")

    # Plot temperature trends
    plt.figure(figsize=(10, 6))
    plt.plot(dates, temperatures, label='Temperature (°C)', color='orange', marker='o')
    plt.title(f"Temperature Trend for {CITY}")
    plt.xlabel("Date & Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Plot humidity trends
    plt.figure(figsize=(10, 6))
    plt.plot(dates, humidity, label='Humidity (%)', color='blue', marker='o')
    plt.title(f"Humidity Trend for {CITY}")
    plt.xlabel("Date & Time")
    plt.ylabel("Humidity (%)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

else:
    print(f"Failed to fetch data: {data.get('message', 'Unknown error')}")
