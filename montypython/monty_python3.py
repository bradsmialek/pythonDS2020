#!/usr/bin/python3
round = 0
answer = " "
answer.lower()

while round < 3 and answer != "brian":
    round += 1     # increase the round counter by 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    if answer.lower() == "brian": # logic to check if user gave correct answer
        print("Correct!")
    elif answer == "shrubbery":
        print("You gave the super seret answer!")
    elif round == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
    else:                 # if answer was wrong
        print("Sorry. Try again!")
if __name__ == "__main__":
    main()
