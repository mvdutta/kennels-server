LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    }
]
def get_all_locations():
    """returns LOCATIONS list of dictionaries"""
    return LOCATIONS

# Function with a single parameter
def get_single_location(id):
    """ Variable to hold the found location, if it exists """
    requested_location = None
    for location in LOCATIONS:
        if location['id'] == id:
            requested_location = location
    return requested_location


def create_location(location):
    """Creates a new location dictionary in the LOCATIONS list of dictionaries"""
    # Get the id value of the last location in the list
    max_id = LOCATIONS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the location dictionary
    location["id"] = new_id

    # Add the location dictionary to the list {append is similar to push}
    LOCATIONS.append(location)

    # Return the dictionary with `id` property added
    return location
