#!user/bin/python3
"""Hockey"""

SEARCH_API = 'https://statsapi.web.nhl.com/api/v1/teams'

import requests
import json
import pprint as p

def main():

    r = requests.get(SEARCH_API)
    data = r.json()

    ## print pretty
    #p.pprint(data)

    ## print pretty what i want to see
    for team in data['teams']:
        p.pprint(f"{team['firstYearOfPlay']} - {team['teamName']}")
    
    ## print what i want
    #for team in data['teams']:
        print(f"Team: {team.get('teamName')} \nLocation: {team.get('locationName')} \nYear Began: {team.get('firstYearOfPlay')} \nOfficial Website: {team.get('officialSiteUrl')} \nHome Venue: {team['venue'].get('name')} \n ")
    
    #print(f"Total teams in data set: {len(data['teams'])}")

    ## sort json object by year
    sorted_obj = dict(data)
    p.pprint(sorted_obj)
    sorted_obj= sorted(data['teams'], key=lambda x : x['firstYearOfPlay'], reverse=True)

    #p.pprint(sorted_obj)
    for team in sorted_obj:
        p.pprint(f"{team['firstYearOfPlay']} - {team['teamName']}")
        print(f"Team: {team.get('teamName')} \nLocation: {team.get('locationName')} \nYear Began: {team.get('firstYearOfPlay')} \nOfficial Website: {team.get('officialSiteUrl')} \nHome Venue: {team['venue'].get('name')} \n ")
        

if __name__ == '__main__':
    main()
