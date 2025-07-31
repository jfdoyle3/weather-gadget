# Get request
#
#  free API:
#
#   https://official-joke-api.appspot.com/random_joke


import requests

def freeTest():
    res=requests.get("https://official-joke-api.appspot.com/random_joke")
    print(f"raw response: {res.text}")
    return res

def apiToken():
    res=requests.get("https://official-joke-api.appspot.com/random_joke")
    print(f"raw response: {res.text}")
    return res


def main():
    
    req=freeTest()
    
    jdata=req.json()
    print("-----------------------------")
    print(f"json pass through: {jdata}")
    print("-----------------------------")
    print(jdata["type"])
    print(jdata["setup"])
    print(jdata["punchline"])
    
    print(jdata.keys())
    print(jdata.values())
    
    keys=jdata.keys()
    print(list(keys))
    





# Main
if __name__ == "__main__":
    main()
