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
