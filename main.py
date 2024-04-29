import requests, os, sys
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_URL = os.getenv('WEATHER_API_URL')
LOCATION_API_URL = os.getenv('LOCATION_API_URL')


ip = requests.get('https://api.ipify.org').content.decode('utf8')
location_data = requests.get(f'{LOCATION_API_URL}/{ip}').json()

if not location_data['status'] == 'success':
    print(f'Error: {location_data["message"]}')

    sys.exit(1)

lat = float(location_data['lat'])
long = float(location_data['lon'])

weather_data = requests.get(f'{WEATHER_API_URL}/{lat},{long}').json()

print(f'My public IP address is: {ip}')
print(f'My Location: {location_data}')
print()
print(f'{weather_data}')
