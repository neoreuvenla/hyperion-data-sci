# task 14 - defining functions
# calculates the cost of a holiday from user inputs using functions

seperator_string = "---------------------------------------------------"  # decorate outputs
destination_cities = ["London", "Madrid", "Tokyo"]  # available cities

# helper function to calculate the hotel price based on number of nights
def hotel_cost(num_nights):      
    return num_nights * 105  # £105 per night

# helper function to calculate flight cost depending on destination
def plane_cost(city_flight):
    if city_flight == destination_cities[0]:  # to london £45
        return 45

    elif city_flight == destination_cities[1]:  # to madrid £80
        return 80

    elif city_flight == destination_cities[2]:  # to tokyo £155
        return 155

# helper function to calculate car rental price based on number of days
def car_rental(rental_days):
    return rental_days * 55  # £55 per day

# main function calling multiple functions to calculate a total holiday price
def holiday_cost(city_flight, num_nights, rental_days):
    # total cost = hotel cost + plane cost + rental cost
    total_cost = plane_cost(city_flight) + hotel_cost(num_nights) + car_rental(rental_days)
    return total_cost

# user input loop starts here
while True:

    # prompt for destination
    city_flight = input("Enter the city you are flying to ({}, {}, {}):\t".format(
        destination_cities[0], destination_cities[1], destination_cities[2]))

    while city_flight not in destination_cities:  # city input validation
        print("Error: Please select an available city\n")
        city_flight = input("Enter the city you are flying to ({}, {}, {}):\t".format(
            destination_cities[0], destination_cities[1], destination_cities[2]))

    # try block anticipating issues with numerical inputs
    while True:
        try:
            # prompt for length of stay
            num_nights = int(input("Enter the number of nights you will be staying at the hotel:\t"))
            
            while num_nights < 0:  # nights input validation
                print("Error: Please chose a positive number of days\n")
                num_nights = int(input("Enter the number of nights you will be staying at the hotel:\t"))

            # prompt for rental usage
            rental_days = int(input("Enter the number of days that you will be hiring a car for:\t"))

            while rental_days < 0:  # rental input validation
                print("Error: Please chose a positive number of days\n")
                rental_days = int(input("Enter the number of days that you will be hiring a car for:\t"))

            # break out of input loop if inputs are valid
            break

        except ValueError:
            # error handling for strings entered as integers
            print("Error: Please enter a valid integer\n")

        except Exception:
            # catch all for any unexpected errors
            print("Error: An unknown error has occured. Please review your input and try again\n")

    # variable to hold the result of the holiday cost function call
    total_cost = holiday_cost(city_flight, num_nights, rental_days)

    # print summary details in a clearly formatted manner
    print("\n" + seperator_string)
    print("Your Holiday Summary:\n")
    print("+ City of flight:\t\t{}".format(city_flight))
    print("+ Number of nights at hotel:\t{}".format(num_nights))
    print("+ Number of days of car rental:\t{}".format(rental_days))
    print(seperator_string)
    print("= Total holiday cost:\t\t£{:.2f}".format(total_cost))
    print(seperator_string + "\n")

    # prompt to start the loop again
    repeat = input("Would you like to calculate another holiday? (y/n):")

    while repeat.lower() not in ("y", "n"):  # repeat loop validation
        print("Please enter a valid option\n")
        repeat = input("Would you like to calculate another holiday? (y/n): ")

    if repeat.lower() == "n":  # exits program
        break
