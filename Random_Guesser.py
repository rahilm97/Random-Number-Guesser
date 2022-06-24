import random
from termcolor import colored

print("\033[1m" + "Welcome to Guess the Number!" + "\033[0m")
name = input("What's your name?")
print("Hello " + name + ". How are you?")
num = random.randint(0, 10)
guess = -1
while guess != num:
    guess = input("Guess the number (press q to quit): ")
    if guess == 'q': break

    if int(guess) != num:
        print(colored("Sorry, your guess is wrong", "red"))
    else:
        print(colored("You guessed correctly! Congratulations!", "green"))
        break