import requests
from datetime import date
import calendar

def format_time(year, month, day, time_str, utc):
    am_pm = time_str.split(' ')[1]
    times = time_str.split(' ')[0].split(':')

    if utc < 0:
        offset_str = f"{utc:03}:00"
    else:
        offset_str = f"+{utc:02}:00"

    if am_pm == "AM":
        h = int(times[0])
    else:
        h = int(times[0]) + 12
    m = int(times[1])
    s = int(times[2])

    time_formatted = f"{year}-{month:02}-{day:02}T{h:02}:{m:02}:{s:02}{offset_str}"

    return time_formatted


def create_event_request(day, month, year,
              location, event_data, utc_offset):
    try:
        event_type = event_data["type"]
        if event_type == "sunrise":
            time_data = {
                    "start" : event_data["dawn"],
                    "end" : event_data["sunrise"]
                    }
            description = (f"First light: {event_data['first_light']}\n"
            f"Dawn: {event_data['dawn']}\n"
            f"Sunrise: {event_data['sunrise']}")
        elif event_type == "sunset":
            time_data = {
                    "start" : event_data["sunset"],
                    "end" : event_data["dusk"]
                    }
            description = f"""
            Sunset: {event_data["sunset"]}\n
            Dusk: {event_data["dusk"]}\n
            Last light: {event_data["last_light"]}
            """
        else:
            print("Type is invalid: must be sunrise or sunset")
            return -1
    except KeyError:
        print("Missing key", err)
        return -1

    day_of_week = calendar.day_name[date(year, month, day).weekday()]
    summary = f"{day_of_week} {event_type}"

    start_time = {
            'dateTime' : format_time(year, month, day, time_data["start"], utc_offset)
            }
    end_time = {
            'dateTime' : format_time(year, month, day, time_data["end"], utc_offset)
            }

    event = {
            'summary' : summary,
            'location' : location,
            'description' : description,
            'start' : start_time,
            'end' : end_time
            }

    return event
