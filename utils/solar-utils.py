import requests

def fetch_json(latitude, longitude, day, month, year):
    api_url = f"https://api.sunrisesunset.io/json?lat={latitude}&lng={longitude}&date={year}-{month}-{day}"
    api_response = requests.get(api_url)
    return api_response.json()

def get_sunrise(response):
    results = response["results"]
    times = {
            "first_light" : results["first_light"],
            "dawn" : results["dawn"],
            "sunrise" : results["sunrise"]
            }
    return times
                                
def get_sunset(response):
    results = response["results"]
    times = {
            "sunset" : results["sunset"],
            "dusk" : results["dusk"],
            "last_light" : results["last_light"]
            }
    return times
