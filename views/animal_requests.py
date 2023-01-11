from .location_requests import get_single_location
from .customer_requests import get_single_customer
ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4,
        "status": "Admitted"
    },
    {
        "id": 2,
        "name": "Roman",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2,
        "status": "Admitted"
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1,
        "status": "Admitted"
    }
]


def get_all_animals():
    """returns ANIMAL list of dictionaries"""
    return ANIMALS

# Function with a single parameter
# the responsibility of this function is to look up a single animal
# the id of the animal has to be passed as an argument.


def get_single_animal(id):
    """Variable to hold the found animal, if it exists"""
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal
            # accessing the locationId of the animal and storing it in variable location_id
            location_id = animal["locationId"]
            # created a new key (location) and storing the information from the location obtained from function get_single_location
            requested_animal["location"] = get_single_location(location_id)
            # no longer need locationId key anymore
            del requested_animal['locationId']
            customer_id = animal['customerId']
            requested_animal["customer"] = get_single_customer(customer_id)
            del requested_animal['customerId']
    return requested_animal


def create_animal(animal):
    """Creates a new animal dictionary in the ANIMALS list of dictionaries"""
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list {append is similar to push}
    ANIMALS.append(animal)

    # Return the dictionary with `id` property added
    return animal


def delete_animal(id):
    """remove animal dictionary from the list"""
    # Initial -1 value for animal index, in case one isn't found
    animal_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Store the current index.
            animal_index = index

    # If the animal was found, use pop(int) to remove it from list
    if animal_index >= 0:
        ANIMALS.pop(animal_index)


def update_animal(id, new_animal):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    """iterates the list of animals until it finds the right one, and then replaces it with what the client sent as the replacement."""
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Update the value.
            ANIMALS[index] = new_animal
            break
