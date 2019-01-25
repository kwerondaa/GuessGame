
def guessGame():

    number = 5
    guess_counter =0
    guess_limit = 3

    guess = int(input("Enter a guess number: " ))

    while guess != number and guess_counter !=(guess_limit-1):
        if guess_counter ==1:
            print(str(guess) + " is not the right number. You have " + str(
                (guess_limit - 1) - guess_counter) + " life left\n")
        else:
            print( str(guess) + " is not the right number. You have " + str((guess_limit-1)- guess_counter) + " lives left\n")
        guess = int(input("Enter a guess number: "))
        guess_counter += 1


    if guess == number:
        print("true")
    else:

        print("Game over")

guessGame()
