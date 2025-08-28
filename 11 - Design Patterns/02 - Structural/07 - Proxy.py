"""
Proxy

* The Proxy pattern is a structural design pattern that provides an object
  representing another object.
* It acts as a surrogate or placeholder for another object to control access to
  it.
"""


###############################################################################
# Proxy
###############################################################################


# Importing modules
# * We will import some resources to be used in the example below.
from abc import ABC, abstractmethod


# Request
# * Abstract class for handling requests.
class Request(ABC):
    @abstractmethod
    def submit(self, payload: str, token: str = None) -> None:
        pass


# API Request
# * Concrete implementation of the Request interface for API calls.
class APIRequest(Request):
    def submit(self, payload: str, token: str = None) -> None:
        print(f"Request submitted")


# Authorized Request
# * Proxy for API requests that require authorization.
# * Note that the AuthRequest class is a proxy that adds an authorization layer
#   to the APIRequest.
class AuthRequest(Request):
    def __init__(self, req: Request):
        self.req = req

    def submit(self, payload: str, token: str = None) -> None:
        if token is None:
            print("Unauthorized")
            return
        self.req.submit(payload, token)


# Testing
# * Now, note that the AuthRequest class is used to add an authorization layer
#   to the APIRequest.
api_request = APIRequest()
auth_request = AuthRequest(api_request)
auth_request.submit("...", "token123")
# Request submitted
