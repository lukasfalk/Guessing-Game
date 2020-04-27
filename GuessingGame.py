import random

print("Welcome to the guessing game!")
input("Press 'Enter' to start")

def guessing_seq():
    game_over = True
    attempts = 0
    while game_over:
        print("Choose how big the range should be: ")
        size = int(input())
        num_in_play = random.randint(1, size)
        while game_over:
            print("Guess a number: ")
            guess = int(input())
            if guess > num_in_play:
                attempts += 1
                print("Guess was too high. Try again!")
            elif guess < num_in_play:
                attempts += 1
                print("Guess was too low. Try again!")
            else:
                attempts += 1
                print("Correct! You used {0} attempts".format(attempts))
                game_over = False

play = True
guessing_seq()
while play:
    print("Play again? (y/1)")
    again = str(input())
    if again == "y" or again == "1":
        guessing_seq()
    elif again == "easter egg":
        print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    else:
        play = False
