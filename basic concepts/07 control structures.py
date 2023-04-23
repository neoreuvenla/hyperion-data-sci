# task 5 - variables and control structures
# code provides investment and bond calculations from various user inputs

# imports
import math

# global variable used in formatting outputs for clarity
seperator_string = "-------------------------------------------"

# prints welcome block with choices for user at program start
print("\n" + seperator_string)
print("investment \t- to calculate the amount of interest you'll earn on your investment")
print("bond \t\t- to calculate the amount you'll have to pay on a home loan")

# prompts for a user choice based on the welcome block
user_choice = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ")
print(seperator_string)
print("\n" + seperator_string)

if user_choice.lower() == "investment":  # if any form "investment" chosen

    print("Please enter this information in whole numbers or letters as appropriate:\n")

    # block of prompts for user investment information
    deposit_value = int(input("How much are you depositing?\t"))
    interest_rate = int(input("What is the interest rate?\t")) / 100
    investment_years = int(input("How many years for?\t\t"))
    interest = input("Simple or compound interest?:\t")
    print(seperator_string)

    if interest.lower() == "simple":  # if any form "simple" chosen

        # simple interest calculation: A = P*(1 + r*t)
        simple_total = deposit_value * (1 + (interest_rate) * investment_years)

        # prints block of summary information and total yield
        print("\n" + seperator_string)
        print("Deposit Value:\t £{:.2f}".format(deposit_value))
        print("Interest Rate:\t {:.2f}%".format(interest_rate*100))
        print("Interest Type:\t {}".format(interest.capitalize()))
        print("Invest Period:\t {} years".format(investment_years))
        print(seperator_string)
        print("Total Yield:\t £{:.2f}".format(simple_total))
        print(seperator_string + "\n")

    elif interest.lower() == "compound":  # if any form "compound" chosen

        # compound interest calculation: A = P * math.pow((1+r),t)
        compound_total = deposit_value * math.pow((1 + interest_rate), investment_years)

        # prints block of summary information and total yield
        print("\n" + seperator_string)
        print("Deposit Value:\t £{:.2f}".format(deposit_value))
        print("Interest Rate:\t {:.2f}%".format(interest_rate*100))
        print("Interest Type:\t {}".format(interest.capitalize()))
        print("Invest Period:\t {} years".format(investment_years))
        print(seperator_string)
        print("Total Yield:\t £{:.2f}".format(compound_total))
        print(seperator_string + "\n")

    else:  # error handling if no valid option chosen
    
        print("\n" + seperator_string)
        print("Error: Please enter either ""simple"" or ""compound"" interest")
        print(seperator_string + "\n")

elif user_choice.lower() == "bond":  # if any form "bond" chosen
    
    print("Please enter this information in whole numbers or letters as appropriate:\n")

    # block of prompts for user bond information
    house_value = int(input("What is value of the house?\t"))
    interest_rate = int(input("What is the interest rate?\t")) / 100
    monthly_interest = (interest_rate) / 12
    repayment_months = int(input("How many repayment months?\t"))
    print(seperator_string)

    # bond repayment calculation: repayment = (i * P)/(1 - (1 + i)**(-n))
    monthly_payment = (monthly_interest * house_value)/(1 - (1 + monthly_interest)**(-repayment_months))

    # prints block of summary information and monthly repayment amount
    print("\n" + seperator_string)
    print("House Value:\t £{:.2f}".format(house_value))
    print("Interest Rate:\t {:.2f}%".format(interest_rate*100))
    print("Monthly Rate:\t {:.2f}%".format(monthly_interest*100))
    print("Bond Period:\t {} months".format(repayment_months))
    print(seperator_string)
    print("Monthly Payment: £{:.2f}".format(monthly_payment))
    print(seperator_string + "\n")

else:  # error handling if no valid option chosen
    
    print("Error: Please enter a valid option from the menu")
    print(seperator_string + "\n")
