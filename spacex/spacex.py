#!/usr/bin/env python3

import json

def main():
    
    def getJsonFile(): 
        with open("spacex.data", "r") as jsonfile:
            data = json.load(jsonfile)
    
            #  print(data)

            print(data[0]["missions"][0]["name"])
            

    def getDataApiCall():
        data = "coming soon"
        print(data)
        

    getJsonFile()
    getDataApiCall()

if __name__ == "__main__":
    main()
