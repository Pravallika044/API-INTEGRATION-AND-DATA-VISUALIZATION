import requests
import matplotlib.pyplot as plt

API_KEY = "your_api_key"
CITY = "London"
url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

# Extract data
temp = data['main']['temp']
humidity = data['main']['humidity']
description = data['weather'][0]['description']

# Visualization
labels = ['Temperature (°C)', 'Humidity (%)']
values = [temp, humidity]

plt.bar(labels, values, color=['blue', 'green'])
plt.title(f'Current Weather in {CITY}')
plt.ylabel('Value')
plt.savefig('weather_dashboard.png')
plt.show()
