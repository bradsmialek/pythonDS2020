#!/usr/bin/env python3

import requests
import socket


myIP = "205.134.219.38"

def main():
    userAddr = input("Enter IP Address: ")
    print("Thanks... Searching " + userAddr)
    

    URI = "http://ip-api.com/json/" + myIP
    print(URI)
    ipAddr = requests.get(URI)

    got_ip = ipAddr.json()

    print(got_ip)

if __name__ == "__main__":
    main()


    
# {'status': 'success', 'country': 'United States', 'countryCode': 'US', 'region': 'WA', 'regionName': 'Washington', 'city': 'Eatonville', 'zip': '98328', 'lat': 46.87, 'lon': -122.2723, 'timezone': 'America/Los_Angeles', 'isp': 'Rainier Connect', 'org': 'Rainier Connect', 'as': 'AS20394 Rainier Connect', 'query': '205.134.219.38'}
