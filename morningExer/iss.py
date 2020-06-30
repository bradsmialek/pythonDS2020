#!/usr/bin/env python3

import json
import requests


def main():

    # Make a get request to get the latest position of the international space station
    response = requests.get("http://api.open-notify.org/iss-now.json")
    print(response.status_code)
    issData_dict = response.json()

    lat = issData_dict["iss_position"]["latitude"]
    lon = issData_dict["iss_position"]["longitude"]

    with open('iss.txt', 'w') as json_file:
        json.dump(lat, json_file)

    with open('iss.txt', 'a') as json_file:
        json.dump(lon, json_file)
    

    #open and read the file after the appending:
    issData_dict = open("iss.txt", "r")
    print(issData_dict.read())



if __name__ == "__main__":
    main()
