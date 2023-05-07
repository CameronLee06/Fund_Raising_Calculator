import pandas as pd


# *** functions go here ****

# checks that input is either a float or an
# integer that is more than zero. Takes in custom error message


def yes_no(question):
    to_check = ["yes", "no"]
    valid = False
    while not valid:
        response = input(question).lower()
        if response in to_check:
            return response
        elif response == to_check[0][0]:
            return to_check[0]
        elif response == to_check[1][0]:
            return to_check[1]
        else:
            print("Please enter either 'yes' or 'no'...\n")


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
            print("{}. \nPlease try again.\n".format(error))
        else:
            return response


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Gets expenses, returns list which has
# the data frame and sub-total

def get_expenses(var_fixed):
    # Set up dictionaries and lists
    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }
    # loop to get component, quantity, and price
    item_name = ""
    while item_name.lower() != "xxx":
        print()
        # get name, quantity, and item
        item_name = not_blank("Item name: ",
                              "The component name can't be blank.")
        if item_name.lower() == "xxx":
            break

        if var_fixed == "fixed":
            quantity = 1
        else:
            quantity = num_check("Quantity: ",
                                 "The amount must be a whole number "
                                 "more than zero",
                                 int)
        price = num_check("How much for a single item? $",
                          "The price must be a number greater than 0",
                          float)

        # add item, quantity, and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expenses_frame = pd.DataFrame(variable_dict)
    expenses_frame = expenses_frame.set_index('Item')

    # Calculate cost of each component
    expenses_frame['Cost'] = expenses_frame['Quantity'] * expenses_frame['Price']

    # Find sub-total
    sub_total = expenses_frame['Cost'].sum()

    # Currency Formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expenses_frame[item] = expenses_frame[item].apply(currency)
    return [expenses_frame, sub_total]


# prints expense frames
def expense_print(heading, frame, subtotal):
    print()

    print("**** {} Costs ****".format(heading))
    print(frame)
    print()
    print("{} Costs: ${:.2f}".format(heading, subtotal))
    return ""


product_name = not_blank("Product name: ", "The product name can't be blank.")

# *** Main routine starts here ***
# Get product name

print()
print("Please enter your variable cost below")
# Get variable costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

print()
have_fixed = yes_no("Do you have fixed costs? (y / n)? ")

if have_fixed == "yes":
    # Get fixed costs
    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]

else:
    fixed_frame = ""
    fixed_sub = 0

# Find Total Costs

# Ask user for profit goals

# Calculate recommended price

# write data to file

# *** Printing Area ***

print()
print("***** Fund Raising - {} *****".format(product_name))
print()
expense_print("Variable", variable_frame, variable_sub)

if have_fixed == "yes":
    expense_print("Fixed", fixed_frame[['Cost']], fixed_sub)
