import random
from datetime import datetime

def default_game():
    """The default game"""
    secret_number = 1000
    secret_number_str = str(secret_number)

    # Secret number printed here just for testing purposes
    print secret_number

    print "\nThe secret number is", len(secret_number_str), "digits long."

    guess = int(raw_input("\nWhat do you think it is?: "))
    tries = 1

    starttime = datetime.now()

    while guess != secret_number:
        cows = 0
        bulls = 0
        guess_str = str(guess)
        for g_num, guess in enumerate(guess_str):
            for s_num, secret in enumerate(secret_number_str):
                if (guess == secret):
                    if g_num == s_num:
                        cows += 1
                    else:
                        bulls += 1
        print cows, "Cows", bulls, "Bulls"
        guess = int(raw_input("\nTry again: "))
        tries += 1

        endtime = datetime.now()
        timediff = endtime - starttime
        
        print "\nYou guessed it! \nThe number was", secret_number, "- it took you", tries, "tries and", timediff.seconds, "seconds to get it.\n"

default_game()

raw_input("\n\nPress the enter key to exit.")
