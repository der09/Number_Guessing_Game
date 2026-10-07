# Number Guessing Game 
# Diane Hsieh 
# AM 

# importing a python module
import random 

# returns random integer 1 to 10, including endpoints
random_number = random.randint(1, 10)

# array for guesses player has made
previous_guesses = [] 

# asking users guess 
user_guess = int(input("Enter a number between 1 - 10: "))


not_dupe = False
def add_guess(user_guess, previous_guesses): 

    # gives invalid input if guess is out of range 
    while user_guess > 10 or user_guess < 1: 
        print("Invalid input!")
        user_guess = int(input("Enter a number between 1 - 10: "))
    # makes sure not duplicate 
    while not_dupe == False:
        for i in previous_guesses: 
            if user_guess in previous_guesses: 
                print("You already guessed:", i)
                print("Choose a different number.")
                print("Previous guesses:", previous_guesses)
            else: 
                if user_guess < 10 or user_guess > 1: 
                    return True
                else:
                    return False 



# compare guess to random number 
if (user_guess == random_number): 
    print("You guessed correctly!")
elif (user_guess > random_number): 
    print("Try again! The random number is lower!")
else: 
    print("Try again! The random number is higher!")

# if guess doesn't equal random number 
while user_guess != random_number: 
    print("Previous guesses:", previous_guesses)
    user_guess = int(input("Enter a number between 1 - 10: "))
    
if (add_guess(user_guess, previous_guesses) == True): 
    previous_guesses.append(user_guess)
