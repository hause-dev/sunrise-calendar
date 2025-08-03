import utils.solarUtils as solarUtils

if __name__ == '__main__':
    womens_forum_location = {"latitude" : 45.534249, "longitude" : -122.261081}
    response = solarUtils.fetch_json(womens_forum_location["latitude"],
                     womens_forum_location["longitude"],
                     day="01", month="08", year="2025")
    print(solarUtils.get_sunset(response))
