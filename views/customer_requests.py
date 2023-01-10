CUSTOMERS = [
    {
        "id": 1,
        "name": "Luke Skywalker"
    },
    {
        "id": 2,
        "name": "Leia Organa"
    }
]
def get_all_customers():
    """returns CUSTOMERS list of dictionaries"""
    return CUSTOMERS

# Function with a single parameter
def get_single_customer(id):
    """ Variable to hold the found customer, if it exists """
    requested_customer = None
    for customer in CUSTOMERS:
        if customer['id'] == id:
            requested_customer = customer
    return requested_customer


def create_customer(customer):
    """Creates a new customer dictionary in the CUSTOMERS list of dictionaries"""
    # Get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the customer dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list {append is similar to push}
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer

def delete_customer(id):
    """remove customer dictionary from the list"""
    # Initial -1 value for animal index, in case one isn't found
    customer_index = -1

    # Iterate the CUSTOMER list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Store the current index.
            customer_index = index

    # If the customer was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    # Iterate the CUSTOMERS list, but use enumerate() so that
    # you can access the index value of each item.
    """iterates the list of customers until it finds the right one, and then replaces it with what the client sent as the replacement."""
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Update the value.
            CUSTOMERS[index] = new_customer
            break
