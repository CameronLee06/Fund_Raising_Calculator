def num_check(question, error, num_type):
    # Set a flag to False to enter the validation loop.
    valid = False

    # Continue looping until a valid input is received.
    while not valid:

        try:
            # Try to convert the user input to the specified data type.
            response = num_type(input(question))

            # Check if the resulting number is greater than 0.
            if response <= 0:
                # Print an error message if the number is not positive.
                print(error)
            else:
                # Return the number if it is positive and the conversion was successful.
                return response

        except ValueError:
            # Print an error message if the user input is not a valid number.
            print(error)
