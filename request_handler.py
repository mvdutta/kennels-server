from urllib.parse import urlparse, parse_qs
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_animals, get_single_animal, get_all_locations, get_single_location, get_all_employees, get_single_employee, get_all_customers, get_single_customer, create_animal, create_location, create_employee, create_customer, delete_animal, delete_location, delete_employee, delete_customer, update_animal, update_customer, update_location, update_employee, get_customer_by_email, get_animal_by_location


# Here's a class. It inherits from another class.
# For now, think of a class as a container for functions that
# work together for a common purpose. In this case, that
# common purpose is to respond to HTTP requests from a client.
class HandleRequests(BaseHTTPRequestHandler):
    # This is a Docstring it should be at the beginning of all classes and functions
    # It gives a description of the class or function
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    # Here's a class function

    def parse_url(self, path):
        """Parse the url into the resource and id"""
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split('/')  # ['', 'animals', 1]
        resource = path_params[1]

        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)

        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass
        return (resource, pk)

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.
    def do_GET(self):
        """Handles GET requests to the server...responds to the client's GET request
        """
        response = {}  # Default response

        # Parse the URL and store the tuple that is returned in a variable parsed
        parsed = self.parse_url(self.path)
        # If the path does not include a query parameter, continue with the original if block
        if '?' not in self.path:
            (resource, id) = parsed

            if resource == "animals":
                if id is not None:
                    response = get_single_animal(id)
                    if response:
                        self._set_headers(200)
                    else:
                        self._set_headers(404)
                        response = {
                            "message": f'The id of {id} is not valid'
                        }
                else:
                    self._set_headers(200)
                    response = get_all_animals()         
            elif resource == "locations":
                if id is not None:
                    response = get_single_location(id)
                    if response:
                        self._set_headers(200)
                    else:
                        self._set_headers(404)
                        response = {
                            "message": f'The id of {id} is not valid'
                        }
                else:
                    self._set_headers(200)
                    response = get_all_locations()
            elif resource == "employees":
                if id is not None:
                    response = get_single_employee(id)
                    if response:
                        self._set_headers(200)
                    else:
                        self._set_headers(404)
                        response = {
                            "message": f'The id of {id} is not valid'
                        }
                else:
                    self._set_headers(200)
                    response = get_all_employees()
            elif resource == "customers":
                if id is not None:
                    response = get_single_customer(id)
                    if response:
                        self._set_headers(200)
                    else:
                        self._set_headers(404)
                        response = {
                            "message": f'The id of {id} is not valid'
                        }
                else:
                    self._set_headers(200)
                    response = get_all_customers()
        else: #There is a ? in the path, run the query param functions
            (resource, query) = parsed

            # see if the query dictionary has an email key
            if query.get('email') and resource == 'customers':
                response = get_customer_by_email(query['email'][0])
                if response:
                    self._set_headers(200)
                else:
                    self._set_headers(404)
                    response = {"message": "Customer not found."}
            if query.get('location_id') and resource == 'animals':
                response = get_animal_by_location(query['location_id'][0])
                if response:
                    self._set_headers(200)
                else:
                    self._set_headers(404)
                    response = {"message": "Animal not found."}
        # writing to the response to the client...dictionary is encoded as a string (json.dumps)
        self.wfile.write(json.dumps(response).encode())
    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.
    def do_POST(self):
        """Handles POST requests to the server """
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new animal
        new_animal = None
        if resource == "animals":
            # if "name" in post_body and "species" in post_body and "locationId" in post_body and "customerId" in post_body and "status" in post_body:
            keys = ['name', 'species', 'locationId', 'customerId', 'status']
            if has_all_keys(post_body, keys):
                self._set_headers(201)
                new_animal = create_animal(post_body)
            else:
                self._set_headers(400)
                # create a dictionary with one key called message and store it in new_animal using a Python version of a ternary statement

                #make a list of the keys in post_body using the built-in keys() function and convert it into python list using list(...). Call this post_body_keys
                post_body_keys = list(post_body.keys())

                #use a list comprehension to find those keys in "keys" that are not present in post_body_keys
                missing_keys = [key for key in keys if key not in post_body_keys]
                msg = ", ".join(missing_keys) + " missing. Please update."
                
                new_animal = {
                    "message": msg
                }
        # Encode the new animal and send in response
            self.wfile.write(json.dumps(new_animal).encode())
        # Initialize new location
        new_location = None
        if resource == "locations":
            # check to see if the dictionary has the keys: name and address
            if "name" in post_body and "address" in post_body:
                self._set_headers(201)
                new_location = create_location(post_body)
            else:
                self._set_headers(400)
                # create a dictionary with one key called message and store it in new_location using a Python version of a ternary statement
                new_location = {
                    "message": f'{"name is required" if "name" not in post_body else ""} {"address is required" if "address" not in post_body else ""}'
                }
        # Encode the new location and send in response
            self.wfile.write(json.dumps(new_location).encode())
            return
        # Initialize new employee
        new_employee = None
        if resource == "employees":
            if "name" in post_body:
                self._set_headers(201)
                new_employee = create_employee(post_body)
            else:
                self._set_headers(400)
                # create a dictionary with one key called message and store it in new_employee using a Python version of a ternary statement
                new_employee = {
                    "message": f'{"name is required" if "name" not in post_body else ""}'
                }

        # Encode the new employee and send in response
            self.wfile.write(json.dumps(new_employee).encode())
            # Initialize new customer
        new_customer = None
        if resource == "customers":
            if "name" in post_body:
                self._set_headers(201)
                new_customer = create_customer(post_body)
            else:
                self._set_headers(400)
                new_customer = {
                    "message": f'{"name is required" if "name" not in post_body else ""}'
                }

        # Encode the new customer and send in response
            self.wfile.write(json.dumps(new_customer).encode())

    def do_DELETE(self):
        """method to process the DELETE request. Uses response code 204: request processed, no information to send back/don't need to refresh"""

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "animals":
            self._set_headers(204)
            delete_animal(id)

        # Encode the new animal and send in response
            self.wfile.write("".encode())

        if resource == "locations":
            self._set_headers(204)
            delete_location(id)

            self.wfile.write("".encode())        
        if resource == "employees":
            self._set_headers(204)
            delete_employee(id)

            self.wfile.write("".encode())
        if resource == "customers":
            # delete_customer(id)
            self._set_headers(405)
            response = {
                "message":'Deleting customers is not permitted. Please contact the company.'
            }
            self.wfile.write(json.dumps(response).encode())

    # A method that handles any PUT request.

    def do_PUT(self):
        """Handles PUT requests to the server"""
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

     # Delete a single animal from the list
        if resource == "animals":
            update_animal(id, post_body)

    # Encode the new animal and send in response
            self.wfile.write("".encode()) 
    # Delete a single location from the list
        if resource == "locations":
            update_location(id, post_body)

            self.wfile.write("".encode())
    # Delete a single employee from the list
        if resource == "employees":
            update_employee(id, post_body)

            self.wfile.write("".encode())
    # Delete a single customer from the list
        if resource == "customers":
            update_customer(id, post_body)

            self.wfile.write("".encode())
    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()


def has_all_keys(dict, key_list):
    '''Checks if the dictionary dict has all the keys in the list key_list. Returns false if any of the keys are not found, and true if all the keys are found'''
    for key in key_list:
        if key not in dict:
            return False
    return True


# This function is not inside the class. It is the starting
# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
