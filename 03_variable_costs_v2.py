import pandas


def get_input(prompt, error, input_type):
    while True:
        try:
            response = input_type(input(prompt))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


def not_blank(prompt, error):
    while True:
        response = input(prompt)
        if response == "":
            print(f"{error}. Please try again.")
        else:
            return response


# currency formatting function
def format_currency(x):
    return "${:,.2f}".format(x)


def main():
    # set up lists to store item details
    items = []
    quantities = []
    prices = []

    # get product name from user
    product_name = not_blank("Product name: ", "Product name can't be blank.")

    # loop to get item details from user
    while True:
        item_name = not_blank("Item name (enter 'xxx' to finish): ", "Item name can't be blank.")
        if item_name.lower() == "xxx":
            break

        quantity = get_input("Quantity: ", "Quantity must be a positive whole number.", int)
        price = get_input("Price per item: $", "Price must be a positive number.", float)

        # add item details to lists
        items.append(item_name)
        quantities.append(quantity)
        prices.append(price)

    # create a pandas DataFrame to store item details
    item_dict = {
        "Item": items,
        "Quantity": quantities,
        "Price": prices,
    }
    item_df = pd.DataFrame(item_dict)
    item_df.set_index("Item", inplace=True)

    # calculate the cost of each item and the total cost
    item_df["Cost"] = item_df["Quantity"] * item_df["Price"]
    total_cost = item_df["Cost"].sum()

    # format prices and costs as currency
    item_df["Price"] = item_df["Price"].apply(format_currency)
    item_df["Cost"] = item_df["Cost"].apply(format_currency)
    total_cost = format_currency(total_cost)

    # print the item details and total cost
    print(item_df)
    print(f"Total cost for {product_name}: {total_cost}")


if __name__ == "__main__":
    main()
    