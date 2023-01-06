EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis"
    },
    {
        "id": 2,
        "name": "Richard Parker"
    }
]
def get_all_employees():
    """returns EMPLOYEES list of dictionaries"""
    return EMPLOYEES

# Function with a single parameter
def get_single_employee(id):
    """ Variable to hold the found employee, if it exists """
    requested_employee = None
    for employee in EMPLOYEES:
        if employee['id'] == id:
            requested_employee = employee
    return requested_employee


def create_employee(employee):
    """Creates a new location dictionary in the EMPLOYEE list of dictionaries"""
    # Get the id value of the last employee in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the location dictionary
    employee["id"] = new_id

    # Add the location dictionary to the list {append is similar to push}
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee
