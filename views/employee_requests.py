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
