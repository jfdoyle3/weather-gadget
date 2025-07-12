import urequests as requests
import ujson

def freeAPIRequest(apiURL):
    # Try to make the HTTP GET request
    try:
        response = requests.get(url=apiURL)
        json_data = response.json()  # Directly parse the JSON response
        response.close()        
    except Exception as e:
        print("Error:", e)

    return json_data
