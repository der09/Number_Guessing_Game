# Number Guessing Game 
# Diane Hsieh 
# AM 

# importing a python module
import random 

# returns random integer 1 to 10, including endpoints
random_number = random.randint(1, 10)

# array for guesses player has made
previous_guesses = [] 

# user can only guess 5 times 
guess = 5 

# function to add a guess if it qualifies 
def add_guess(user_guess, previous_guesses): 

    # gives invalid input if guess is out of range or dupes 
    while user_guess > 10 or user_guess < 1 or user_guess in previous_guesses:
        # if out of range 
        if user_guess > 10 or user_guess < 1:
            print("Invalid input! Number must be between 1 and 10.")
        # if duplicate
        else:
            print("Invalid input! You already guessed this number.")

        print("Previous guesses:", previous_guesses)
        user_guess = int(input("Enter a number between 1 - 10: "))

    # returns valid guess  
    return user_guess

# when there are still guesses avaliable 
while guess > 0: 
    user_guess = int(input("Enter a number between 1 - 10: "))
    user_guess = add_guess(user_guess, previous_guesses)
    previous_guesses.append(user_guess)

    if user_guess == random_number:
        print("You guessed correctly!")
        print("The number was", random_number)
        break
    elif user_guess > random_number:
        # when guess is less than the random number
        print("Try again! The random number is lower!")
        
    else:
        # when guess is greater than the random number
        print("Try again! The random number is higher!")

    if user_guess != random_number:
        guess = guess - 1
        print("Previous guesses:", previous_guesses)
        if guess != 0:
            print("You have", guess, "guesses left.")
        else: 
            print("You have no guesses left.")
            print("The correct number was", random_number)
            print("Game over!")