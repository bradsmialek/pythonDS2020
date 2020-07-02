#!/usr/bin/python3
import requests
import webbrowser
import json

## Define NEOW URL 
NEOURL = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol="

def main():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")        

    ## update with earth_date
    earth_date = input("Enter number: ")
    
    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + earth_date + "&" + nasacreds)
    
    # strip off json attachment from our response
    neodata = neowrequest.json()
    
   # print(neodata["photos"][0]["img_src"])

    for image in neodata["photos"]:
        print(image["img_src"])


if __name__ == "__main__":
    main()

