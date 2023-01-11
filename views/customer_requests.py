import sqlite3
import json
from models import Customer

# CUSTOMERS = [
#     {
#         "id": 1,
#         "name": "Luke Skywalker"
#     },
#     {
#         "id": 2,
#         "name": "Leia Organa"
#     }
# ]
# def get_all_customers():
#     """returns CUSTOMERS list of dictionaries"""
#     return CUSTOMERS

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


def get_all_customers():
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer c
        """)

        # Initialize an empty list to hold all customer representations
        customers = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create a customer instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Customer class above.
            customer = Customer(row['id'], row['name'], row['address'], row['email'], row['password'])

            customers.append(customer.__dict__)

    return customers

def get_single_customer(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer c
        WHERE c.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create a customer instance from the current row
        customer = Customer(data['id'], data['name'],
                            data['address'], data['email'], data['password'])

        return customer.__dict__
