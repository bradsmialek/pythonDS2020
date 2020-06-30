#!/usr/bin/python3
"""
Author: RZFeeser & Brad Smialek
This program harvests SpaceX data avail from https://api.spacexdata.com/v3/cores using the Python Standard Library methods
"""

# using std library method for getting at API data
import requests
import json
from datetime import datetime as dt

from colorama import Fore, Back, Style

# GOBAL / CONSTANT of the API we want to lookup
SPACEXURI = "https://api.spacexdata.com/v3/cores"

def main():
    # create a urllib.request response object by sending an HTTP GET to SPACEXURI
    coreData = requests.get(SPACEXURI)

    # convert STRING data into Python Lists and Dictionaries
    listOfCores = coreData.json()
    print(type(listOfCores))

    for core in listOfCores:
        #print(core, end="\n\n")
        print(Back.BLUE + "CORE: " + Fore.YELLOW + core["core_serial"], end="\n")

        launch = core.get("original_launch")
        if launch is None:
            print(Fore.WHITE + "LAUNCH: " + Back.RED + "No Info - CLASSIFIED", end="\n")
        else:
             # 2019-12-05T17:29:23.000Z
            newTimeP = launch.replace("T", " ")
            n = newTimeP.replace(".000Z", " ")
            #t = n.strftime("%b %d %Y")
            print(Back.BLUE + Fore.WHITE + "LAUNCH: " + Fore.YELLOW + n , end="\n\n")
        
        missions = core.get("missions")
        for mission in missions:
            #print(mission)
            if len(mission) > 1:
                print(Fore.GREEN + Style.BRIGHT + "Mission: " + mission["name"] + " / " + "Flight# " + str(mission["flight"]) , end="\n")
            else:
                print(Fore.WHITE + "Mission: " + Back.RED + "No Info - CLASSIFIED", end="\n")
        print(Style.RESET_ALL)
        print()
        print()

if __name__ == "__main__":
    main()
