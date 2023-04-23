# task 3 - if, elif, else
# code to validate that a user input is an appropriate length for a full name

# requests a name and assigns to a variable
full_name = input("Please enter your full name:")

if not full_name:  # if full_name variable is empty
    print("You haven’t entered anything. Please enter your full name")
elif len(full_name) < 4:  # if string is under 4 characters long
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname")
elif len(full_name) > 25:  # if string is 25 characters long
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name")
else:  # if all checks are false
    print("Thank you for entering your name")
