#!/usr/bin/python3
""" Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://jservice.io/

import requests

URI = "https://jservice.io/api/random?count="

COUNTER = 0


def main():

    ## get initials and rounds
    initials = input("Enter your initials: ")
    cap_initials = initials.upper()
    rounds = input("How many rounds will you play: ")
    rounds_int = int(rounds)
    counter = 0
    print(type(rounds_int))

    while (rounds_int > 10):
        rounds = input("Enter 10 or less: ")
        rounds_int = int(rounds)
        print(type(rounds))

    print("Lets play " + rounds + " rounds!")

    ## Send HTTPS GET to the API
    resp = requests.get(URI + rounds)
    j_resp = resp.json()
    #print(j_resp, end="\n\n") 
    
    for item in j_resp:
        print(item["answer"])
        user_resp = input(item["question"] + "? ")

        if user_resp == item["answer"]:
            print(counter)
            counter = counter + item["value"]
            print("Correct")
            print("Score:", end=" ")
            print(counter)
        else:
            counter = counter - item["value"]
            print("Incorrect")
            print("Score:", end=" ")
            print(counter)
    
    print("End of game")
    print("Your Final Score", end=" ")
    print(counter)

    ## add score to top 10 if score is greater than one of top 10 scores
    #read high_score.txt
    
    f = open("high_scores.txt", "r")
    print(f.read())


        


if __name__ == "__main__":
    main()
