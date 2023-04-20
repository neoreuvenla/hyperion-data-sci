# code offers users basic calculation functions or retrieval  of previous calculations

# global variable used to format certain outputs for clarity
seperator_string = "---------------------------------------------------"

# prints welcome message only when first starting the program
print(seperator_string)
print("Please selection from the following options:")

while True:

    # prompts user for choice of mode
    mode_selection = input("Perform calculation (c), File read (r), Exit program (x): ")
    
    # mode input validation
    while mode_selection.lower() not in ['c', 'r', 'x']:
        print("Error: Please enter a valid option\n")
        mode_selection = input("Perform calculation (c), File read (r), Exit program (x): ")
            
    if mode_selection.lower() == 'c':  # perform calculation selected

        # try block to help catch input errors
        try:
            first_number = float(input("\nEnter the first number:\t\t"))  # first number input
            
            operator = input("Enter the operator (+ - * /):\t")   # operator input

            # operator input validation
            if operator not in ['+', '-', '*', '/']:
                # raises try block ValueError with custom message
                raise ValueError("Invalid operator selected")

            second_number = float(input("Enter the second number:\t"))  # second number input

            # division by zero check
            if (second_number == 0) and (operator == "/"):
                # raises try block ZeroDivisionError with custom message
                raise ZeroDivisionError("Unable to divide by zero")

            # calculate the result depending on operator
            if operator == '+':
                result = first_number + second_number
            elif operator == '-':
                result = first_number - second_number
            elif operator == '*':
                result = first_number * second_number
            elif operator == '/':
                result = first_number / second_number

            # variable to hold properly formatted equation
            equation = "{} {} {} = {}".format(first_number, operator, second_number, result)

            # prints the equation with result
            print(seperator_string)
            print("Result:\t\t\t\t" + equation)
            print(seperator_string + "\n")

            # open file, adds previous equation, closes when block exited
            with open("equations.txt", "a") as file:  # append will create file if none
                file.write(equation + "\n")

        # value error message formatting 
        except ValueError as error:
            print("Error: {}\n".format(error))
        
        # divide by zero message formatting 
        except ZeroDivisionError as error:
            print("Error: {}\n".format(error))
        
        # catch all for any unexpected errors
        except Exception:
            print("An unexpected error occurred\n")

    elif mode_selection.lower() == 'r':  # file read selected

        # prints user instructions for file reading 
        print("\nCalculations are written to equations.txt")
        print("Data from other .txt files can also be read\n")

        # try block to help catch file handling errors
        try:
            # prompts user for name of file
            filename = input("Enter the name of the file to read: ")
                
            print(seperator_string)

            # opens given file in read only mode and prints contents
            with open(filename, 'r') as file:
                content = file.read()
                print(content)

            # prints confirmation message, useful in case of empty files
            print("Read complete")
            print(seperator_string + "\n")
            
        # file not found error message formatting
        except FileNotFoundError:
            print("Error: file not found\n")
            
        # catch all for any unexpected errors
        except Exception:
            print("An unexpected error occurred")
           
    elif mode_selection.lower() == 'x':  # exit program selected
        print("Exiting")
        break