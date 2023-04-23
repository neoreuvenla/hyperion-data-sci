# task 7 - while loops
# code provides the average value of the guesses of a secret number 

secret_number = -1  # target number
user_number = 0     # current guess
user_total = 0      # current value of the guesses
i = 0               # loop counter

# loop until the secret number is correctly guessed
while user_number != secret_number: 

    # prompts user for next guess
    user_number = int(input("Please enter a positive or negative number: "))

    if user_number == secret_number:  # breaks the loop if guess is accurate
        break
    
    else:  # if current guess is incorrect
        user_total = user_total + user_number # adds guess to total
        i += 1 # increments the loop

# calculates the average and prints to user: total / iterations
print("The average of the incorrect guesses is: {}".format(user_total / i) )
