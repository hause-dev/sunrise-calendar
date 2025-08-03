import requests
import calendarUtils

def fetch_json(latitude, longitude, day, month, year):
    api_url = f"https://api.sunrisesunset.io/json?lat={latitude}&lng={longitude}&date={year}-{month}-{day}"
    api_response = requests.get(api_url)
    return api_response.json()

def get_sunrise_data(response):
    results = response["results"]
    sunrise_data = {
            "type" : "sunrise",
            "first_light" : results["first_light"],
            "dawn" : results["dawn"],
            "sunrise" : results["sunrise"]
            }
    return sunrise_data
                                
def get_sunset_data(response):
    results = response["results"]
    sunset_data = {
            "type" : "sunset",
            "sunset" : results["sunset"],
            "dusk" : results["dusk"],
            "last_light" : results["last_light"]
            }
    return sunset_data

def create_event(latitude, longitude, day, month, year, event_type, utc_offset):
    response = fetch_json(latitude, longitude, day, month, year)
    if (event_type == "sunrise"):
        event_data = get_sunrise_data(response)
    elif (event_type == "sunset"):
        event_data = get_sunset_data(response)
    else:
        print(f"Invalid event type '{event_type}', must be sunrise or sunset")
        return -1

    event_request = calendarUtils.create_event_request(day, month, year,
                                         f"{latitude}, {longitude}", 
                                         event_data, utc_offset)

    return event_request
