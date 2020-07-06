#!/usr/bin/env python3

import argparse
import time
import requests
import hashlib
import webbrowser
import os
## Define the API here
XAVIER = 'http://gateway.marvel.com/v1/public/characters'

## Calculate a hash to pass through to our MARVEL API call
## Marvel API wants md5 calc md5(ts+privateKey+publicKey)
def hashbuilder(timeywimey, pvkee, pubkee):
    return hashlib.md5((timeywimey+pvkee+pubkee).encode('utf-8')).hexdigest()

## Perform a call to MARVEL Character API
## http://gateway.marvel.com/v1/public/characters
## ?name=Spider-Man&ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150
def marvelcharcall(stampystamp, hashyhash, pkeyz, lookmeup):

    r = requests.get(XAVIER+"?nameStartsWith="+lookmeup+"&ts="+stampystamp+"&apikey="+pkeyz+"&hash="+hashyhash)

    #print(XAVIER+"?name="+lookmeup+"&ts="+stampystamp+"&apikey="+pkeyz+"&hash="+hashyhash)
    return r.json()


def main():
    url = 'http://docs.python.org/'

    # Open URL in a new tab, if a browser window is already open.
    webbrowser.open_new_tab(url)

    # Open URL in new window, raising the window if possible.
    webbrowser.open_new(url)
    ## Dict to store data
    data_set = []
     
    ## harvest private key
    #dev = /home/student/marvel.priv
    with open(args.dev) as mccoy:
        beast = mccoy.read().rstrip('\n')
    
    ## harvest public key
    #pub = /home/student/marvel.pub
    with open(args.pub) as munroe:
        storm = munroe.read().rstrip('\n')
    
    ## create an integer from a float timestamp (for our RAND)
    nightcrawler = str(time.time()).rstrip('.')
    
    ## build hash with hashbuilder(timestamp, privatekey, publickey)
    cerebro = hashbuilder(nightcrawler, beast, storm)

    ## call the API with marvelcharcall(timestamp, hash, publickey, character)
    print(args.hero)
    
    if args.hero == None:
        char_input = input("Enter a Marvel character name: ")
        
        while (char_input == ""):
            inpus = input("blank input: ")
            char_input = inpus
        
        uncannyxmen = marvelcharcall(nightcrawler, cerebro, storm, char_input)
    else: 
        uncannyxmen = marvelcharcall(nightcrawler, cerebro, storm, args.hero)
    
    ## display results
    
    results = uncannyxmen['data']['results']
    for result in results:
        print(f"ID: {result['id']} \nNAME: {result['name']} \nDESCRIPTION: {result['description']}", end="\n\n")

    ## id for image
    id_input = str(input("Enter character ID for image: "))
    
    for result in results:
        if id_input == str(result['id']):
            print('Opening image in new tab...')
            path = result['thumbnail']['path']
            ext = result['thumbnail']['extension']
            size = "/portrait_incredible"
            uri = path + size + "." + ext
            print(uri)
            url = str(uri)
            print(url)
            webbrowser.open(url)
        webbrowser.open(url)
    webbrowser.open(url)

## Define arguments to collect
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dev', help='Provide the /path/to/file.priv \
      containing Marvel private developer key')
    parser.add_argument('--pub', help='Provide the /path/to/file.pub \
      containing Marvel public developer key')
    
    ## The line below is NEW! This allows us to pass the lookup character
    parser.add_argument('--hero', \
      help='Returns character that begin with input')
    
    args = parser.parse_args()
    main()

