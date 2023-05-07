import pandas


def num_check(question, error, num_type):
    while True:
        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def not_blank(question, error):
    while True:
        response = input(question).strip()

        if response == "":
            print(error)
        else:
            return response


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Gets expenses, returns list which has
# the data frame and sub-total
def get_expenses(var_fixed):
    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # Get user data
    product_name = not_blank("Product name: ", "The product name can't be blank.")

    # loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":

        print()
        # get name, quantity and item
        item_name = not_blank("Item name: ",
                              "The component name can't be blank.")
        if item_name.lower() == "xxx":
            break

        quantity = num_check("Quantity: The amount must be a whole number more than zero ",
                             "Please enter a valid quantity.",
                             int)
        price = num_check("How much for a single item? $",
                          "Please enter a valid price (more than 0).",
                          float)

        # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    variable_frame = pandas.DataFrame(variable_dict)
    variable_frame = variable_frame.set_index('Item')

    # Calculate cost of each component
    variable_frame['Cost'] = variable_frame['Quantity'] * variable_frame['Price']

    # Find sub-total
    variable_sub = variable_frame['Cost'].sum()

    # Currency Formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        variable_frame[item] = variable_frame[item].apply(currency)

    # *** Printing Area ****
    print(variable_frame)

    print(f"\nSub-total: {currency(variable_sub)}\n")


# Main routine goes here

get_expenses(var_fixed)