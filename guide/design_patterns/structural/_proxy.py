"""
Proxy design pattern

* Proxy is a structural design pattern that lets you provide a substitute or
  placeholder for another object. A proxy controls access to the original
  object, allowing you to perform something either before or after the request
  gets through to the original object
* The Proxy pattern suggests that you create a new proxy class with the same
  interface as an original service object. Then you update your app so that it
  passes the proxy object to all of the original object’s client
"""
from abc import ABC, abstractmethod


# Request ABC
class Request(ABC):
    @abstractmethod
    def do_request(self):
        pass


# Api request
class ApiRequest(Request):
    def __init__(self, url, data):
        self.url = url
        self.data = data

    def do_request(self):
        print('Request successfully')


# Auth request
class AuthRequestProxy(Request):
    def __init__(self, api_request):
        self.api_request = api_request

    def do_request(self):
        if 'token' in self.api_request.data:
            self.api_request.do_request()
        else:
            print('Forbidden')


# Algorithm
request = ApiRequest('www.api.com', {})
request.do_request()
# Request successfully

auth_request = AuthRequestProxy(request)
auth_request.do_request()
# Forbidden

request = ApiRequest('www.api.com', {'token': '123'})
auth_request = AuthRequestProxy(request)
auth_request.do_request()
# Request successfully
