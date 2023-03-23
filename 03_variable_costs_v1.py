import pandas


def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print(f"{error}. \nPlease try again. \n")
            continue

        return response


# currency formatting function
def currency(x): ...

# Main routine goes here
