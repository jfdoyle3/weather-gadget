
    

def initApp():
     print("wifi init")
     lcdClear()
     ip=wifiConnect()



          
    # No WiFi connection - Exit
    if not isinstance(ip, str):
        lcdNotConnected()
        errorCode(3,.5)   # 3 blinks no connection
        powerOff()
        
    # Connected to net
    lcdConnected()
    print(ip)
    ledOn()
    '''    
    print(getTemp())
    # res = requests.get(url='https://api.weather.gov/points/41.87092932,-71.42788283')
    # print(res.text)
    apiURL='https://api.open-meteo.com/v1/forecast?latitude=41.8501&longitude=-71.4662&current=temperature_2m&timezone=America%2FNew_York&wind_speed_unit=mph&temperature_unit=fahrenheit&precipitation_unit=inch '
    # Make the HTTP GET request
    try:
        # req=freeAPIRequest(apiURL)
        with open('/files/f.json') as f:
            data = json.load(f)
        
        # Access parsed data
        print(data)
        print('>>------------------------->')
        print('<-------------------------<<')
        
        temp="{:.0f}".format(data['current']['temperature_2m'])
        unit=data['current_units']['temperature_2m']
        
        print(f"{temp}{unit}")
        '''
        #lcdText(f"{temp}{unit}",0,0)
        lcdText("Hi",0,0)
        
        buttonPress()
        
    except Exception as e:
        print("Error:", e)
    
    # powerOff()
    
