import requests

class APIConsumer:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        
    def _make_request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def addPet(self, **kwargs):
        """Add a new pet to the store
        Add a new pet to the store
        """
        return self._make_request("POST", "/pet", **kwargs)

    def updatePet(self, **kwargs):
        """Update an existing pet
        Update an existing pet by Id
        """
        return self._make_request("PUT", "/pet", **kwargs)

    def findPetsByStatus(self, **kwargs):
        """Finds Pets by status
        Multiple status values can be provided with comma separated strings
        """
        return self._make_request("GET", "/pet/findByStatus", **kwargs)

    def findPetsByTags(self, **kwargs):
        """Finds Pets by tags
        Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.
        """
        return self._make_request("GET", "/pet/findByTags", **kwargs)

    def getPetById(self, **kwargs):
        """Find pet by ID
        Returns a single pet
        """
        return self._make_request("GET", "/pet/{petId}", **kwargs)

    def updatePetWithForm(self, **kwargs):
        """Updates a pet in the store with form data
        
        """
        return self._make_request("POST", "/pet/{petId}", **kwargs)

    def deletePet(self, **kwargs):
        """Deletes a pet
        
        """
        return self._make_request("DELETE", "/pet/{petId}", **kwargs)

    def uploadFile(self, **kwargs):
        """uploads an image
        
        """
        return self._make_request("POST", "/pet/{petId}/uploadImage", **kwargs)

    def getInventory(self, **kwargs):
        """Returns pet inventories by status
        Returns a map of status codes to quantities
        """
        return self._make_request("GET", "/store/inventory", **kwargs)

    def placeOrder(self, **kwargs):
        """Place an order for a pet
        Place a new order in the store
        """
        return self._make_request("POST", "/store/order", **kwargs)

    def getOrderById(self, **kwargs):
        """Find purchase order by ID
        For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.
        """
        return self._make_request("GET", "/store/order/{orderId}", **kwargs)

    def deleteOrder(self, **kwargs):
        """Delete purchase order by ID
        For valid response try integer IDs with value < 1000. Anything above 1000 or nonintegers will generate API errors
        """
        return self._make_request("DELETE", "/store/order/{orderId}", **kwargs)

    def createUser(self, **kwargs):
        """Create user
        This can only be done by the logged in user.
        """
        return self._make_request("POST", "/user", **kwargs)

    def createUsersWithListInput(self, **kwargs):
        """Creates list of users with given input array
        Creates list of users with given input array
        """
        return self._make_request("POST", "/user/createWithList", **kwargs)

    def loginUser(self, **kwargs):
        """Logs user into the system
        
        """
        return self._make_request("GET", "/user/login", **kwargs)

    def logoutUser(self, **kwargs):
        """Logs out current logged in user session
        
        """
        return self._make_request("GET", "/user/logout", **kwargs)

    def getUserByName(self, **kwargs):
        """Get user by user name
        
        """
        return self._make_request("GET", "/user/{username}", **kwargs)

    def updateUser(self, **kwargs):
        """Update user
        This can only be done by the logged in user.
        """
        return self._make_request("PUT", "/user/{username}", **kwargs)

    def deleteUser(self, **kwargs):
        """Delete user
        This can only be done by the logged in user.
        """
        return self._make_request("DELETE", "/user/{username}", **kwargs)
