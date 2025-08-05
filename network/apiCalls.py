import requests
import json



def freeAPIRequest(apiURL):
    # Try to make the HTTP GET request
    try:
        response = requests.get(url=apiURL)         
    except Exception as e:
        print("Error:", e)
    print(f'{response}') 
    return response

def getWeather():
    try:
        response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=41.8501&longitude=-71.4662&current=temperature_2m&timezone=America%2FNew_York&wind_speed_unit=mph&temperature_unit=fahrenheit&precipitation_unit=inch")             
        data=json.loads(response.text)
    except Exception as e:
        print("Error:", e)
    return data